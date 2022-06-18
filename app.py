from datetime import datetime
import os
import json

class PathError(Exception):
    def __init__(self, message="No path was entered"):
        self.message = message
        super().__init__(self.message)

class MakeNodeObject:
    def __init__(self, content=None, timeStamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), path = None):
        '''Path is set to none by default because node file doesn't exist yet. also input the path of the file that
        the nodes will be in aka C:/Users/admin/Desktop/file or something like that'''

        self.content = content

        self.timeStamp = timeStamp
        
        self.path = path

        self.previous = None
        
        if path is None:
            raise PathError()

        files = []
        
        for file in os.listdir(os.getcwd()):
            if file.endswith(".json"):
                files.append(file)
    
        if files == []:
            self.id_code = None
            self.metadata = {
            "Node Files": True,
            "id_code": self.id_code,
            "data": {
                "content": str(self.content),
                "timeStamp": str(self.timeStamp),
                "path of prev": f"{str(0)}.json".replace("\\", "/")
            }
        }
        else:
            large = int(files[0].split('.')[0])
            for number in files:
                if int(number.split('.')[0]) > int(large):
                    large = int(number.split('.')[0])
            self.id_code = large+1

            self.metadata = {
            "Node Files": True,
            "id_code": self.id_code,
            "data": {
                "content": str(self.content),
                "timeStamp": str(self.timeStamp),
                "path of prev": f"{str(self.path)}/{str(self.id_code-1)}.json".replace("\\", "/")
            }
        }
        print("past id_code assignment")
        

        self.startFile = {
            "Node Files": True,
            "id_code": "000000000000",
            "data": {
                "content": "startFile",
                "timeStamp": str(self.timeStamp),
                "path of prev": None
            }
        }

        if len(os.listdir(os.getcwd()))-1 < 1:
            with open(f"{os.curdir}/0.json", "w") as f:
                f.write(json.dumps(self.startFile))

        if "0.json" in os.listdir(os.getcwd()):
             with open(f"{os.curdir}/{self.id_code}.json", "w") as f:
                f.write(json.dumps(self.metadata))
    
class FindNode:
    def __init__(self, findBy: dict):
        '''the structure of the findBy dict is 
        {

        }'''

MakeNodeObject(content="first!", path=os.getcwd())