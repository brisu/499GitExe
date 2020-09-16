import unittest
from Master import anagramComp

class anagram(unittest.TestCase):

   def testTrue(self):
       self.assertTrue(anagramComp("a b 3 b", "a b b"))

   def testString(self):
       self.assertFalse(anagramComp("I am ha99y", "I am happy"))
