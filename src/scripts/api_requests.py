import requests     # Request data from API
import json         # Json Format to print

class seehowapi():
    def __init__(self):
        self.api_url_get            = "https://0phfqk.deta.dev/"
        self.api_url_get_by_id      = "https://0phfqk.deta.dev/hand/"
        self.api_url_get_by_name    = "https://0phfqk.deta.dev/get-hand-by-name/"
        self.api_url_post           = "https://0phfqk.deta.dev/create-hand/"
        self.api_url_put            = "https://0phfqk.deta.dev/update-hand/"
        self.api_url_delete         = "https://0phfqk.deta.dev/delete-hand/"
        
        
    # Create a hand object in API    
    def post(self, countFingers = 0, level = 0, name = 'none', side = 'none', id = 0):
        
        data                        = {
                                            "countFingers": countFingers,
                                            "level": level,
                                            "name": name,
                                            "side": side
                                        }
        
        # Get by id to verify if exists
        if self.getbyid(id) == 200:
            self.post(countFingers, level, name, side, id)
            return
        
        post_response   = requests.post(self.api_url_post+f"{id}", json = data)
        print(self.jprint(post_response.json()))
     
     
    # Update a hand object in API    
    def put(self, countFingers = 0, level = 0, name = 'none', side = 'none', id = 0):
        
        data                        = {
                                            "countFingers": countFingers,
                                            "level": level,
                                            "name": name,
                                            "side": side
                                        }
        
        ### Get by id to verify if exists
        if self.getbyid(id) == 200:
            put_response   = requests.put(self.api_url_put+f"{id}", json = data)
            print(self.jprint(put_response.json()))   
            return
        
        self.post(countFingers, level, name, side, id)
        
    def delete(self, id):
        delete_response = requests.delete(self.api_url_delete+f"{id}")
        return delete_response.status_code
        
    # Get all the data from API    
    def get(self):
        get_response    = requests.get(self.api_url_get)
        return get_response.status_code
        
    # Get data by id    
    def getbyid(self, id):
        get_response    = requests.get(self.api_url_get_by_id+f"{id}") 
        return get_response.status_code      

    # Get data by id    
    def getbyname(self, name):
        get_response    = requests.get(self.api_url_get_by_name+f"{name}") 
        return get_response.status_code
    
    # Convert data format to print like JSON
    def jprint(self, obj):
        response = json.dumps(obj, sort_keys = True, indent = 4)
        return response

