#!/usr/bin/env python

import nodecore_api
import json

def pretty(self):
    return json.dumps(self, sort_keys=True, indent=4)

host = 'http://127.0.0.1:10600'

rpc_password = ''

# Create api object
api = nodecore_api.nodecore_api(host, rpc_password, True)

# Get Info
info = api.getinfo()
print(pretty(info))

# Add Peer/node
#addnode = api.addnode('192.168.0.63', 7500)
#print(pretty(addnode))

# Get new address
#newaddress = api.getnewaddress(1)
#print(pretty(newaddress))

# Get Balance of one address or multiple.
addresses = ['address_one']
#addresses = ['address_one', 'address_two']
balance = api.getbalance(addresses)
print(pretty(balance))

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

# Get State Info
stateinfo = api.getstateinfo()
print(pretty(stateinfo))

# Get Blockchains
blockchains = api.getblockchains()
print(pretty(blockchains))

# Get Block Times
blocktimes = api.getblocktimes(5)
print(pretty(blocktimes))

# Get Diagnostic Info
diaginfo = api.getdiagnosticinfo()
print(pretty(diaginfo))

# Get Endorsements of Block
#blockHash = '000000000000A0D547D360D849E0DCFC6F7B4543274AFF25'
#filter = ['hash', blockHash]
#filter = ['number', '552214']
#filter = ['index', '0']
#endorsements = api.getendorsementsofblock(filter)
#print(pretty(endorsements))

# Get Blocks
blockHash = '000000000000A0D547D360D849E0DCFC6F7B4543274AFF25'
#filters = ['number','552214']
filters = ['hash', blockHash]
blocks = api.getblocks(1, filters)
print(pretty(blocks))
