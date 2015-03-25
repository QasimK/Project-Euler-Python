import unittest
import utility.integers as integers

class Test(unittest.TestCase):

    def test_is_integer(self):
        self.assertTrue(integers.is_integer(50))
        self.assertTrue(integers.is_integer(50))
        self.assertTrue(integers.is_integer(-26))
        self.assertTrue(integers.is_integer(40.0))
        self.assertFalse(integers.is_integer(40.5))
        self.assertFalse(integers.is_integer(-0.5))
    
    def test_digit_factorial(self):
        assert(integers.digit_factorial(0)==1)
        assert(integers.digit_factorial(1)==1)
        assert(integers.digit_factorial(2)==2)
        assert(integers.digit_factorial(3)==6)
        assert(integers.digit_factorial(9)==362880)
        assert(integers.digit_factorial(11)==2)
        assert(integers.digit_factorial(256)==842)
        assert(integers.digit_factorial(200)==4)
    
    def test_rotations(self):
        self.assertSequenceEqual(integers.get_rotations(1), [1])
        self.assertSequenceEqual(integers.get_rotations(9), [9])
        
        self.assertSequenceEqual(sorted(integers.get_rotations(20)),
                         sorted([20, 2]))
        self.assertSequenceEqual(sorted(integers.get_rotations(2345)),
                         sorted([2345, 3452, 4523, 5234]))
        self.assertSequenceEqual(sorted(integers.get_rotations(200406)),
                         sorted([200406, 4062, 40620, 406200, 62004, 620040]))
        
        self.assertEquals(len(integers.get_rotations(1234567890)), 10)
        
        #Test for palindrome duplications
        self.assertSequenceEqual(sorted(integers.get_rotations(1111)), [1111])
        self.assertSequenceEqual(sorted(integers.get_rotations(2121)),
                         sorted([2121, 1212]))
        self.assertSequenceEqual(sorted(integers.get_rotations(123123)),
                         sorted([123123, 231231, 312312]))
    
    def test_get_triangle_number(self):
        self.assertEqual(integers.get_triangle_number(1), 1)
        self.assertEqual(integers.get_triangle_number(4), 10)
        self.assertEqual(integers.get_triangle_number(10), 55)
    
    def test_get_triangle_numbers(self):
        triangle_numbers = integers.get_triangle_numbers()
        self.assertEqual(next(triangle_numbers), 1)
        self.assertEqual(next(triangle_numbers), 3)
        self.assertEqual(next(triangle_numbers), 6)
        self.assertEqual(next(triangle_numbers), 10)
        self.assertEqual(next(triangle_numbers), 15)
        self.assertEqual(next(triangle_numbers), 21)
        self.assertEqual(next(triangle_numbers), 28)
        self.assertEqual(next(triangle_numbers), 36)
        self.assertEqual(next(triangle_numbers), 45)
        self.assertEqual(next(triangle_numbers), 55)
    
    def test_is_triangle_number(self):
        self.assertFalse(integers.is_triangle_number(59))
        
        self.assertTrue(integers.is_triangle_number(1))
        self.assertTrue(integers.is_triangle_number(55))
        self.assertTrue(integers.is_triangle_number(630))
        self.assertTrue(integers.is_triangle_number(5050))
        
        self.assertFalse(integers.is_triangle_number(5000000049999999))
        self.assertTrue(integers.is_triangle_number(5000000050000000))
        self.assertFalse(integers.is_triangle_number(5000000050000001))
    
    def test_is_pentagonal(self):
        self.assertTrue(integers.is_pentagonal(117))
        self.assertFalse(integers.is_pentagonal(118))
        
        self.assertFalse(integers.is_pentagonal(144))
        self.assertTrue(integers.is_pentagonal(145))
        self.assertFalse(integers.is_pentagonal(146))
    
    def test_get_pentagonal(self):
        self.assertEqual(integers.get_pentagonal(1), 1)
        self.assertEqual(integers.get_pentagonal(10), 145)
    
    def test_get_pentagonals(self):
        pentagonals = integers.get_pentagonals()
        actual_pentagonals = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(next(pentagonals), actual_pentagonals[i])
    
    def test_choose(self):
        self.assertEqual(integers.choose(0, 0), 1)
        self.assertEqual(integers.choose(1, 0), 1)
        self.assertEqual(integers.choose(1, 1), 1)
        
        self.assertEqual(integers.choose(3, 1), integers.choose(3, 2))
        
        self.assertEqual(integers.choose(5, 2), 10)
        self.assertEqual(integers.choose(6, 3), 20)
        self.assertEqual(integers.choose(7, 5), 21)


if __name__ == "__main__":
    unittest.main()