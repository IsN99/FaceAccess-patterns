from Table_Modules import *

# join - функция
def merge_dicts_by_key(list1, list2, key1, key2):
    merged_list = []
    for dict1 in list1:
        for dict2 in list2:
            if dict1[key1] == dict2[key2]:
                merged_dict = {**dict1, **dict2}
                merged_list.append(merged_dict)
    return merged_list

class Manager():
    def __init__(self):
        self.employee_list = Employees_TM()
        self.checkpoint_list = Checkpoints_TM ()
        self.request_list = Requests_TM()

    def get_history(self):
        employees = self.employee_list.get_all_employees()
        employee_ = [employee.__dict__ for employee in employees]

        checkpoints = self.checkpoint_list.get_all_checkpoints()
        checkpoint_ = [checkpoint.__dict__ for checkpoint in checkpoints]

        requests = self.request_list.get_all_requests()
        request_ = [request.__dict__ for request in requests]

        history = merge_dicts_by_key(request_, employee_, 'employee_id', 'id')
        history = merge_dicts_by_key(history, checkpoint_, 'checkpoint_id', 'id')

        return history

    def get_empls (self):
        employees = self.employee_list.get_all_employees()
        return [employee.__dict__ for employee in employees]

    def create (self, name, photo_path):
        self.employee_list.create_employee(name,photo_path)

    def update (self, id, name, photo_path):
        self.employee_list.update_employee(id, name, photo_path)

    def delete(self, id):
        self.employee_list.delete_employee(id)

    def restore(self, id):
        self.employee_list.restore(id)