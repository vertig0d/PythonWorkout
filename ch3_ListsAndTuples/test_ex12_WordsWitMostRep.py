import unittest
from ex12_WordsWithMostRepeatedWords import get_counter_val

class Test(unittest.TestCase):
    def test_mostrep(self):
        words = ['this', 'is', 'an', 'elementary', 'test', 'example']
        self.assertEqual(get_counter_val(words), 'elementary')
    
if __name__ == '__main__':
    unittest.main()