#!/usr/bin/env python

import nodecore_api
import json

def pretty(self):
    return json.dumps(self, sort_keys=True, indent=4)

def convertAtomic(self):
    return int(self)/100000000

host = 'http://192.168.0.62:10600'

rpc_password = ''

# Create api object
api = nodecore_api.nodecore_api(host, rpc_password, True)

# Add Peer/node
#addnode = api.addnode('192.168.0.63', 7500)
#print(pretty(addnode))

# Backup wallet to file path.
#path = '/root/'
#backupwallet = api.backupwallet(path)
#print(pretty(backupwallet))

# Clear Allowed
#clearallowed = api.clearallowed()
#print(pretty(clearallowed))

# Clear Banned
#clearbanned = api.clearbanned()
#print(pretty(clearbanned))

# Clear Banned Miners
#clearbannedminers = api.clearbannedminers()
#print(pretty(clearbannedminers))

# Decrypt Wallet
#decrypt = api.decryptwallet('passphrase')
#print(pretty(decrypt))

# Drain Address
#drainAddress = api.drainaddress('VBasFp1K8LvMWypcC6jFff3TW2JyTn', 'V3TCJ69TfVVELGJi9H5c2m3smAiWeP')
#print(pretty(drainAddress))

# Dump Private Key
#privkey = api.dumpprivatekey('V3TCJ69TfVVELGJi9H5c2m3smAiWeP')
#print(pretty(privkey))

# Encrypt Wallet
#encrypt = api.encryptwallet('passphrase')
#print(pretty(encrypt))

# Generate Multisig Address

# Get Balance of one address or multiple.
#addresses = ['V3TCJ69TfVVELGJi9H5c2m3smAiWeP']
#addresses = ['address_one', 'address_two']
#balance = api.getbalance(addresses)
#print(pretty(balance))

# Get Balance Unlock Schedule
#addresses = ['V3TCJ69TfVVELGJi9H5c2m3smAiWeP']
#addresses = ['address_one', 'address_two']
#unlockschedule = api.getbalanceunlockschedule(addresses)
#print(pretty(unlockschedule))

# Get Bitcoin Block Index
#searchLength = 0
#blockHeader = '00000020527cc2b1b37f65a7d56b632fe96653ea54493ce51a159cce6d0300000000000016d66b45a248b6c5c32d2b9b5ba0d8186c5e136caee978ceb1bb958d6cda5c14d1d5ee5decae031a782e3d19'
#btcblockindex = api.getbitcoinblockindex(blockHeader, searchLength)
#print(pretty(btcblockindex))

# Get Blockchains
#blockchains = api.getblockchains()
#print(pretty(blockchains))

# Get Blocks
#blockHash = '000000181E25345C75A5176696FF5E989F1E86786A51EC42'
#filters = ['index','80000']
#filters = ['hash', blockHash]
#blocks = api.getblocks(1, filters)
#print(pretty(blocks))
#print(blocks['header'])
# Get Block Template

# Get Block Times
#blocktimes = api.getblocktimes(5)
#print(pretty(blocktimes))

# Get Diagnostic Info
#diaginfo = api.getdiagnosticinfo()
#print(pretty(diaginfo))

# Get Endorsements of Block
#blockHash = '000000181E25345C75A5176696FF5E989F1E86786A51EC42'
#filter = ['hash', blockHash]
#filter = ['number', '552214']
#filter = ['index', '0']
#endorsements = api.getendorsementsofblock(filter)
#print(pretty(endorsements))

# Get History
#addresses = ['V3TCJ69TfVVELGJi9H5c2m3smAiWeP']
#history = api.gethistory(addresses)
#print(pretty(history))

# Get Info
#info = api.getinfo()
#print(pretty(info))
#print(info['result']['defaultAddress']['address'] + " Balance: " + str(convertAtomic(info['result']['defaultAddress']['unlockedAmount'])) + " VBK")

# Get Last Bitcoin Block
#lastbtcblock = api.getlastbitcoinblock()
#print(pretty(lastbtcblock))

# Get Last Block
#lastblock = api.getlastblock()
#print(pretty(lastblock))

# Get new address
#newaddress = api.getnewaddress(1)
#print(pretty(newaddress))

# Get Peer Info
#peers = api.getpeerinfo()
#print(pretty(peers))

# Get Pending Transactions
#pendingtxs = api.getpendingtransactions()
#print(pretty(pendingtxs))

# Get Pool State
#poolstate = api.getpoolstate()
#print(pretty(poolstate))

# Get PoP
#blockNum = 100000
#getpop = api.getpop(blockNum)
#print(pretty(getpop))

# Get PoP Endorsements Info
#addresses = ['V3TCJ69TfVVELGJi9H5c2m3smAiWeP']
#searchLength = 0
#getpopendorsements = api.getpopendorsementsinfo(searchLength, addresses)
#print(pretty(getpopendorsements))

# Get Protected Children
#searchLength = 0
#blockHash = '0000001755917FDB90335FBEBED76D4E6C007494173B0E27'
#protectedchildren = api.getprotectedchildren(searchLength, blockHash)
#print(pretty(protectedchildren))

# Get Protecting Parents
#searchLength = 0
#blockHash = '0000001755917FDB90335FBEBED76D4E6C007494173B0E27'
#protectingparents = api.getprotectingparents(searchLength, blockHash)
#print(pretty(protectingparents))

# Get Signature Index
#addresses = ['V3TCJ69TfVVELGJi9H5c2m3smAiWeP']
#sigindex = api.getsignatureindex(addresses)
#print(pretty(sigindex))

# Get State Info
#stateinfo = api.getstateinfo()
#print(pretty(stateinfo))

# Get Transactions
#ids = 'D634C6E7D7E19F083068DAB4ED9499EE312EF4ADACCCD74B496F4DE22ED527DC'
#transactions = api.gettransactions(ids)
#print(pretty(transactions))

#TODO: What is context hash?
# Get VeriBlock Publications
#keystoneHash = ''
#contextHash = ''
#vtbpublications = api.getveriblockpublications(keystoneHash, contextHash)
#print(pretty(vtbpublications))

# Get Wallet Transactions
# LIST = 0, QUERY = 1
#requestType = 0
# NOT_SET = 0, POW_COINBASE = 1, POP_COINBASE = 2, BOTH_COINBASE = 3, SENT = 4, RECEIVED = 5, SENT_AND_RECEIVED = 6, POP = 7
#transactionType = 6
# pageNumber=1, resultsPerPage=5
#page = [1,5]
#transactions = api.getwallettransactions(requestType, transactionType, page)
#print(pretty(transactions))

# Get Wallet Transactions by Address
#address = 'V7TMHDQC8myywuGbQs5ADTrk14fajz'
# LIST = 0, QUERY = 1
#requestType = 1
# NOT_SET = 0, POW_COINBASE = 1, POP_COINBASE = 2, BOTH_COINBASE = 3, SENT = 4, RECEIVED = 5, SENT_AND_RECEIVED = 6, POP = 7
#transactionType = 6
# pageNumber=1, resultsPerPage=5
#page = [1,5]
#transactions = api.getwallettransactionsbyaddress(address, requestType, transactionType, page)
#print(pretty(transactions))

#TODO: Import Private Key

#TODO: Import Wallet

# List Allowed/Whitelist
#allowed = api.listallowed()
#print(pretty(allowed))

# List Banned
#bannedpeers = api.listbanned()
#print(pretty(bannedpeers))

# List Banned Miners
#bannedminers = api.listbannedminers()
#print(pretty(bannedminers))

# List Blocks Since
#blockHash = '00000010AC62E9738BFA09BEF3DA7F435D20F11EE64A5397'
#listblocks = api.listblockssince(blockHash)
#print(pretty(listblocks))

# Lock Wallet
#lock = api.lockwallet()
#print(pretty(lock))

#TODO: Make Unsigned Multisig Tx

# Refresh Wallet Cache
#refresh = api.refreshwalletcache()
#print(pretty(refresh))

# Remove Peer/Node
#removenode = api.removenode('192.168.0.63', 7500)
#print(pretty(removenode))

# Restart Pool Webserver
#restart = api.restartpoolwebserver()
#print(pretty(restart))

#TODO:  Send Alt Chain Endorsement

# Send Coins
#source = 'V3TCJ69TfVVELGJi9H5c2m3smAiWeP'
#dest = 'V7TMHDQC8myywuGbQs5ADTrk14fajz'
# Specify amount in VBK
#amount = 100
#amount = amount * 100000000
#send = api.sendcoins(source, dest, amount)
#print(pretty(send))

#TODO:  Set Allowed

#TODO:  Set Banned

# Set Default Address
#defaultaddress = api.setdefaultaddress('V3TCJ69TfVVELGJi9H5c2m3smAiWeP')
#print(pretty(defaultaddress))

# Set Transaction Fee
#amount = 00000100
#txfee = api.settransactionfee(amount)
#print(pretty(txfee))

# Sign Message
#address = 'V3TCJ69TfVVELGJi9H5c2m3smAiWeP'
#message = 'Overcooked Panda'
#message = message.encode("hex")
#signedmsg = api.signmessage(address, message)
#print(pretty(signedmsg))

# Start Pool
#poolType = 'CPU'
#pool = api.startpool(poolType)
#print(pretty(pool))

# Start Solo Pool
#address = 'V3TCJ69TfVVELGJi9H5c2m3smAiWeP'
#pool = api.startsolopool(address)
#print(pretty(pool))

# Stop NodeCore
#stop = api.stopnodecore()
#print(pretty(stop))

# Stop Pool
#pool = api.stoppool()
#print(pretty(pool))

#TODO: Submit PoP

#TODO: Troubleshoot PoP Transactions

# Unlock Wallet
#passphrase = 'password'
#unlock = api.unlockwallet(passphrase)
#print(pretty(unlock))

# Validate Address
#address = 'V3TCJ69TfVVELGJi9H5c2m3smAiWeP'
#validateaddress = api.validateaddress(address)
#print(pretty(validateaddress))
