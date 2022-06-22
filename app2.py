from cmath import e
from datetime import datetime
import os
import json
import platform
from time import time
import ast


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


        if timestamp:
            self.timestamp = datetime.now()
        else:
            self.timestamp = None
        
        print(os.listdir(self.dir))

    
        
        
        with open(f"{self.dir}{len(os.listdir(self.dir))+1}.json", "w") as f:
                
            data = {
                "timestamp": str(self.timestamp),
                "next": f"{self.dir}{len(os.listdir(self.dir))+1}.json",
                "data": self.json_data
            }
            json.dump(data, f)


    def deleteNodeObject(self):
        pass

    def findNodeObject(self, search_query: dict, method: str):
        """the current methods are:
        
        "data match" and "contains"

        for data match, enter the exact json data that needs to be found

        for contains, enter the json data that you want i.e. in the example below:

            {"id": 140,
            "name": Ezra,
            "and": "so on"}

        to find "id", enter in: {"id": 140} to find the file with that id
        """
        if method == "data match":
            total_files = []
            for files in os.listdir(self.dir):
                with open(f"{self.dir}{files}", "r") as f:
                    data = json.load(f)
                    if data["data"] == search_query:
                        total_files.append(files)
            return total_files
        elif method == "contains":
            total_files = []

            str_list = str(str(search_query.keys())[10:-1])
            key_list = [i for i in ast.literal_eval(str_list)]
            val_list = list(search_query.values())

            for files in os.listdir(self.dir):
                with open(f"{self.dir}{files}", "r") as f:
                    data = json.load(f)["data"]
                    for i in range(len(val_list)):
                        try:
                            if data[key_list[i]] == val_list[i]:
                                if files in total_files:
                                    pass
                                else:
                                    total_files.append(files)
                        except KeyError:
                            pass
            
            return total_files

                    
                    
            

new = Nodes(directory = "/Users/winstonwalter/Desktop/demo_file/") 

#new.makeNodeObject(json_data={"hello": "world"}, timestamp=True)
print(new.findNodeObject({"id": 1400, "hello": "world"}, method="contains"))