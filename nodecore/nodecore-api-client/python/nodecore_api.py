#!/usr/bin/env python
import requests
import json
import logging
import httplib

# Debug logging
httplib.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
req_log = logging.getLogger('requests.packages.urllib3')
req_log.setLevel(logging.DEBUG)
req_log.propagate = True

class nodecore_api:

    def __init__(self, host, rpc_password, verbose=False):
        self.host = host
        self.rpc_password = rpc_password

    def request(self, method, path, body):
        url = self.host + path

        headers = {
            'X-VBK-RPC-PASSWORD': self.rpc_password,
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

## Thanks bitspill :)
    def doRequest(self, method, params):
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
        return self.doRequest("addnode", params)

    def backupwallet(self, path):
        params = {
            "targetLocation": path
        }
        return self.doRequest("backupwallet", params)

    def clearallowed(self):
        params = {}
        return self.doRequest("clearallowed", params)

    def clearbanned(self):
        params = {}
        return self.doRequest("clearbanned", params)

    def clearbannedminers(self):
        params = {}
        return self.doRequest("clearbannedminers", params)

    def decryptwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.doRequest("decryptwallet", params)

    def drainaddress(self, source, dest):
        params = {
            "sourceAddress": source,
            "destinationAddress": dest
        }
        return self.doRequest("drainaddress", params)

    def dumpprivatekey(self, address):
        params = {
            "address": address
        }
        return self.doRequest("drainaddress", params)

    def encryptwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.doRequest("encryptwallet", params)

    def generatemultisigaddress(self, addresses, threshold):
        params = {
            "sourceAddresses": addresses,
            "signatureThresholdM": threshold
        }
        return self.doRequest("generatemultisigaddress", params)

    def getbalance(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.doRequest("getbalance", params)

    def getbalanceunlockschedule(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.doRequest("getbalanceunlockschedule", params)

    def getbitcoinblockindex(self, blockHeader, searchLength):
        params = {
            "blockHeader": blockHeader,
            "searchLength": searchLength
        }
        return self.doRequest("getbitcoinblockindex", params)

    def getblockchains(self):
        params = {}
        return self.doRequest("getblockchains", params)

    def getblocks(self, searchLength, filters):

        hash = filters[0]
        index = filters[1]
        number = filters[2]

        params = {
            "searchLength": searchLength,
            "filters": [{
                "hash": hash,
                "index": index,
                "number": number
            }],
        }
        return self.doRequest("getblocks", params)

    def getblocktemplate(self, mode, capabilities):
        params = {
            "mode": mode,
            "capabilities": capabilities
        }
        return self.doRequest("getblocktemplate", params)

    def getblocktimes(self, historyLength):
        params = {
            "historyLength": historyLength
        }
        return self.doRequest("getblocktimes", params)

    def getdiagnosticinfo(self):
        params = {}
        return self.doRequest("getdiagnosticinfo", params)

    def getendorsementsofblock(self, filter):

        filterType = filter[0]
        filterValue = filter[1]

        params = {
            "filter": {
                filterType: filterValue,
            }
        }
        return self.doRequest("getendorsementsofblock", params)

    def gethistory(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.doRequest("gethistory", params)

    def getinfo(self):
        params = {}
        return self.doRequest("getinfo", params)

    def getlastbitcoinblock(self):
        params = {}
        return self.doRequest("getlastbitcoinblock", params)

    def getlastblock(self):
        params = {}
        return self.doRequest("getlastblock", params)

    def getnewaddress(self, count):
        params = {
            "count": count
        }
        return self.doRequest("getnewaddress", params)

    def getpeerinfo(self):
        params = {}
        return self.doRequest("getpeerinfo", params)

    def getpendingtransactions(self):
        params = {}
        return self.doRequest("getpendingtransactions", params)

    def getpoolstate(self):
        params = {}
        return self.doRequest("getpoolstate", params)

    def getpop(self, blockNum):
        params = {
            "blockNum": blockNum
        }
        return self.doRequest("getpop", params)

    def getpopendorsementsinfo(self, searchLength, addresses):
        params = {
            "searchLength": searchLength,
            "addresses": [{
                "standardAddress": addresses
            }]
        }
        return self.doRequest("getpopendorsementsinfo", params)

    def getprotectedchildren(self, searchLength, veriblockBlockHash):
        params = {
            "searchLength": searchLength,
            "veriblockBlockHash": veriblockBlockHash
        }
        return self.doRequest("getprotectedchildren", params)

    def getprotectingparents(self, searchLength, veriblockBlockHash):
        params = {
            "searchLength": searchLength,
            "veriblockBlockHash": veriblockBlockHash
        }
        return self.doRequest("getprotectingparents", params)

    def getsignatureindex(self, addresses):
        params = {
            "addresses": addresses
        }
        return self.doRequest("getsignatureindex", params)

    def getstateinfo(self):
        params = {}
        return self.doRequest("getstateinfo", params)

    def gettransactions(self, searchLength, ids):
        params = {
            "searchLength": searchLength,
            "ids": ids
        }
        return self.doRequest("gettransaction", params)

    def getveriblockpublications(self, keystoneHash, contextHash):
        params = {
            "keystoneHash": keystoneHash,
            "contextHash": contextHash
        }
        return self.doRequest("getveriblockpublications", params)

    def getwallettransactions(self, requestType, address, transactionType, status, amountFilter, timestampFilter, page):

        amountFilterOperator = amountFilter[0]
        amountFilterValue = amountFilter[1]
        amountFilterSecondaryValue = amountFilter[2]

        timestampFilterOperator = timestampFilter[0]
        timestampFilterValue = timestampFilter[1]
        timestampFilterSecondaryValue = timestampFilter[2]

        pageNum = page[0]
        pageResults = page[1]

        params = {
            "requestType": requestType,
            "address": address,
            "transactionType": transactionType,
            "status": status,
            "amountFilter": [{
                "operator": amountFilterOperator,
                "value": amountFilterValue,
                "secondaryValue": amountFilterSecondaryValue
            }],
            "timestampFilter": [{
                "operator": timestampFilterOperator,
                "value": timestampFilterValue,
                "secondaryValue": timestampFilterSecondaryValue
            }],
            "page": [{
                "pageNumber": pageNum,
                "resultsPerPage": pageResults
            }]
        }
        return self.doRequest("getwallettransactions", params)

    def importprivatekey(self, privateKey):
        params = {
            "privateKey": privateKey
        }
        return self.doRequest("importprivatekey", params)

    def importwallet(self, path, passphrase):
        params = {
            "sourceLocation": path,
            "passphrase": passphrase
        }
        return self.doRequest("importwallet", params)

    def listallowed(self):
        params = {}
        return self.doRequest("listallowed", params)

    def listbanned(self):
        params = {}
        return self.doRequest("listbanned", params)

    def listbannedminers(self):
        params = {}
        return self.doRequest("listbannedminers", params)

    def listblockssince(self, hash):
        params = {
            "hash": hash
        }
        return self.doRequest("listblockssince", params)

    def lockwallet(self):
        params = {}
        return self.doRequest("lockwallet", params)

    def makeunsignedmultisigtx(self, sourceMultisigAddress, amounts, fee, signatureIndexString):
        address = amounts[0]
        amount = amounts[1]
        params = {
            "sourceMultisigAddress": sourceMultisigAddress,
            "amounts": [{
                "address": address,
                "amount": amount
            }],
            "fee": fee,
            "signatureIndexString": signatureIndexString
        }
        return self.doRequest("makeunsignedmultisigtx", params)

    def refreshwalletcache(self):
        params = {}
        return self.doRequest("refreshwalletcache", params)

    def removenode(self, ip, port):
        params = {
            "endpoint": [{
                "address": ip,
                "port": port
            }]
        }
        return self.doRequest("removenode", params)

    def restartpoolwebserver(self):
        params = {}
        return self.doRequest("restartpoolwebserver", params)

    def sendaltchainendorsement(self, publicationData):
        params = {
            "publicationData": publicationData
        }
        return self.doRequest("sendaltchainendorsement", params)

    def sendcoins(self, sourceAddress, address, amount):
        params = {
            "sourceAddress": sourceAddress,
            "amounts": [{
                "address": address,
                "amount": amount
            }]
        }
        return self.doRequest("sendcoins", params)

    def setallowed(self, command, value):
        params = {
            "command": command,
            "value": value
        }
        return self.doRequest("setallowed", params)

    def setban(self, command, value, reason, expiryTimestamp):
        params = {
            "command": command,
            "value": value,
            "reason": reason,
            "expiryTimestamp": expiryTimestamp
        }
        return self.doRequest("setban", params)

    def setdefaultaddress(self, address):
        params = {
            "address": address
        }
        return self.doRequest("setdefaultaddress", params)

    def settransactionfee(self, amount):
        params = {
            "amount": amount
        }
        return self.doRequest("settransactionfee", params)

    def signmessage(self, address, message):
        params = {
            "address": address,
            "message": message
        }
        return self.doRequest("signmessage", params)

    def startpool(self, type):
        params = {
            "type": type
        }
        return self.doRequest("startpool", params)

    def startsolopool(self, address):
        params = {
            "address": address
        }
        return self.doRequest("startsolopool", params)

    def stopnodecore(self):
        params = {}
        return self.doRequest("stopnodecore", params)

    def stoppool(self):
        params = {}
        return self.doRequest("stopool", params)

    def submitblocks(self):
        pass

    def submitmultisigtx(self):
        pass

    def submitpop(self, endorsedBlockHeader, bitcoinTransaction, bitcoinMerklePathToRoot, bitcoinBlockHeaderOfProof, contextHeader, address):
        params = {
            "endorsedBlockHeader": endorsedBlockHeader,
            "bitcoinTransaction": bitcoinTransaction,
            "bitcoinMerklePathToRoot": bitcoinMerklePathToRoot,
            "bitcoinBlockHeaderOfProof": bitcoinBlockHeaderOfProof,
            "contextBitcoinBlockHeaders": [{
                "header": contextHeader
            }],
            "address": address
        }
        return self.doRequest("submitpop", params)

    def submittransactions(self):
        pass

    def troubleshootpoptransactions(self, onlyFailures, searchLength, addresses, transactions):
        params = {
            "onlyFailures": onlyFailures,
            "searchLength": searchLength,
            "addresses": [{
                "addresses": addresses
            }],
            "transactions": [{
                "txids": transactions
            }]
        }
        return self.doRequest("troubleshootpoptransactions", params)

    def unlockwallet(self, passphrase):
        params = {
            "passphrase": passphrase
        }
        return self.doRequest("unlockwallet", params)

    def validateaddress(self, address):
        params = {
            "address": address
        }
        return self.doRequest("validateaddress", params)
