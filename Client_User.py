import base64
import requests
import os

class User_Client:
    def __init__(self):
        self.server_url = 'http://localhost:8888'
        
    def access_request(self, image_path):
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_b64 = base64.b64encode(image_data).decode()
        payload = {'method': 'Access_Request', 'image': image_b64}
        response = requests.post(self.server_url, json=payload)
        if response.json()['result'] == 'Success':
            image_result = base64.b64decode(response.json()['image'])
            result_path = os.path.join(os.getcwd(), 'result')
            with open(result_path, 'wb') as f:
                f.write(image_result)
            return result_path
        else:
            return None

