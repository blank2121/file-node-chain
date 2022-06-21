from datetime import datetime
import os
import json
import platform
from time import time


class Nodes:
    def __init__(self, directory: str):
        """enter the fill directory, enter the json data that you want in the file,
        and enter True or False if you want to add a time stamp of the creation
        date"""

        

        self.dir = directory

        self.WHICH_OS = platform.platform()

        if "macos" in self.WHICH_OS.lower():
            self.mac_process()

            #check what id to make the next file

    #file system different between windows and mac so this is jsut for mac os    
    def mac_process(self):

            #end goal is to get the chdir to be the disk aka /
            INITIAL_CWD = os.getcwd()
            for file in range(len(INITIAL_CWD)):
                if INITIAL_CWD[file] == "/":
                    os.chdir("../")

    
    def makeNodeObject(self, json_data, timestamp: bool):
        self.json_data = json_data

        if timestamp:
            self.timestamp = datetime.now()
        else:
            self.timestamp = None
        
        print(os.listdir(self.directory))


    def deleteNodeObject(self):
        pass

    def findNodeObject(self):
        pass
      
            

new = Nodes(directory = "/Users/winstonwalter/Desktop/file-node-chain/app2.py") 

new.makeNodeObject(json_data={}, timestamp=True)