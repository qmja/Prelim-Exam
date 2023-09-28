import unittest

def name(x):
   return x == "PEDRO"

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(name("Pedro"))

if __name__== '__main__':

    unittest.main()
