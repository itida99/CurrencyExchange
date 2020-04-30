# Name : Aditi Gupta 
# Roll No : 2019292
# Group : B-8

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertEqual(changeBase(1,"EUR","MYR","2000-10-25"), 'currency not found')
		self.assertEqual(changeBase(-1,"EUR","MYR","1980-3-4"), 'amount cannot be negative')
		self.assertEqual(changeBase(90,"EUR","EUR","2007-7-5"), 90)
		self.assertAlmostEqual(changeBase(62,"CHF", "HRK", "2008-9-5"), 278.41, delta = 0.1)
		self.assertAlmostEqual(changeBase(13,"CAD", "SGD", "1999-10-12"), 14.733, delta = 0.1)
		self.assertEqual(changeBase(12.80,"DKK", "HUF", "2003-06-08"), 449.1016351049215)
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()