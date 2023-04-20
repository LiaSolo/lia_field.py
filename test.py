import unittest
from field import Field
from simple_field import PrimeField
from main import RandomGenerator


class FieldsTester(unittest.TestCase):
    def test_addition_1(self):
        f = Field(2, [1, 1, 1])
        elem1 = [0, 1]
        elem2 = [1, 1]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 0], 'oops in test_addition_1')

    def test_addition_2(self):
        f = Field(3, [1, 2, 0, 1])
        elem1 = [2, 1, 1]
        elem2 = [2, 2, 1]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 0, 2], 'oops in test_addition_2')

    def test_addition_3(self):
        f = Field(5, [2, 3, 0, 1])
        elem1 = [4, 4, 1]
        elem2 = [3, 2, 0]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [2, 1, 1], 'oops in test_additions_3')

    def test_addition_4(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem1 = [0, 1, 1, 1]
        elem2 = [1, 0, 1, 0]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 1, 0, 1], 'oops in test_addition_4')

    def test_is_norm_1(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem = [0, 1, 1, 2]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in test_is_norm_1')

    def test_is_norm_2(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem = [0, 1, 0, 1]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, True, 'oops in test_is_norm_2')

    def test_is_norm_3(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem = [0, 1, 1]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in  test_is_norm_3')

    def test_opposite_addition_1(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem = [0, 1, 1, 1]

        res = f.opposite_addition(elem)
        self.assertEqual(res, [0, 1, 1, 1], 'oops in test_opposite_addition_1')

    def test_opposite_addition_2(self):
        f = Field(5, [2, 2, 1, 0, 1])
        elem = [4, 3, 2, 1]

        res = f.opposite_addition(elem)
        self.assertEqual(res, [1, 2, 3, 4], 'oops in test_opposite_addition_2')

    def test_subtraction_1(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem1 = [1, 0, 0, 0]
        elem2 = [1, 1, 0, 1]

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, [0, 1, 0, 1], 'oops in test_subtraction_1')

    def test_subtraction_2(self):
        f = Field(3, [2, 1, 0, 0, 1])
        elem1 = [1, 1, 2, 0]
        elem2 = [2, 0, 2, 1]

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, [2, 1, 0, 2], 'oops in test_subtraction_2')

    def test_multiplication_1(self):
        f = Field(2, [1, 1, 0, 1])
        elem1 = [0, 1, 1]
        elem2 = [0, 0, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [1, 0, 1], 'oops in  test_multiplication_1')

    def test_multiplication_2(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem1 = [0, 1, 0, 1]
        elem2 = [1, 1, 1, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in  test_multiplication_2')

    def test_multiplication_3(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        elem1 = [1, 0, 1, 0, 0, 1, 1, 1]
        elem2 = [1, 1, 1, 0, 1, 0, 1, 0]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 0, 1, 0, 0, 0, 1], 'oops in  test_multiplication_5')

    def test_multiplication_4(self):
        f = Field(3, [1, 2, 0, 1])
        elem1 = [0, 1, 2]
        elem2 = [2, 0, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [2, 1, 0], 'oops in  test_multiplication_4')

    def test_multiplication_5(self):
        f = Field(5, [2, 3, 0, 3])
        elem1 = [2, 3, 4]
        elem2 = [0, 1, 2]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 4], 'oops in  test_multiplication_5')

    def test_multiplication_6(self):
        f = Field(7, [2, 3, 0, 3])
        elem1 = [1, 5, 0]
        elem2 = [2, 3, 6]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [3, 4, 0], 'oops in  test_multiplication_6')

    def test_opposite_multiplication_1(self):
        f = Field(2, [1, 1, 0, 0, 1])
        elem = [0, 1, 0, 1]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_opposite_multiplication_1')

    def test_opposite_multiplication_2(self):
        f = Field(2, [1, 0, 1, 0, 0, 1])
        elem = [1, 1, 1, 1, 1]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [1, 1, 0, 1, 1], 'oops in test_opposite_multiplication_2')

    def test_opposite_multiplication_3(self):
        f = Field(5, [2, 3, 0, 3])
        elem = [2, 3, 4]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [2, 0, 4], 'oops in test_opposite_multiplication_3')

    def test_division_1(self):
        f = Field(2, [1, 1, 0, 0, 1])
        dividend = [1, 1, 1, 1]
        divisor = [0, 0, 1, 1]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_division_1')

    def test_division_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        dividend = [1, 0, 1, 0, 0, 1, 1, 0]
        divisor = [1, 1, 1, 0, 1, 0, 1, 1]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [1, 0, 1, 0, 1, 0, 1, 1], 'oops in test_division_2')

    def test_division_3(self):
        f = Field(3, [1, 2, 0, 1])
        dividend = [0, 1, 1]
        divisor = [1, 0, 2]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [2, 1, 1], 'oops in test_division_3')

    def test_to_int_1(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        elem = [1, 0, 1, 0, 0, 1, 1, 0]

        res = f.from_elem_to_int(elem)
        self.assertEqual(res, 101, 'oops in test_to_int_1')

    def test_to_int_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        elem = [0, 1, 1, 1, 1, 1, 1, 1]

        res = f.from_elem_to_int(elem)
        self.assertEqual(res, 254, 'oops in test_to_int_2')

    def test_from_int_1(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        number = 101

        res = f.from_int_to_elem(number)
        self.assertEqual(res, [1, 0, 1, 0, 0, 1, 1, 0], 'oops in test_from_int_1')

    def test_from_int_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        number = 257

        res = f.from_int_to_elem(number)
        self.assertEqual(res, [1, 0, 0, 0, 0, 0, 0, 0], 'oops in test_from_int_2')

    def test_to_bytes_1(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        elem = [1, 0, 1, 0, 0, 1, 1, 0]

        res = f.binary_field_to_bytes(elem)
        self.assertEqual(res, b'e', 'oops in test_to_bytes_1')

    def test_to_bytes_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        elem = [1, 1, 1, 1, 1, 1, 1, 1]

        res = f.binary_field_to_bytes(elem)
        self.assertEqual(res, b'\xff', 'oops in test_to_bytes_2')

    def test_from_bytes_1(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        byte_number = b'\n'

        res = f.binary_field_from_bytes(byte_number)
        self.assertEqual(res, [0, 1, 0, 1, 0, 0, 0, 0], 'oops in test_from_bytes_1')

    def test_from_bytes_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])
        byte_number = b'\r'

        res = f.binary_field_from_bytes(byte_number)
        self.assertEqual(res, [1, 0, 1, 1, 0, 0, 0, 0], 'oops in test_from_bytes_2')

    if __name__ == '__main__':
        unittest.main()


class PrimeFieldsTester(unittest.TestCase):

    def test_addition_1(self):
        f = PrimeField(2)
        elem1 = 1
        elem2 = 0

        res = f.addition(elem1, elem2)
        self.assertEqual(res, 1, 'oops in prime_field_test_addition_1')

    def test_addition_2(self):
        f = PrimeField(5)
        elem1 = 4
        elem2 = 3

        res = f.addition(elem1, elem2)
        self.assertEqual(res, 2, 'oops in prime_field_test_addition_2')

    def test_opposite_addition_1(self):
        f = PrimeField(5)
        elem = 4

        res = f.opposite_addition(elem)
        self.assertEqual(res, 1, 'oops in prime_field_test_opposite_addition_1')

    def test_subtraction_1(self):
        f = PrimeField(7)
        elem1 = 1
        elem2 = 6

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, 2, 'oops in prime_field_test_subtraction_1')

    def test_multiplication_1(self):
        f = PrimeField(5)
        elem1 = 3
        elem2 = 4

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, 2, 'oops in prime_field_test_multiplication_1')

    def test_multiplication_2(self):
        f = PrimeField(11)
        elem1 = 10
        elem2 = 9

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, 2, 'oops in prime_field_test_multiplication_2')

    def test_opposite_multiplication_1(self):
        f = PrimeField(7)
        elem = 5

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, 3, 'oops in prime_field_test_opposite_multiplication_1')

    def test_division_elem_1(self):
        f = PrimeField(11)
        dividend = 6
        divisor = 10

        res = f.division_elem(dividend, divisor)
        self.assertEqual(res, 5, 'oops in prime_field_test_division_elem_1')

    def test_division_poly_1(self):
        dividend = [1, 9, 6, 5, 3, 8, 12]
        divisor = [4, 1, 0, 1]

        res = PrimeField.division_poly(dividend, divisor, 13)
        self.assertEqual(res, [10, 5, 9], 'oops in prime_field_test_division_poly_1')

    def test_division_poly_2(self):
        dividend = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
        divisor = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]

        res = PrimeField.division_poly(dividend, divisor, 2)
        self.assertEqual(res, [1, 1, 0, 1, 1, 0, 1, 1, 0], 'oops in prime_field_test_division_poly_2')

    def test_is_norm_1(self):
        f = PrimeField(17)
        elem = 78

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in prime_field_test_is_norm_1')

    if __name__ == '__main__':
        unittest.main()


class RandomGeneratorTester(unittest.TestCase):

    def test_1(self):
        a = [[1] + [0] * 7, [0, 1] + [0] * 6]
        c = [0, 0, 1] + [0] * 5
        g = RandomGenerator(a, c)

        res = [g.generator() for _ in range(0, 5)]
        self.assertEqual(res, [b'\x00', b'\x00', b'\x04', b'\x0c', b'\x18'], 'oops in test_random_1')

    def test_2(self):
        a = [[0] * 8] * 5
        c = [0] * 8
        g = RandomGenerator(a, c)

        res = [g.generator() for _ in range(0, 15)]
        self.assertEqual(res, [b'\x00'] * 15, 'oops in test_random_2')

    def test_3(self):
        a = [[1] + [0] * 7] * 3
        c = [1] * 8
        g = RandomGenerator(a, c)

        res = [g.generator() for _ in range(0, 8)]
        self.assertEqual(res, [b'\x00', b'\x00', b'\x00', b'\xff', b'\x00', b'\x00', b'\x00', b'\xff'], 'oops in test_random_3')

    def test_4(self):
        a = [[1] + [0] * 7] * 5
        c = [1] + [0] * 7
        g = RandomGenerator(a, c)

        res = [g.generator() for _ in range(0, 7)]
        self.assertEqual(res, [b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x01', b'\x00'], 'oops in test_random_4')

    def test_5(self):
        a = [[1] + [0] * 7] * 7
        c = [0] * 8
        g = RandomGenerator(a, c)

        res = [g.generator() for _ in range(0, 25)]
        self.assertEqual(res, [b'\x00'] * 25, 'oops in test_random_5')

    if __name__ == '__main__':
        unittest.main()


