from datetime import datetime
import os
import json
import platform
from time import time


class Nodes:
    def __init__(self, directory: str):
        """enter the fill directory, enter the json data that you want in the file,
        and enter True or False if you want to add a time stamp of the creation
        date
        
        *IMPORTANT NOTE* 

        when entering a directory, make sure to always end it with a slash and not
        the name of the file"""

        

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
        try:
            os.system(f"rm {self.dir}.DS_Store")
        except Exception as e:
            pass

        self.json_data = json_data
        files_in_dir = os.listdir(self.dir)


        if timestamp:
            self.timestamp = datetime.now()
        else:
            self.timestamp = None
        
        print(os.listdir(self.dir))

        if len(files_in_dir) == 0:
            with open(f"{self.dir}head_file.json", 'w') as f:
                data = {
                    "timestamp": str(self.timestamp),
                    "next": f"{self.dir}{1}.json"
                }
                json.dump(data, f)
        
        elif len(files_in_dir) >= 0:
            with open(f"{self.dir}{len(os.listdir(self.dir))}.json", "w") as f:
                
                data = {
                    "timestamp": str(self.timestamp),
                    "next": f"{self.dir}{len(os.listdir(self.dir))}.json",
                    "data": self.json_data
                }
                json.dump(data, f)


    def deleteNodeObject(self):
        pass

    def findNodeObject(self):
        pass
      
            

new = Nodes(directory = "/Users/winstonwalter/Desktop/demo_file/") 

new.makeNodeObject(json_data={"hello": "world"}, timestamp=True)