from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("configurations/config.ini")#reading data from config.ini file
    return config.get(category,key)

list =["mnm","Msnn"]
print(max(list))


