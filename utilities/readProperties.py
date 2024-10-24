import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        baseurl=config.get('common info','baseurl')
        return baseurl
    @staticmethod
    def getUserName():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
