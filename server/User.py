from Table_Modules import *
import face_recognition
import datetime
import cv2

class User:
    def __init__(self):
        self.employee_tm = Employees_TM()
        self.request_tm = Requests_TM()

    def Access_Request(self, image_path, checkpoint_id=1):
        employees = self.employee_tm.get_all_employees()
        results = []
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Загружаем входное изображение и конвертируем его в RGB формат
        input_image = face_recognition.load_image_file(image_path)
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

        # Изменяем размер входного изображения
        input_image = cv2.resize(input_image, (0, 0), fx=0.25, fy=0.25)

        # Получаем кодировку лица для входного изображения
        input_encoding = face_recognition.face_encodings(input_image)

        for employee in employees:
            employee_dict = employee.__dict__
            employee_photo_path = employee_dict['photo_path']
            try:
                # Загружаем фотографию сотрудника и конвертируем ее в RGB формат
                employee_photo = face_recognition.load_image_file(employee_photo_path)
                employee_photo = cv2.cvtColor(employee_photo, cv2.COLOR_BGR2RGB)

                # Изменяем размер фотографии сотрудника
                employee_photo = cv2.resize(employee_photo, (0, 0), fx=0.25, fy=0.25)

                # Получаем кодировку лица для фотографии сотрудника
                employee_encoding = face_recognition.face_encodings(employee_photo)

                # Сравниваем кодировки лиц
                result = face_recognition.compare_faces([employee_encoding[0]], input_encoding[0])
                if result[0]:
                    results.append(employee_dict)
            except FileNotFoundError:
                continue

        if results:
            self.request_tm.create_request(date, True, image_path, checkpoint_id, results[0]['id'])
            return results[0]['photo_path']
        else:
            self.request_tm.create_request(date, False, image_path, checkpoint_id, None)
            return None
