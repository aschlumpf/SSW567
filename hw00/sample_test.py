import unittest

class SampleTest(unittest.TestCase):
  def itShouldBeFour(self):
    self.assertEqual(2+2, 4)

if __name__ == '__main__':
  unittest.main()