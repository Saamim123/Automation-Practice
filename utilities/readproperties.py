
import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class Readconfig:

    @staticmethod
    def getAppUrl():
        url=config.get('common info', 'base url')
        return url

    @staticmethod
    def getuseremail():
        username=config.get('common info', 'email')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getname():
        name = config.get('common info', 'name')
        return name

    @staticmethod
    def getFnameinaddress():
        Fname = config.get('common info', 'Fname')
        return Fname

    @staticmethod
    def getLnameinaddress():
        Lname = config.get('common info', 'Lname')
        return Lname

    @staticmethod
    def getaddress():
        Add = config.get('common info', 'Address')
        return Add

    @staticmethod
    def getusername():
        usernamee =config.get('common info','username')
        return usernamee

    @staticmethod

    def getpwd():
        password = config.get('common info', 'password for login')
        return password


