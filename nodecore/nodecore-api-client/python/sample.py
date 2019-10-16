#!/usr/bin/env python

import nodecore_api
import json

def pretty(self):
    return json.dumps(self, sort_keys=True, indent=4)

def convertAtomic(self):
    return int(self)/100000000

host = 'http://127.0.0.1:10600'

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
#addresses = ['address_one']
#addresses = ['address_one', 'address_two']
#balance = api.getbalance(addresses)
#print(pretty(balance))

# Get Balance Unlock Schedule

# Get Bitcoin Block Index

# Get Blockchains
#blockchains = api.getblockchains()
#print(pretty(blockchains))

# Get Blocks
#blockHash = '000000181E25345C75A5176696FF5E989F1E86786A51EC42'
#filters = ['number','552214']
#filters = ['hash', blockHash]
#blocks = api.getblocks(1, filters)
#print(pretty(blocks))

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

# Get Last Block

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
poolstate = api.getpoolstate()
print(pretty(poolstate))

# Get PoP

# Get PoP Endorsements Info

# Get Protected Children

# Get Protecting Parents

# Get Signature Index

# Get State Info
#stateinfo = api.getstateinfo()
#print(pretty(stateinfo))

# Get Transactions

# Get VeriBlock Publications

# Get Wallet Transactions

# Import Private Key

# Import Wallet

# List Allowed

# List Banned

# List Banned Miners

# List Blocks Since

# Lock Wallet

# Make Unsigned Multisig Tx

# Refresh Wallet Cache

# Remove Node

# Restart Pool Webserver

# Send Alt Chain Endorsement

# Send Coins

# Set Allowed

# Set Banned

# Set Default Address

#defaultaddress = api.setdefaultaddress('V3TCJ69TfVVELGJi9H5c2m3smAiWeP')
#print(pretty(defaultaddress))

# Set Transaction Fee

# Sign Message

# Start Pool

# Start Solo Pool

# Stop NodeCore

# Stop Pool

# Submit PoP

# Troubleshoot PoP Transactions

# Unlock Wallet

# Validate Address




