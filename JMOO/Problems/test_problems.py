import unittest
from Problems.Schaffer import Schaffer

class TestProblems(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_schaffer(self):
        """Ensure that then Schaffer problem is working properly"""
        self.assertEquals(Schaffer().evaluate(input = [7]), [49,25])

if __name__ == '__main__':
    unittest.main()
