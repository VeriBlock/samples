#!/usr/bin/env python
import requests
import json

class nodecore_pop_api:

    def __init__(self, host, verbose=False):
        self.host = host

    def request(self, method, path, body):
        url = self.host + path

        s = requests.Session()

        headers = {"Content-Type": "application/json"}

        if body == '{}':
            response = s.request(method, url, data=body, headers=headers)
        elif body:
            body_json = json.dumps(body)
            response = s.request(method, url, data=body_json, headers=headers)
        else:
            response = s.request(method, url, headers=headers)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_config(self):
        return self.request('GET', '/api/config', None)

    def put_config(self, key, value):
        config_data = {
            "key": key,
            "value": value
        }
        return self.request('PUT', '/api/config', config_data)

    def get_miner_properties(self):
        return self.request('GET', '/api/miner', None)

    def get_operations(self):
        return self.request('GET', '/api/operations', None)

    def get_operations_id(self, id):
        return self.request('GET', '/api/operations/' + id, None)

    def get_lastbitcoinblock(self):
        return self.request('GET', '/api/lastbitcoinblock', None)

    def quit(self):
        return self.request('POST', '/api/quit', None)

    def mine_current_block(self):
        return self.request('POST', '/api/mine', '{}')

    def mine(self, block):
        block_data = {
            "block": block
        }
        return self.request('POST', '/api/mine', block_data)
