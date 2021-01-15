import tests.context

import unittest

import sheets

class TestFuncs(unittest.TestCase):
	'''
	Exercise the functionality given by the dummy funcs
	'''

	def test_func_1_positive_num(self):
		res = sheets.func_1(3)

		self.assertEqual(res, 1)