#!/usr/bin/env python
import requests
import json

class nodecore_pop_api:

    def __init__(self, host, verbose=False):
        self.host = host

    def request(self, method, path, body):
        url = self.host + path

        s = requests.Session()
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

    def get_config(self):
        return json.dumps(self.request('GET', '/api/config', None), sort_keys=True, indent=4)

    def put_config(self, key, value):
        config_data = {
            "key": key,
            "value": value
        }
        return json.dumps(self.request('PUT', '/api/config', config_data), sort_keys=True, indent=4)

    def get_miner_properties(self):
        return json.dumps(self.request('GET', '/api/miner', None), sort_keys=True, indent=4)

    def get_operations(self):
        return json.dumps(self.request('GET', '/api/operations', None), sort_keys=True, indent=4)

    def get_operations_id(self, id):
        return json.dumps(self.request('GET', '/api/operations/' + id, None), sort_keys=True, indent=4)

    def get_lastbitcoinblock(self):
        return json.dumps(self.request('GET', '/api/lastbitcoinblock', None), sort_keys=True, indent=4)

    def quit(self):
        return json.dumps(self.request('POST', '/api/quit', None), sort_keys=True, indent=4)

    def mine_current_block(self):
        return json.dumps(self.request('POST', '/api/mine', '{}'), sort_keys=True, indent=4)

    def mine(self, block):
        block_data = {
            "block": block
        }
        return json.dumps(self.request('POST', '/api/mine', block_data), sort_keys=True, indent=4)
