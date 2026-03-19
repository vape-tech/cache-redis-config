# utils.py

import logging
import redis
import os

class Config:
    def __init__(self, config):
        self.config = config

        self.REDIS_HOST = self.config.get('REDIS_HOST', 'localhost')
        self.REDIS_PORT = self.config.getint('REDIS_PORT', 6379)
        self.REDIS_PASSWORD = self.config.get('REDIS_PASSWORD')

        self.REDIS_DB = self.config.getint('REDIS_DB', 0)
        self.REDIS_MAX_CONNECTIONS = self.config.getint('REDIS_MAX_CONNECTIONS', 10)
        self.REDIS_TIMEOUT = self.config.getint('REDIS_TIMEOUT', 10)

    def get_redis_connection(self):
        return redis.Redis(
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            password=self.REDIS_PASSWORD,
            db=self.REDIS_DB,
            max_connections=self.REDIS_MAX_CONNECTIONS,
            timeout=self.REDIS_TIMEOUT,
        )

class Logger:
    def __init__(self, config):
        self.config = config
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger()

    def get_logger(self, name):
        return logging.getLogger(name)

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}
        self.parse_config()

    def parse_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file {self.config_file} does not exist")

        with open(self.config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split('=')
                self.config[key.strip()] = value.strip()

    def get(self, key, default=None):
        return self.config.get(key, default)

    def getint(self, key, default=None):
        return int(self.get(key, default))

    def getboolean(self, key, default=None):
        return self.get(key, default).lower() == 'true'