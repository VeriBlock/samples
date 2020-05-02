#!/usr/bin/env python3

import nodecore_pop_api
import json
import logging

# Uncomment these for debug logging of requests
#try:
#    import http.client as http_client
#except ImportError:
#    # Python 2
#    import httplib as http_client
#http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

host = 'http://127.0.0.1:8080'

# Create api object
api = nodecore_pop_api.nodecore_pop_api(host, True)

# Get current config
config = api.get_config()
print("GET /api/config")
print(pretty(config))

# Get miner info
miner_properties = api.get_miner_properties()
print("GET /api/miner")
print(pretty(miner_properties))

# Get operations
operations = api.get_operations()
print("GET /api/operations")
print(pretty(operations))

# Get last bitcoin block
lastbitcoinblock = api.get_lastbitcoinblock()
print("GET /api/lastbitcoinblock")
print(pretty(lastbitcoinblock))

# Quit NodeCore-PoP
# POST /api/quit
#quit = api.quit()

# Mine specific block number
# POST /api/mine
#mine = api.mine(413381)
#print("POST /api/mine")
#print(pretty(mine))

# Mine current block
#mine = api.mine_current_block()
#print("POST /api/mine")
#print(pretty(mine))

# Change config information example
#config = api.put_config('auto.mine.round1', 'true')
#print("PUT /api/config")
#print(pretty(config))
