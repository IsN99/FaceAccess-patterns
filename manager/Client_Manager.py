import base64
import requests

class Manager_Client:
    def __init__(self, server_url='http://localhost:8888'):
        self.server_url = server_url
          
    def get_history(self):
        payload = {'method': 'Manager_History'}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200:
            return response.json()['history']
        else:
            return None
        
    def get_empls(self):
        payload = {'method': 'Manager_Empls'}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200:
            return response.json()['empls']
        else:
            return None
        
    def create(self, name, photo_path):
        with open(photo_path, 'rb') as f:
            photo_data = f.read()
        photo_b64 = base64.b64encode(photo_data).decode()
        payload = {'method': 'Manager_Create', 'name': name, 'photo': photo_b64}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200 and response.json()['result'] == 'Success':
            return True
        else:
            return False
        
    def update(self, id, name, photo_path):
        with open(photo_path, 'rb') as f:
            photo_data = f.read()
        photo_b64 = base64.b64encode(photo_data).decode()
        payload = {'method': 'Manager_Update', 'id': id, 'name': name, 'photo': photo_b64}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200 and response.json()['result'] == 'Success':
            return True
        else:
            return False
        
    def delete(self, id):
        payload = {'method': 'Manager_Delete', 'id': id}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200 and response.json()['result'] == 'Success':
            return True
        else:
            return False
        
    def restore(self, id):
        payload = {'method': 'Restore', 'id': id}
        response = requests.post(self.server_url, json=payload)
        if response.status_code == 200 and response.json()['result'] == 'Success':
            return True
        else:
            return False
