from data.mock_app_data import MockData

class PayrollDatabse:

    def __init__(self):
        self.data = MockData.payroll_data


    def get_comp(self, emp_id):
        for employee in self.data:
            if employee["emp_id"] == emp_id:
                return {"compensation": employee["comp"]}
        return {}

    def get_total_comp(self, emp_ids):

        total_comp = 0
        for employee in self.data:
            if employee["emp_id"] in emp_ids:
                total_comp += employee["comp"]
        return {"total compensation": total_comp}