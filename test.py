import unittest
from field import Field
from simple_field import Simple_field


class Fields_tester(unittest.TestCase):

    def test_plus_1(self):
        f = Field(2, [1, 1, 1], 2)
        elem1 = [0, 1]
        elem2 = [1, 1]

        res = f.plus(elem1, elem2)
        self.assertEqual(res, [1, 0], 'oops in test_plus_1')

    def test_plus_2(self):
        f = Field(3, [1, 2, 0, 1], 3)
        elem1 = [2, 1, 1]
        elem2 = [2, 2, 1]

        res = f.plus(elem1, elem2)
        self.assertEqual(res, [1, 0, 2], 'oops in test_plus_2')

    def test_plus_3(self):
        f = Field(5, [2, 3, 0, 1], 3)
        elem1 = [4, 4, 1]
        elem2 = [3, 2, 0]

        res = f.plus(elem1, elem2)
        self.assertEqual(res, [2, 1, 1], 'oops in test_plus_3')

    def test_plus_4(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [0, 1, 1, 1]
        elem2 = [1, 0, 1, 0]

        res = f.plus(elem1, elem2)
        self.assertEqual(res, [1, 1, 0, 1], 'oops in test_plus_4')

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

    def test_protiv_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 1, 1]

        res = f.protiv(elem)
        self.assertEqual(res, [0, 1, 1, 1], 'oops in test_protiv_1')

    def test_protiv_2(self):
        f = Field(5, [2, 2, 1, 0, 1], 4)
        elem = [4, 3, 2, 1]

        res = f.protiv(elem)
        self.assertEqual(res, [1, 2, 3, 4], 'oops in test_protiv_2')

    def test_minus_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [1, 0, 0, 0]
        elem2 = [1, 1, 0, 1]

        res = f.minus(elem1, elem2)
        self.assertEqual(res, [0, 1, 0, 1], 'oops in test_minus_1')

    def test_minus_2(self):
        f = Field(3, [2, 1, 0, 0, 1], 4)
        elem1 = [1, 1, 2, 0]
        elem2 = [2, 0, 2, 1]

        res = f.minus(elem1, elem2)
        self.assertEqual(res, [2, 1, 0, 2], 'oops in test_minus_2')

    def test_multi_1(self):
        f = Field(2, [1, 1, 0, 1], 3)
        elem1 = [0, 1, 1]
        elem2 = [0, 0, 1]

        res = f.multi(elem1, elem2)
        self.assertEqual(res,[1, 0, 1], 'oops in test_multi_1')

    def test_multi_2(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem1 = [0, 1, 0, 1]
        elem2 = [1, 1, 1, 1]

        res = f.multi(elem1, elem2)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_multi_2')

    def test_multi_3(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1], 8)
        elem1 = [1, 0, 1, 0, 0, 1, 1, 1]
        elem2 = [1, 1, 1, 0, 1, 0, 1, 0]

        res = f.multi(elem1, elem2)
        self.assertEqual(res, [0, 0, 0, 1, 0, 0, 0, 1], 'oops in test_multi_3')

    def test_multi_4(self):
        f = Field(3, [1, 2, 0, 1], 3)
        elem1 = [0, 1, 2]
        elem2 = [2, 0, 1]

        res = f.multi(elem1, elem2)
        self.assertEqual(res, [2, 1, 0], 'oops in test_multi_4')

    def test_multi_5(self):
        f = Field(5, [2, 3, 0, 3], 3)
        elem1 = [2, 3, 4]
        elem2 = [0, 1, 2]

        res = f.multi(elem1, elem2)
        self.assertEqual(res, [0, 0, 4], 'oops in test_multi_5')

    def test_multi_6(self):
        f = Field(7, [2, 3, 0, 3], 3)
        elem1 = [1, 5, 0]
        elem2 = [2, 3, 6]

        res = f.multi(elem1, elem2)
        self.assertEqual(res, [3, 4, 0], 'oops in test_multi_6')

    def test_obrat_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        elem = [0, 1, 0, 1]

        res = f.obrat(elem)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_obrat_1')

    def test_obrat_2(self):
        f = Field(2, [1, 0, 1, 0, 0, 1], 5)
        elem = [1, 1, 1, 1, 1]

        res = f.obrat(elem)
        self.assertEqual(res, [1, 1, 0, 1, 1], 'oops in test_obrat_2')
    def test_obrat_3(self):
        f = Field(5, [2, 3, 0, 3], 3)
        elem = [2, 3, 4]

        res = f.obrat(elem)
        self.assertEqual(res, [2, 0, 4], 'oops in test_obrat_3')

    def test_div_1(self):
        f = Field(2, [1, 1, 0, 0, 1], 4)
        delimoe = [1, 1, 1, 1]
        delitel = [0, 0, 1, 1]

        res = f.div(delimoe, delitel)
        self.assertEqual(res, [0, 0, 1, 1], 'oops in test_div_1')

    def test_div_2(self):
        f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1], 8)
        delimoe = [1, 0, 1, 0, 0, 1, 1, 0]
        delitel = [1, 1, 1, 0, 1, 0, 1, 1]

        res = f.div(delimoe, delitel)
        self.assertEqual(res, [1, 0, 1, 0, 1, 0, 1, 1], 'oops in test_div_2')

    def test_div_3(self):
        f = Field(3, [1, 2, 0, 1], 3)
        delimoe = [0, 1, 1]
        delitel = [1, 0, 2]

        res = f.div(delimoe, delitel)
        self.assertEqual(res, [2, 1, 1], 'oops in test_div_3')


class Simple_fields_tester(unittest.TestCase):

    def test_plus_1(self):
        f = Simple_field(2)
        elem1 = 1
        elem2 = 0

        res = f.plus(elem1, elem2)
        self.assertEqual(res, 1, 'oops in simple_field_test_plus_1')

    def test_plus_2(self):
        f = Simple_field(5)
        elem1 = 4
        elem2 = 3

        res = f.plus(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_plus_2')

    def test_protiv_1(self):
        f = Simple_field(5)
        elem = 4

        res = f.protiv(elem)
        self.assertEqual(res, 1, 'oops in simple_field_test_protiv_1')

    def test_minus_1(self):
        f = Simple_field(7)
        elem1 = 1
        elem2 = 6

        res = f.minus(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_minus_1')

    def test_multi_1(self):
        f = Simple_field(5)
        elem1 = 3
        elem2 = 4

        res = f.multi_elem(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_multi_1')

    def test_multi_2(self):
        f = Simple_field(11)
        elem1 = 10
        elem2 = 9

        res = f.multi_elem(elem1, elem2)
        self.assertEqual(res, 2, 'oops in simple_field_test_multi_2')

    def test_obrat_1(self):
        f = Simple_field(7)
        elem = 5

        res = f.obrat(elem)
        self.assertEqual(res, 3, 'oops in simple_field_test_obrat_1')

    def test_div_elem_1(self):
        f = Simple_field(11)
        delimoe = 6
        delitel = 10

        res = f.div_elem(delimoe, delitel)
        self.assertEqual(res, 5, 'oops in simple_field_test_div_elem_1')

    # def test_div_poly_1(self):
    #
    # def test_div_poly_2(self):

    def test_is_norm_1(self):
        f = Simple_field(17)
        elem = 78

        res = f.is_norm_elem(elem)
        self.assertEqual(res, False, 'oops in simple_field_test_is_norm_1')








