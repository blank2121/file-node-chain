from datetime import datetime
import os
import json

class Nodes:
    def __init__(self, json_data, timestamp: bool):
        self.json_data = json_data
        
        if timestamp:
            self.timestamp = datetime.now()

        print(self.timestamp)


Nodes(json_data = {}, timestamp=True)
