import unittest
import Random_Walk, Random_Walk2

class Random_Walk_Test(unittest.TestCase):

    def test_one(self):
        for i in range(5):
            walk = Random_Walk.random_walk(10)
            print (walk, 'Distance from home=', abs(walk[0] + abs(walk[1])))
        self.defaultTestResult()

    def test_two(self):
        for i in range(25):
            walk = Random_Walk2.random_walk_2(10)
            print (walk, 'Distance from home=', abs(walk[0] + abs(walk[1])))
        self.defaultTestResult()

if __name__ == '__main__':
    unittest.main()
