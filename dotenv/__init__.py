# -*- coding: utf-8 -*-

__version__ = '0.0.2'

import re

class DotEnv:
    def __init__(self, path='.env'):
        self.path = path
        self.data = {}
        self.__read()

    ''' get key with default value '''
    def get(self, key, default=None):
        return self.data.get(key, default)

    ''' show if specific key exists '''
    def has(self, key):
        return key in self.data

    ''' provide all data in dicts '''
    def all(self):
        return self.data

    ''' dump all data to screen '''
    def dump(self):
        print(self.data)

    ''' read configuration file '''
    def __read(self):
        with open(self.path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                # ignore comment line and empty/bad line
                if line.startswith('#') or '=' not in line:
                    continue
                self.__read_line(line)

    ''' parse a line with .env standards '''
    def __read_line(self, line):
        result = re.search('(.+)=([A-Za-z0-9\'\"]+)', line)
        key = result.group(1)
        value = result.group(2).strip('\"').strip('\'')
        self.data[key] = value
