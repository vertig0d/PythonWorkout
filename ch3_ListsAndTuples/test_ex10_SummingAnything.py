import unittest
from ex10_SummingAnything import mysum

class Test(unittest.TestCase):
    def test_mysum(self):
        self.assertEqual(mysum('abc', 'def'), 'abcdef')    
        self.assertEqual(mysum([1,2,3], [4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(mysum(5,6), 11)

if __name__ == '__main__':
    unittest.main()