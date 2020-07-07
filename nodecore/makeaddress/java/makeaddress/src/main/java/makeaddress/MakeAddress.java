// VeriBlock NodeCore
// Copyright 2017-2020 Xenios SEZC
// All rights reserved.
// https://www.veriblock.org
// Distributed under the MIT software license, see the accompanying
// file LICENSE or http://www.opensource.org/licenses/mit-license.php.

package makeaddress;

import com.google.gson.*;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.security.spec.ECGenParameterSpec;
import java.util.*;

public class MakeAddress {
    private static KeyPairGenerator keyPairGenerator;

    private static final String HEX_ALPHABET = "0123456789ABCDEF";
    private static final char[] HEX_ALPHABET_ARRAY = HEX_ALPHABET.toCharArray();
    private static final char STARTING_CHAR = 'V';
    private final static int ADDRESS_DATA_START = 0;
    private final static int ADDRESS_DATA_END = 24;
    private final static int ADDRESS_CHECKSUM_START = 25;
    private final static int ADDRESS_CHECKSUM_END = 29;
    private final static int ADDRESS_CHECKSUM_LENGTH = ADDRESS_CHECKSUM_END - ADDRESS_CHECKSUM_START;
    private static final int WALLET_VERSION = 0x02;
    private static final int KEY_TYPE = 0x01;

    static {
        try {
            keyPairGenerator = KeyPairGenerator.getInstance("EC");

            /* Initialize the KeyPairGenerator to create 256-bit ECDSA-secp256k1.
             * Bitcoin + co. use ECDSA-secp256k1 (a Koblitz curve). While mathematically secp256r1 is believed to be marginally
             * more secure (~1%), the secp256k1 curve is more 'rigid', and the choosing of apparently 'random' parameters
             * for secp256r1 are suspicious--NIST claims that the 'random' parameters are more efficient, despite
             * evidence that other prime choices are more efficient. */
            keyPairGenerator.initialize(new ECGenParameterSpec("secp256k1"));
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    private KeyPair generateKeyPair() {
        return keyPairGenerator.generateKeyPair();
    }

    private String addressFromPublicKey(byte[] publicKey) {
        final Crypto crypto = new Crypto();
        // Calculate the SHA-256 of the public key, encode as base-58, take the first 24 characters, prepend a 'V' for VeriBlock
        String address = STARTING_CHAR + crypto.SHA256ReturnBase58(publicKey).substring(ADDRESS_DATA_START, ADDRESS_DATA_END);
        // Append a five-character base-58 checksum
        address += chopChecksumStandard(crypto.SHA256ReturnBase58(address));
        return address;
    }

    private static String chopChecksumStandard(String checksum) {
        if (checksum == null) {
            throw new IllegalArgumentException("getChecksumPortionFromAddress cannot be called with a null checksum!");
        }
        if (checksum.length() < ADDRESS_CHECKSUM_LENGTH) {
            throw new IllegalArgumentException("getChecksumPortionFromAddress cannot be called with an checksum " +
                    "(" + checksum + ") which is not at least " + ADDRESS_CHECKSUM_LENGTH + " characters long!");
        }
        return checksum.substring(0, ADDRESS_CHECKSUM_LENGTH + 1);
    }

    private static class StoredAddress {
        private final String address;
        private final byte[] publicKey;
        private final EncryptedInfo cipher;

        public StoredAddress(String address, byte[] publicKey, EncryptedInfo chiper) {
            this.address = address;
            this.publicKey = publicKey;
            this.cipher = chiper;
        }
    }

    private static class EncryptedInfo {
        private final byte[] cipherText;

        public EncryptedInfo(byte[] chiperText) {
            this.cipherText = chiperText;
        }
    }

    private static class StoredWallet {
        private final int version;
        private final int keyType;
        private final boolean locked;
        private final String defaultAddress;
        private final List<StoredAddress> addresses;

        public StoredWallet(int version, int keyType, boolean locked, String defaultAddress, List<StoredAddress> addresses) {
            this.version = version;
            this.keyType = keyType;
            this.locked = locked;
            this.defaultAddress = defaultAddress;
            this.addresses = addresses;
        }
    }

    private static class Base58 {
        private static final String BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
        private static final char[] ALPHABET = BASE58_ALPHABET.toCharArray();
        private static final int BASE_58 = ALPHABET.length;
        private static final int BASE_256 = 256;

        private static String encode(byte[] input) {
            if (input.length == 0) {
                // paying with the same coin
                return "";
            }

            // Make a copy of the input since we are going to modify it.
            input = copyOfRange(input, 0, input.length);

            // Count leading zeroes
            int zeroCount = 0;
            while (zeroCount < input.length && input[zeroCount] == 0) {
                ++zeroCount;
            }

            // The actual encoding
            byte[] temp = new byte[input.length * 2];
            int j = temp.length;

            int startAt = zeroCount;
            while (startAt < input.length) {
                byte mod = divmod58(input, startAt);
                if (input[startAt] == 0) {
                    ++startAt;
                }

                temp[--j] = (byte) ALPHABET[mod];
            }

            // Strip extra '1' if any
            while (j < temp.length && temp[j] == ALPHABET[0]) {
                ++j;
            }

            // Add as many leading '1' as there were leading zeros.
            while (--zeroCount >= 0) {
                temp[--j] = (byte) ALPHABET[0];
            }

            byte[] output = copyOfRange(temp, j, temp.length);
            return new String(output);
        }

        private static byte divmod58(byte[] number, int startAt) {
            int remainder = 0;
            for (int i = startAt; i < number.length; i++) {
                int digit256 = (int) number[i] & 0xFF;
                int temp = remainder * BASE_256 + digit256;

                number[i] = (byte) (temp / BASE_58);

                remainder = temp % BASE_58;
            }

            return (byte) remainder;
        }

        private static byte[] copyOfRange(byte[] source, int from, int to) {
            byte[] range = new byte[to - from];
            System.arraycopy(source, from, range, 0, range.length);
            return range;
        }
    }

    private static class Crypto {
        private MessageDigest _sha256;

        public Crypto() {
            try {
                _sha256 = MessageDigest.getInstance("SHA-256");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
        }

        private byte[] SHA256ReturnBytes(String input) {
            return SHA256ReturnBytes(input.getBytes(StandardCharsets.UTF_8));
        }

        private byte[] SHA256ReturnBytes(byte[] input) {
            return _sha256.digest(input);
        }

        private String SHA256ReturnBase58(byte[] input) {
            return bytesToBase58(SHA256ReturnBytes(input));
        }

        private String SHA256ReturnBase58(String input) {
            return bytesToBase58(SHA256ReturnBytes(input));
        }
    }

    private static String bytesToHex(byte[] bytes) {
        if (bytes == null) {
            throw new IllegalArgumentException("bytesToHex cannot be called with a null byte array!");
        }
        // Two hex characters always represent one byte
        char[] hex = new char[bytes.length << 1];
        for (int i = 0, j = 0; i < bytes.length; i++) {
            hex[j++] = HEX_ALPHABET_ARRAY[(0xF0 & bytes[i]) >>> 4];
            hex[j++] = HEX_ALPHABET_ARRAY[(0x0F & bytes[i])];
        }
        return new String(hex);
    }

    private static String bytesToBase58(byte[] bytes) {
        return Base58.encode(bytes);
    }

    private static class ByteArrayToBase64TypeAdapter implements JsonSerializer<byte[]>, JsonDeserializer<byte[]> {
        public byte[] deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException {
            return Base64.getDecoder().decode(json.getAsString());
        }

        public JsonElement serialize(byte[] src, Type typeOfSrc, JsonSerializationContext context) {
            return new JsonPrimitive(Base64.getEncoder().encodeToString(src));
        }
    }

    public static void main(String[] args) {
        final MakeAddress makeAddress = new MakeAddress();
        final KeyPair pair = makeAddress.generateKeyPair();
        final byte[] publicKey = pair.getPublic().getEncoded();
        final byte[] privateKey = pair.getPrivate().getEncoded();
        final String address = makeAddress.addressFromPublicKey(publicKey);

        final StoredAddress storedAddress = new StoredAddress(
                address,
                publicKey,
                new EncryptedInfo(privateKey)
        );
        final StoredWallet storedWallet = new StoredWallet(
                WALLET_VERSION,
                KEY_TYPE,
                false,
                address,
                Collections.singletonList(storedAddress)
        );

        final File walletFile = new File("./"+address+".dat");
        try {
            final Gson gson = new GsonBuilder().registerTypeHierarchyAdapter(
                    byte[].class,
                    new ByteArrayToBase64TypeAdapter()
            ).create();

            final BufferedWriter writer = new BufferedWriter(new FileWriter(walletFile, true));
            writer.append(gson.toJson(storedWallet));
            writer.close();
        } catch(Exception e) {
            e.printStackTrace();
        }

        // Private key dump - NodeCore format
        byte[] fullBytes = new byte[privateKey.length + publicKey.length + 1];
        fullBytes[0] = (byte) privateKey.length;
        System.arraycopy(privateKey, 0, fullBytes, 1, privateKey.length);
        System.arraycopy(publicKey, 0, fullBytes, 1 + privateKey.length, publicKey.length);
        System.out.println("Private Key (for NodeCore): " + bytesToHex(fullBytes));
        // Public key dump - raw format
        System.out.println("Private key: " + bytesToHex(privateKey));
        System.out.println("Public Key: " + bytesToHex(publicKey));
        // Others
        System.out.println("Address: " + address);
        System.out.println("Wallet File: " + walletFile.toPath());
        // Exit
        System.out.println("Finished! Press any key to exit...");
        new Scanner(System.in).nextLine();
    }
}

