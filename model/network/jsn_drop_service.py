import requests 
import json 

#YOUR_TOKEN_GOES_HERE
#https://docs.python.org/3/library/json.html

class jsnDrop(object):

    def __init__(self, tok = None, url = None) -> None:
        self.tok = tok
        self.url = url
        self.jsnStatus = ""
        self.jsnResult = {}

        # Setting up data structures for storing JsnDrop Commands
        self.decode = json.JSONDecoder().decode
        self.encode = json.JSONEncoder().encode

        self.jsnDropRecord = self.decode('{"tok":"","cmd":{}}')
        self.jsnDropCreate = self.decode('{"CREATE":"aTableName","EXAMPLE":{}}')
        self.jsnDropStore  = self.decode('{"STORE":"aTableName","VALUE":[]}')
        self.jsnDropAll    = self.decode('{"ALL":"aTableName"}')
        self.jsnDropSelect = self.decode('{"SELECT":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDelete = self.decode('{"DELETE":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDrop   = self.decode('{"DROP":"aTableName"}')

    def jsnDropApi(self,command):
        api_call  = self.jsnDropRecord
        api_call["tok"] = self.tok
        api_call["cmd"] = command
        payload = {'tok': self.encode(api_call)}

        # Feedback to check it works
        # print(f"API CALL PAYLOAD= {payload}")

        # Request to the API - LOOK UP calls to requests.get() ARE they Synchronous or Asynchronous?
        r = requests.get(self.url, payload)

        # Update the status and result
        jsnResponse = r.json()
        self.jsnStatus = jsnResponse["JsnMsg"]
        self.jsnResult = jsnResponse["Msg"]

        # Feedback to check it works
        print(f"Status = {self.jsnStatus} , Result = {self.jsnResult}")
        return self.jsnResult 

    
    def create(self,table_name, example):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"YOUR_TOKEN_GOES_HERE","cmd":{"CREATE":"tblTest","EXAMPLE":{"PersonID  PK":"Todd","Score":21}}}
        command = self.jsnDropCreate
        command["CREATE"] = table_name
        command["EXAMPLE"] = example
        return self.jsnDropApi(command)
        
    def store(self, table_name, value_list):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"YOUR_TOKEN_GOES_HERE","cmd":{"STORE":"tblTest","VALUE":[{"PersonID":"Todd","Score":21},{"PersonID":"Jane","Score":2000}]}}
        command = self.jsnDropStore
        command["STORE"] = table_name
        command["VALUE"] = value_list
        return self.jsnDropApi(command)

    def all(self, table_name):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"YOUR_TOKEN_GOES_HERE","cmd":{"ALL":"tblTest"}} 
        command = self.jsnDropAll
        command["ALL"] = table_name
        return self.jsnDropApi(command)

    def select(self, table_name, where):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"YOUR_TOKEN_GOES_HERE","cmd":{"SELECT":"tblTest","WHERE":"Score > 200"}}
        command = self.jsnDropSelect
        command["SELECT"] = table_name
        command["WHERE"] = where
        return self.jsnDropApi(command)

    def delete(self,table_name, where):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"YOUR_TOKEN_GOES_HERE","cmd":{"DELETE":"tblTest","WHERE":"Score > 200"}}
        command = self.jsnDropDelete
        command["DELETE"] = table_name
        command["WHERE"] = where
        return self.jsnDropApi(command)

    def drop(self,table_name):
        command = self.jsnDropDrop
        command["DROP"] = table_name
        return self.jsnDropApi(command)

    

#class jsnTable(object):

