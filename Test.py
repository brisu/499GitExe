import unittest
from Master import anagramComp

class anagram(unittest.TestCase):

   def testFirstAna(self):
       self.assertTrue(is_anagram("hi", "eat"))

   def test_different_lengths(self):
       self.assertFalse(is_anagram("tea", "treat"))
