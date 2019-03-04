import unittest

def placeholder(x):
    return x + 1

class PlaceholderTest(unittest.TestCase):
    def test(self):
        self.assertEqual(placeholder(3), 4)

if __name__ == '__main__':
    unittest.main()
