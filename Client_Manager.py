import requests
import base64

class User_Client:
    def __init__(self, server_url = 8888):
        self.server_url = server_url

    def manager_history(self):
        payload = {'method': 'Manager_History'}
        response = requests.post(self.server_url, json=payload)
        return response.json()

    def manager_empls(self):
        payload = {'method': 'Manager_Empls'}
        response = requests.post(self.server_url, json=payload)
        return response.json()

    def manager_create(self, name, photo_path):
        with open(photo_path, 'rb') as f:
            photo_data = f.read()
        photo_b64 = base64.b64encode(photo_data).decode()
        payload = {'method': 'Manager_Create', 'name': name, 'photo': photo_b64}
        response = requests.post(self.server_url, json=payload)
        return response.json()

    def manager_update(self, id, name, photo_path):
        with open(photo_path, 'rb') as f:
            photo_data = f.read()
        photo_b64 = base64.b64encode(photo_data).decode()
        payload = {'method': 'Manager_Update', 'id': id, 'name': name, 'photo': photo_b64}
        response = requests.post(self.server_url, json=payload)
        return response.json()

    def manager_delete(self, id):
        payload = {'method': 'Manager_Delete', 'id': id}
        response = requests.post(self.server_url, json=payload)
        return response.json()

    def restore(self, id):
        payload = {'method': 'Restore', 'id': id}
        response = requests.post(self.server_url, json=payload)
        return response.json()
