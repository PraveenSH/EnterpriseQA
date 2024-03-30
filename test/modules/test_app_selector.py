import unittest
from src.modules.apps_selector import Selector


class TestSelector(unittest.TestCase):

    def test_app_selector(self):
        data = [("get emloyee id of praveen", ["hr"]),
                ("what is the salary of john", ["hr", "payroll"])]

        for d in data:
            result = Selector().detect(d[0])
            assert result == d[1]

if __name__ == "__main__":
    unittest.main()