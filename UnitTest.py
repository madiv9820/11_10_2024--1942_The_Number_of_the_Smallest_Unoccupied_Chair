from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testCases = {
            1: {'times': [[1,4],[2,3],[4,6]], 'targetFriend': 1, 'output': 1},
            2: {'times': [[3,10],[1,5],[2,6]], 'targetFriend': 0, 'output': 2},
        }
        
        self.obj = Solution()
        return super().setUp()
    
    def test_Case1(self):
        times, targetFriend, output = self.testCases[1].values()
        result = self.obj.smallestChair(times = times, targetFriend = targetFriend)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    def test_Case2(self):
        times, targetFriend, output = self.testCases[2].values()
        result = self.obj.smallestChair(times = times, targetFriend = targetFriend)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()