import unittest

import utility.factors as uf


class Test(unittest.TestCase):
    def test_is_factor(self):
        factorsof36 = [1, 36, 2, 18, 3, 12, 4, 9, 6]
        for factor in factorsof36:
            self.assertTrue(uf.is_factor(factor, 36))
        
        self.assertFalse(uf.is_factor(5, 36))
        
        self.assertTrue(uf.is_factor(1, 1711))
        self.assertTrue(uf.is_factor(12, 144))
        self.assertTrue(uf.is_factor(80, 8000))
        self.assertFalse(uf.is_factor(7, 10))
        self.assertFalse(uf.is_factor(9, 120))
        
    def test_get_factors(self):
        self.assertEqual(set(uf.get_factors(32)), {1, 32, 2, 16, 4, 8})
        self.assertEqual(set(uf.get_factors(1)), {1})
        self.assertEqual(set(uf.get_factors(7)), {1, 7})
    
    def test_get_proper_divisors(self):
        self.assertEqual(set(uf.get_proper_divisors(1)), set())
        self.assertEqual(set(uf.get_proper_divisors(2)), {1})
        self.assertEqual(set(uf.get_proper_divisors(3)), {1})
        self.assertEqual(set(uf.get_proper_divisors(4)), {1, 2})
        self.assertEqual(set(uf.get_proper_divisors(32)), {1, 2, 16, 4, 8})
    
    def test_get_proper_factors(self):
        self.assertEqual(set(uf.get_proper_factors(1)), set())
        self.assertEqual(set(uf.get_proper_factors(2)), set())
        self.assertEqual(set(uf.get_proper_factors(3)), set())
        self.assertEqual(set(uf.get_proper_factors(4)), {2})
        self.assertEqual(set(uf.get_proper_factors(32)), {2, 16, 4, 8})
    
    def test_eulers_algorithm(self):
        eatest = uf.euclids_algorithm(76, 45)
        self.assertSequenceEqual(next(eatest), (1, 31, 1, 1))
        self.assertSequenceEqual(next(eatest), (1, 14, 2, 1))
        self.assertSequenceEqual(next(eatest), (2, 3, 5, 3))
        self.assertSequenceEqual(next(eatest), (4, 2, 22, 13))
        self.assertSequenceEqual(next(eatest), (1, 1, 27, 16))
        self.assertSequenceEqual(next(eatest), (2, 0, 76, 45))
        with self.assertRaises(StopIteration):
            next(eatest)
    
    def test_get_eulers_table(self):
        expected_table = [
            (1, 31, 1, 1), (1, 14, 2, 1), (2, 3, 5, 3), (4, 2, 22, 13),
            (1, 1, 27, 16), (2, 0, 76, 45)
        ]
        actual_table = uf.get_euclids_table(76, 45)
        self.assertEqual(expected_table, actual_table)
    
    def test_get_hcf(self):
        self.assertEqual(uf.get_hcf(76, 45), 1)
        self.assertEqual(uf.get_hcf(54321, 12345), 3)
        self.assertEqual(uf.get_hcf(3528, 966), 42)
    
    def test_get_lowest_fraction(self):
        self.assertEqual(uf.get_lowest_fraction(76, 45), (76, 45))
        self.assertEqual(uf.get_lowest_fraction(3528, 966), (84, 23))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()