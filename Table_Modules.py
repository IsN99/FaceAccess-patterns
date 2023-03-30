import Row_Data_Gateway as rdg
from Buffer_GOF import Emp_Buffer

# Employees_TM

# class Employees_TM:
#     def __init__(self):
#         self.gateway = rdg.Empl_RDG()
#
#     def get_employee_by_id(self, id):
#         return self.gateway.get(id=id)[0]
#
#     def get_all_employees(self):
#         return self.gateway.get()
#
#     def create_employee(self, name, photo_path):
#         employee = rdg.Empl_RDG(name=name, photo_path=photo_path)
#         employee.insert()
#
#
#     def update_employee(self, id, name, photo_path):
#         employee = rdg.Empl_RDG(id=id, name=name, photo_path=photo_path)
#         employee.update()
#
#
#     def delete_employee(self, id):
#         employee = rdg.Empl_RDG(id=id)
#         employee.delete()

class Employees_TM:
    def __init__(self):
        self.gateway = rdg.Empl_RDG
        self.buffer = Emp_Buffer()

    def get_employee_by_id(self, id):
        return self.gateway.get(id=id)[0]

    def get_all_employees(self):
        return self.gateway.get()

    def create_employee(self, name, photo_path):
        employee = rdg.Empl_RDG(name=name, photo_path=photo_path)
        employee.insert()


    def update_employee(self, id, name, photo_path):
        try:
            employee = rdg.Empl_RDG(id=id, name=name, photo_path=photo_path)
            state = self.gateway.get(id=id)[0]
            self.buffer.save_state(id, state)
            employee.update()
        except():
            "Sorry"

    def delete_employee(self, id):
        try:
            employee = rdg.Empl_RDG(id=id)
            state = self.gateway.get(id=id)[0]
            self.buffer.save_state(id, state)
            employee.delete()
        except():
            "Sorry"

    def restore(self, id):
        state = self.buffer.get_state(id)
        obj = self.gateway.get(id)
        if state:
            if obj:
                state.update()
            else:
                state.insert()

# Checkpoints_TM

class Checkpoints_TM:
    def __init__(self):
        self.gateway = rdg.Checkpoint_RDG()

    def get_checkpoint_by_id(self, id):
        return self.gateway.get(id=id)[0]

    def get_all_checkpoints(self):
        return self.gateway.get()

    def create_checkpoint(self, access_zone):
        checkpoint = rdg.Checkpoint_RDG(access_zone=access_zone)
        checkpoint.insert()


    def update_checkpoint(self, id, access_zone):
        checkpoint = rdg.Checkpoint_RDG(id=id, access_zone=access_zone)
        checkpoint.update()


    def delete_checkpoint(self, id):
        checkpoint = rdg.Checkpoint_RDG(id=id)
        checkpoint.delete()

# Requests_TM

class Requests_TM:
    def __init__(self):
        self.gateway = rdg.Request_RDG()

    def get_request_by_id(self, id):
        return self.gateway.get(id=id)[0]

    def get_all_requests(self):
        return self.gateway.get()

    def create_request(self, date, result, image_path, checkpoint_id, employee_id):
        request = rdg.Request_RDG(date=date, result=result, image_path=image_path, checkpoint_id=checkpoint_id, employee_id=employee_id)
        request.insert()


    def update_request(self, id, date, result, image_path, checkpoint_id, employee_id):
        request = rdg.Request_RDG(id=id, date=date, result=result, image_path=image_path, checkpoint_id=checkpoint_id, employee_id=employee_id)
        request.update()


    def delete_request(self, id):
        request = rdg.Request_RDG(id=id)
        request.delete()
