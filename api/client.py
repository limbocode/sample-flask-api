import requests
import json
import os
import re

class Client:

    def __init__(self, host='localhost', port='5000'):
        self.host = host
        self.port = port
        if 'local' in host:
            self.host = '127.0.0.1'
        self.base_url = 'http://' + self.host + ':' + self.port
        self.json_pattern = re.compile(r'.*\.jsonl?$')

    def get_score(self, pk):
        url = self.base_url + '/get/' + str(pk)
        response = requests.get(url=url)
        # response.raise_for_status()
        
        if response.status_code != 200:
            return None
            
        score = int(response.json()['score'])

        return score

    def update_data(self, dir):
        url = self.base_url + '/update'
        lines = self._get_lines(dir)
        for line in lines:
            self._update_line(url, line)

        return None

    def _get_lines(self, dir):
        filenames = [dir + '/' + s for s in os.listdir(dir) if self.json_pattern.match(s)]

        if filenames == []:
            raise Exception('Directory is empty.')

        lines = []
        for filename in filenames:
            with open(filename, 'r') as f:
                lines += [line.strip() for line in f.readlines()]
        
        return lines
        
    def _update_line(self, url, line):
        response = requests.post(url=url, json=json.loads(line))
        response.raise_for_status()
        
        return None