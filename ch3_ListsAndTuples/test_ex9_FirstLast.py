import unittest
from ex9_FirstLast import first_last

class Test(unittest.TestCase):
    def test_first_last(self):
        self.assertEqual(first_last('abc'), 'ac')
        self.assertEqual(first_last([1,2,3,4]), [1,4])
    
    def test_first_last_type(self):
        with self.assertRaises(TypeError):
            first_last(35)

if __name__ == '__main__':
    unittest.main()