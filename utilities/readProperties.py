#reads the common data from the config.ini

import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login info', 'userid')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'pass')
        return password


