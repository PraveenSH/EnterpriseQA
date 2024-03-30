from data.mock_app_data import MockData

class HrDatabse:

    def __init__(self):
        self.data = MockData.hr_data


    def get_employee_name(self, emp_id):

        for employee in self.data:
            if employee["emp_id"] == emp_id:
                return {"employee_name": employee["emp_name"]}

        return {}


    def get_employee_id(self, name):

        for employee in self.data:
            if employee["emp_name"] == name:
                return {"employee_id": employee["emp_id"]}

        return {}


    def get_manager_name(self, emp_id):

        for employee in self.data:
            if employee["emp_id"] == emp_id:
                manager_id = employee["manager_id"]
                return {"manager_name": self.get_employee_name(manager_id)}

        return {}


    def get_manager_id(self, emp_id):

        for employee in self.data:
            if employee["emp_id"] == emp_id:
                return {"manager_id": employee["manager_id"]}

        return {}