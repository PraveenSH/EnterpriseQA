import unittest
from src.modules.tasks_detector import Detector

class TestDetector(unittest.TestCase):

    def test_task_detector(self):
        data = [("get emloyee id of praveen", ["hr"], ["get_employee_id"]),
                ("what is the salary of john", ["hr", "payroll"], ["get_employee_id", "get_comp"])]

        for d in data:
            result = Detector().detector(d[0], d[1])
            assert result == d[2]


if __name__ == "__main__":
    unittest.main()