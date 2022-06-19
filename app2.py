from datetime import datetime
import os
import json

class Nodes:
    def __init__(self, json_data, timestamp: bool, directory: str):
        os.chdir("/")
        print(os.curdir)
        """enter the fill directory, enter the json data that you want in the file,
        and enter True or False if you want to add a time stamp of the creation
        date"""
        
        self.json_data = json_data
        self.directory = os.chdir(directory)
        if timestamp:
            self.timestamp = datetime.now()
        else:
            self.timestam = None

        #checking what id to make the next file

        print(os.listdir("."))      

Nodes(json_data = {}, directory = "/Users/winstonwalter/Desktop/file-node-chain/app2.py", timestamp=True) 
