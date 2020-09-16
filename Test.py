import unittest
from Master import anagramComp

class anagram(unittest.TestCase):

   def testTrue(self):
       self.assertTrue(anagramComp("a b c", "a c b"))

   def testString(self):
       self.assertFalse(anagramComp("I am happy", "I am sad"))
