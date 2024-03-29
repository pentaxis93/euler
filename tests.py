import unittest
from problems import *

class TestProblemSolvers(unittest.TestCase):
    def test_multipladd(self):
        self.assertEqual(multipladd(3, 5, 1000), 233168)

    def test_evenfibs(self):
        self.assertEqual(evenfibs(4000000), 4613732)

    def test_sumsquarediff(self):
        self.assertEqual(sumsquarediff(100), 25164150)

    def test_smallmult(self):
        self.assertEqual(smallmult(20), 232792560)

    def test_largestpfactor(self):
        self.assertEqual(largestpfactor(600851475143), 6857)

    def test_largestpalinprod(self):
        self.assertEqual(largestpalinprod(), 906609)

    def test_nthprime(self):
        self.assertEqual(nthprime(10001), 104743)

    def test_specpythtrip(self):
        self.assertEqual(specpythtrip(), 31875000)

    def test_seriesprod(self):
        self.assertEqual(seriesprod(13), 23514624000)
