from configparser import ConfigParser
import os


class Config:
    def __init__(self):
        self.file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config.ini"
        self.config = ConfigParser()
        self.config.read(self.file)
        if "DDNS" not in self.config.sections():
            self.config["DDNS"] = {
                "access_key_id": "",
                "access_key_secret": "",
                "domain_name": "example.com",
                "rrkey_word": "www",
                "rtype": "AAAA",
                "interval": 5
            }
            with open(self.file, 'w') as configfile:
                self.config.write(configfile)

    def get_ddns_config(self):
        return self.config["DDNS"]
