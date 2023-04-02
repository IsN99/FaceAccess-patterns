import http.server
import socketserver
import json
import base64
from User import User
from Manager import Manager
import datetime

user = User()
manager = Manager()

class MyHandler(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if data['method'] == 'Access_Request':
            
            image_data = base64.b64decode(data['image'])
            image_path = 'images/' + date
            with open(image_path, 'wb') as f:
                f.write(image_data)
            
            result_path = user.Access_Request(image_path) 
            if result_path:        
                with open(result_path, 'rb') as f:
                    image_result = f.read()            
                image_b64 = base64.b64encode(image_result).decode() 
                response = {'result':'Success','image': image_b64}           
                self.send_response(200)
                self.send_header('Content-type', 'application/json')              
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            else:
                response = {'result':'Fail'}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')              
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

        elif data['method'] == 'Manager_History':
            history = manager.get_history()

            # Отправляем ответ 
            response = {'history': history}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif data['method'] == 'Manager_Empls':
            empls = manager.get_empls()

            # Отправляем ответ 
            response = {'empls': empls}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif data['method'] == 'Manager_Create':
            name = data['name']
            photo_data = base64.b64decode(data['photo'])
            photo_path = 'images/' + date
            with open(photo_path, 'wb') as f:
                f.write(photo_data)

            manager.create(name, photo_path)

            # Отправляем ответ 
            response = {'result': 'Success'}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif data['method'] == 'Manager_Update':
            id = data['id']
            name = data['name']
            photo_data = base64.b64decode(data['photo'])
            photo_path = 'images/' + date
            with open(photo_path, 'wb') as f:
                f.write(photo_data)

            manager.update(id, name, photo_path)

            # Отправляем ответ 
            response = {'result': 'Success'}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        elif data['method'] == 'Manager_Delete':
            id = data['id']

            manager.delete(id)

            # Отправляем ответ 
            response = {'result': 'Success'}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        
        elif data['method'] == 'Restore':
            
            id = data['id']
            
            manager.restore(id)
            
            response = {'result': 'Success'}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

PORT = 8888

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()