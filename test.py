import unittest
from field import Field
from simple_field import SimpleField


class FieldsTester(unittest.TestCase):

    def test_addition_1(self):
        f = Field(2, [1, 1, 1], 2)
        elem1 = [0, 1]
        elem2 = [1, 1]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 0], 'oops in test_addition_1')

    def test_addition_2(self):
        f = Field(3, [1, 2, 0, 1], 3)
        elem1 = [2, 1, 1]
        elem2 = [2, 2, 1]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 0, 2], 'oops in test_addition_2')

    def test_addition_3(self):
        f = Field(5, [2, 3, 0, 1], 3)
        elem1 = [4, 4, 1]
        elem2 = [3, 2, 0]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [2, 1, 1], 'oops in test_additions_3')

    def test_addition_4(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [0, 1, 1, 1]
        elem2 = [1, 0, 1, 0]

        res = f.addition(elem1, elem2)
        self.assertEqual(res, [1, 1, 0, 1], 'oops in test_addition_4')

    def test_is_norm_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 1, 2]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in test_is_norm_1')

    def test_is_norm_2(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 0, 1]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, True, 'oops in test_is_norm_2')

    def test_is_norm_3(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 1]

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in  test_is_norm_3')

    def test_opposite_addition_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 1, 1]

        res = f.opposite_addition(elem)
        self.assertEqual(res, [0, 1, 1, 1], 'oops in test_opposite_addition_1')

    def test_opposite_addition_2(self):
        f = Field(5, [2, 2, 1, 0, 1], 4)
        elem = [4, 3, 2, 1]

        res = f.opposite_addition(elem)
        self.assertEqual(res, [1, 2, 3, 4], 'oops in test_opposite_addition_2')

    def test_subtraction_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [1, 0, 0, 0]
        elem2 = [1, 1, 0, 1]

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, [0, 1, 0, 1], 'oops in test_subtraction_1')

    def test_subtraction_2(self):
        f = Field(3, [2, 1, 0, 0, 1], 4)
        elem1 = [1, 1, 2, 0]
        elem2 = [2, 0, 2, 1]

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, [2, 1, 0, 2], 'oops in test_subtraction_2')

    def test_multiplication_1(self):
        f = Field(2, [1, 1, 0, 1], 3)
        elem1 = [0, 1, 1]
        elem2 = [0, 0, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [1, 0, 1], 'oops in  test_multiplication_1')

    def test_multiplication_2(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [0, 1, 0, 1]
        elem2 = [1, 1, 1, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in  test_multiplication_2')

    def test_multiplication_3(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1], 8)
        elem1 = [1, 0, 1, 0, 0, 1, 1, 1]
        elem2 = [1, 1, 1, 0, 1, 0, 1, 0]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 0, 1, 0, 0, 0, 1], 'oops in  test_multiplication_5')

    def test_multiplication_4(self):
        f = Field(3, [1, 2, 0, 1], 3)
        elem1 = [0, 1, 2]
        elem2 = [2, 0, 1]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [2, 1, 0], 'oops in  test_multiplication_4')

    def test_multiplication_5(self):
        f = Field(5, [2, 3, 0, 3], 3)
        elem1 = [2, 3, 4]
        elem2 = [0, 1, 2]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [0, 0, 4], 'oops in  test_multiplication_5')

    def test_multiplication_6(self):
        f = Field(7, [2, 3, 0, 3], 3)
        elem1 = [1, 5, 0]
        elem2 = [2, 3, 6]

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, [3, 4, 0], 'oops in  test_multiplication_6')

    def test_opposite_multiplication_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 0, 1]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_opposite_multiplication_1')

    def test_opposite_multiplication_2(self):
        f = Field(2, [1, 0, 1, 0, 0, 1], 5)
        elem = [1, 1, 1, 1, 1]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [1, 1, 0, 1, 1], 'oops in test_opposite_multiplication_2')

    def test_opposite_multiplication_3(self):
        f = Field(5, [2, 3, 0, 3], 3)
        elem = [2, 3, 4]

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, [2, 0, 4], 'oops in test_opposite_multiplication_3')

    def test_division_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        dividend = [1, 1, 1, 1]
        divisor = [0, 0, 1, 1]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_division_1')

    def test_division_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1], 8)
        dividend = [1, 0, 1, 0, 0, 1, 1, 0]
        divisor = [1, 1, 1, 0, 1, 0, 1, 1]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [1, 0, 1, 0, 1, 0, 1, 1], 'oops in test_division_2')

    def test_division_3(self):
        f = Field(3, [1, 2, 0, 1], 3)
        dividend = [0, 1, 1]
        divisor = [1, 0, 2]

        res = f.division(dividend, divisor)
        self.assertEqual(res, [2, 1, 1], 'oops in test_division_3')


class SimpleFieldsTester(unittest.TestCase):

    def test_addition_1(self):
        f = SimpleField(2)
        elem1 = 1
        elem2 = 0

        res = f.addition(elem1, elem2)
        self.assertEqual(res, 1, 'oops in simple_field_test_addition_1')

    def test_addition_2(self):
        f = SimpleField(5)
        elem1 = 4
        elem2 = 3

        res = f.addition(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_addition_2')

    def test_opposite_addition_1(self):
        f = SimpleField(5)
        elem = 4

        res = f.opposite_addition(elem)
        self.assertEqual(res, 1, 'oops in simple_field_test_opposite_addition_1')

    def test_subtraction_1(self):
        f = SimpleField(7)
        elem1 = 1
        elem2 = 6

        res = f.subtraction(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_subtraction_1')

    def test_multiplication_1(self):
        f = SimpleField(5)
        elem1 = 3
        elem2 = 4

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_multiplication_1')

    def test_multiplication_2(self):
        f = SimpleField(11)
        elem1 = 10
        elem2 = 9

        res = f.multiplication(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_multiplication_2')

    def test_opposite_multiplication_1(self):
        f = SimpleField(7)
        elem = 5

        res = f.opposite_multiplication(elem)
        self.assertEqual(res, 3, 'oops in simple_field_test_opposite_multiplication_1')

    def test_division_elem_1(self):
        f = SimpleField(11)
        dividend = 6
        divisor = 10

        res = f.division_elem(dividend, divisor)
        self.assertEqual(res, 5, 'oops in simple_field_test_division_elem_1')

    def test_division_modulo_1(self):
        dividend = [1, 9, 6, 5, 3, 8, 12]
        divisor = [4, 1, 0, 1]

        res = SimpleField.division_modulo(dividend, divisor, 13)
        self.assertEqual(res, [10, 5, 9], 'oops in simple_field_test_division_modulo_1')

    def test_division_modulo_2(self):
        dividend = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
        divisor = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]

        res = SimpleField.division_modulo(dividend, divisor, 2)
        self.assertEqual(res, [1, 1, 0, 1, 1, 0, 1, 1, 0], 'oops in simple_field_test_division_modulo_2')

    def test_is_norm_1(self):
        f = SimpleField(17)
        elem = 78

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in simple_field_test_is_norm_1')
