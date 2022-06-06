import unittest
from problems import *

class TestProblemSolvers(unittest.TestCase):
    def test_multipladd(self):
        self.assertEqual(multipladd(3, 5, 1000), 233168)

    def test_evenfibs(self):
        self.assertEqual(evenfibs(4000000), 4613732)

    def test_sumsquarediff(self):
        self.assertEqual(sumsquarediff(100), 25164150)
