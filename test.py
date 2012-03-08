import unittest

from bloom import *

class TestBasicFilter(unittest.TestCase):
    
    def setUp(self):
        self.b = Bloom(500000, 5)

    def testMightExist(self):
        self.b.add('pony')
        self.assertTrue('pony' in self.b)
    
    def testNotExist(self):
        self.b.add('pony')
        self.assertFalse('cat' in self.b)

if __name__ == '__main__':
    unittest.main()
