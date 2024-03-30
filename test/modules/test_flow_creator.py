import unittest
from src.modules.flow_creator import Creator


class TestFlowCreator(unittest.TestCase):

    def test_extract_parameters(self):
        data = ("what is sachin's salary?", "get_employee_id", {}, "sachin")
        result = Creator().extract_parameters(data[0], data[1], data[2])
        assert result == data[3]

if __name__ == "__main__":
    unittest.main()