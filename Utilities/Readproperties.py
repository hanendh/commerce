#Read data  from config file
import configparser

# define obj from class Rawconfigparser

config = configparser.RawConfigParser()

config.read("C:\projet\commerce\Configurations\config.ini") # read the config file info

# create class

class Config:

    # function to get commen data
    @staticmethod # call the method by class

    def GetUrl():
        BaseUrl = config.get('common info', 'URL')
        return BaseUrl

    @staticmethod  # call the method by class
    def GetEmail():
        username = config.get('common info', 'email')
        return username

    @staticmethod  # call the method by class

    def GetPassword():
        password = config.get('common info', 'password')
        return password