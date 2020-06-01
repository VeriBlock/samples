#!/usr/bin/env python
import requests
import json


class NodeCoreApi:

    def __init__(self, host, rpc_password, verbose=False):
        self.host = host
        self.rpc_password = rpc_password

    def request(self, method, path, body):
        url = self.host + path

        headers = {
            'X-VBK-RPC-PASSWORD': self.rpc_password,
            'Content-Type': 'application/json'
        }

        s = requests.Session()
        s.headers = headers

        if body == '{}':
            response = s.request(method, url, data=body)
        elif body:
            body_json = json.dumps(body)
            response = s.request(method, url, data=body_json)
        else:
            response = s.request(method, url)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

# Thanks bitspill :)
    def do_request(self, method, params):
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        return self.request('POST', '/api', request)

    def addnode(self, ip, port):
        params = {
            "endpoint": [{
                "address": ip,
                "port": port
            }]
        }
        return self.do_request("addnode", params)

    def backupwallet(self, path):
        params = {
            "targetLocation": path
        }
        return self.do_request("backupwallet", params)

    def clearallowed(self):
        params = {}
        return self.do_request("clearallowed", params)

    def clearbanned(self):
        params = {}
        return self.do_request("clearbanned", params)

    def clearbannedminers(self):
        params = {}
        return self.do_request("clearbannedminers", params)

    def decryptwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.do_request("decryptwallet", params)

    def drainaddress(self, source, dest):
        params = {
            "sourceAddress": source,
            "destinationAddress": dest
        }
        return self.do_request("drainaddress", params)

    def dumpprivatekey(self, address):
        params = {
            "address": address
        }
        return self.do_request("dumpprivatekey", params)

    def encryptwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.do_request("encryptwallet", params)

    def generatemultisigaddress(self, addresses, threshold):
        params = {
            "sourceAddresses": addresses,
            "signatureThresholdM": threshold
        }
        return self.do_request("generatemultisigaddress", params)

    def getbalance(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.do_request("getbalance", params)

    def getbalanceunlockschedule(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.do_request("getbalanceunlockschedule", params)

    def getbitcoinblockindex(self, blockHeader, searchLength):
        params = {
            "blockHeader": blockHeader,
            "searchLength": searchLength
        }
        return self.do_request("getbitcoinblockindex", params)

    def getblockchains(self):
        params = {}
        return self.do_request("getblockchains", params)

    def getblocks(self, searchLength, filters):

        filterType = filters[0]
        filterValue = filters[1]

        params = {
            "searchLength": searchLength,
            "filters": [{
                filterType: filterValue
            }],
        }
        return self.do_request("getblocks", params)

    def getblocktemplate(self, mode, capabilities):
        params = {
            "mode": mode,
            "capabilities": capabilities
        }
        return self.do_request("getblocktemplate", params)

    def getblocktimes(self, historyLength):
        params = {
            "historyLength": historyLength
        }
        return self.do_request("getblocktimes", params)

    def getdiagnosticinfo(self):
        params = {}
        return self.do_request("getdiagnosticinfo", params)

    def getendorsementsofblock(self, filter):

        filterType = filter[0]
        filterValue = filter[1]

        params = {
            "filter": {
                filterType: filterValue,
            }
        }
        return self.do_request("getendorsementsofblock", params)

    def gethistory(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.do_request("gethistory", params)

    def getinfo(self):
        params = {}
        return self.do_request("getinfo", params)

    def getlastbitcoinblock(self):
        params = {}
        return self.do_request("getlastbitcoinblock", params)

    def getlastblock(self):
        params = {}
        return self.do_request("getlastblock", params)

    def getnewaddress(self, count):
        params = {
            "count": count
        }
        return self.do_request("getnewaddress", params)

    def getpeerinfo(self):
        params = {}
        return self.do_request("getpeerinfo", params)

    def getpendingtransactions(self):
        params = {}
        return self.do_request("getpendingtransactions", params)

    def getpoolstate(self):
        params = {}
        return self.do_request("getpoolstate", params)

    def getpop(self, blockNum):
        params = {
            "blockNum": blockNum
        }
        return self.do_request("getpop", params)

    def getpopendorsementsinfo(self, searchLength, addresses):
        params = {
            "searchLength": searchLength,
            "addresses": [{
                "standardAddress": addresses
            }]
        }
        return self.do_request("getpopendorsementsinfo", params)

    def getprotectedchildren(self, searchLength, veriblockBlockHash):
        params = {
            "searchLength": searchLength,
            "veriblockBlockHash": veriblockBlockHash
        }
        return self.do_request("getprotectedchildren", params)

    def getprotectingparents(self, searchLength, veriblockBlockHash):
        params = {
            "searchLength": searchLength,
            "veriblockBlockHash": veriblockBlockHash
        }
        return self.do_request("getprotectingparents", params)

    def getsignatureindex(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.do_request("getsignatureindex", params)

    def getstateinfo(self):
        params = {}
        return self.do_request("getstateinfo", params)

    def gettransactions(self, ids):
        params = {
            "searchLength": 0,
            "ids": [ ids ]

        }
        return self.do_request("gettransactions", params)

    def getveriblockpublications(self, keystone_hash, context_hash, btc_context_hash):
        params = {
            "keystoneHash": keystone_hash,
            "contextHash": context_hash,
            "btcContextHash": btc_context_hash
        }
        return self.do_request("getveriblockpublications", params)

    def getwallettransactions(self, request_type, transaction_type, page):

        page_num = page[0]
        page_results = page[1]

        params = {
            "requestType": request_type,
            "transactionType": transaction_type,
            "page": {
                "pageNumber": page_num,
                "resultsPerPage": page_results
            }
        }
        return self.do_request("getwallettransactions", params)

    def getwallettransactionsbyaddress(self, address, request_type, transaction_type, page):

        page_num = page[0]
        page_results = page[1]

        params = {
            "address": address,
            "requestType": request_type,
            "transactionType": transaction_type,
            "page": {
                "pageNumber": page_num,
                "resultsPerPage": page_results
            }
        }
        return self.do_request("getwallettransactions", params)

    def importprivatekey(self, private_key):
        params = {
            "privateKey": private_key
        }
        return self.do_request("importprivatekey", params)

    def importwallet(self, path, passphrase):
        params = {
            "sourceLocation": path,
            "passphrase": passphrase
        }
        return self.do_request("importwallet", params)

    def listallowed(self):
        params = {}
        return self.do_request("listallowed", params)

    def listbanned(self):
        params = {}
        return self.do_request("listbanned", params)

    def listbannedminers(self):
        params = {}
        return self.do_request("listbannedminers", params)

    def listblockssince(self, hash):
        params = {
            "hash": hash
        }
        return self.do_request("listblockssince", params)

    def lockwallet(self):
        params = {}
        return self.do_request("lockwallet", params)

    def makeunsignedmultisigtx(self, source_multisig_address, amounts, fee, signature_index_string):
        address = amounts[0]
        amount = amounts[1]
        params = {
            "sourceMultisigAddress": source_multisig_address,
            "amounts": [{
                "address": address,
                "amount": amount
            }],
            "fee": fee,
            "signatureIndexString": signature_index_string
        }
        return self.do_request("makeunsignedmultisigtx", params)

    def refreshwalletcache(self):
        params = {}
        return self.do_request("refreshwalletcache", params)

    def removenode(self, ip, port):
        params = {
            "endpoint": [{
                "address": ip,
                "port": port
            }]
        }
        return self.do_request("removenode", params)

    def restartpoolwebserver(self):
        params = {}
        return self.do_request("restartpoolwebserver", params)

    def sendaltchainendorsement(self, publication_data):
        params = {
            "publicationData": publication_data
        }
        return self.do_request("sendaltchainendorsement", params)

    def sendcoins(self, source_address, address, amount):
        params = {
            "sourceAddress": source_address,
            "amounts": [{
                "address": address,
                "amount": amount
            }]
        }
        return self.do_request("sendcoins", params)

    def setallowed(self, command, value):
        params = {
            "command": command,
            "value": value
        }
        return self.do_request("setallowed", params)

    def setban(self, command, value, reason, expiry_timestamp):
        params = {
            "command": command,
            "value": value,
            "reason": reason,
            "expiryTimestamp": expiry_timestamp
        }
        return self.do_request("setban", params)

    def setdefaultaddress(self, address):
        params = {
            "address": address
        }
        return self.do_request("setdefaultaddress", params)

    def settransactionfee(self, amount):
        params = {
            "amount": amount
        }
        return self.do_request("settransactionfee", params)

    def signmessage(self, address, message):
        params = {
            "address": address,
            "message": message
        }
        return self.do_request("signmessage", params)

    def startpool(self, type):
        params = {
            "type": type
        }
        return self.do_request("startpool", params)

    def startsolopool(self, address):
        params = {
            "address": address
        }
        return self.do_request("startsolopool", params)

    def stopnodecore(self):
        params = {}
        return self.do_request("stopnodecore", params)

    def stoppool(self):
        params = {}
        return self.do_request("stoppool", params)

    def submitblocks(self):
        pass

    def submitmultisigtx(self):
        pass

    def submitpop(self, endorsed_blockheader, bitcoin_transaction, bitcoin_merklepath_to_root, bitcoin_blockheader_of_proof, context_header, address):
        params = {
            "endorsedBlockHeader": endorsed_blockheader,
            "bitcoinTransaction": bitcoin_transaction,
            "bitcoinMerklePathToRoot": bitcoin_merklepath_to_root,
            "bitcoinBlockHeaderOfProof": bitcoin_blockheader_of_proof,
            "contextBitcoinBlockHeaders": [{
                "header": context_header
            }],
            "address": address
        }
        return self.do_request("submitpop", params)

    def submittransactions(self):
        pass

    def troubleshootpoptransactions(self, only_failures, search_length, addresses, transactions):
        params = {
            "onlyFailures": only_failures,
            "searchLength": search_length,
            "addresses": [{
                "addresses": addresses
            }],
            "transactions": [{
                "txids": transactions
            }]
        }
        return self.do_request("troubleshootpoptransactions", params)

    def unlockwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.do_request("unlockwallet", params)

    def validateaddress(self, address):
        params = {
            "address": address
        }
        return self.do_request("validateaddress", params)
