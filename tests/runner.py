import unittest
from tests.unit import 

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(yaml_to_cart.TestYAMLToCart))
  return suite

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())