import unittest
from src.pipeline import process


class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        data = ("what is sachin's salary?", "265000")
        result = process(data[0])
        assert data[1] in result


if __name__ == "__main__":
    unittest.main()