
class SimpleField:
    def __init__(self, simple_number):
        self.simple_number = simple_number

    def is_norm_elem(self, elem):
        p = self.simple_number

        flag = True

        if elem >= p:
            flag = False

        return flag

    def opposite_multiplication(self, elem):
        p = self.simple_number
        if elem == 0 or not self.is_norm_elem(elem):
            raise Exception("Wrong element(s)!!!")

        else:
            return (elem**(p - 2)) % p

    def multiplication(self, elem1, elem2):
        p = self.simple_number
        if not self.is_norm_elem(elem1) or not self.is_norm_elem(elem2):
            raise Exception("Wrong element(s)!!!")

        else:
            return (elem1 * elem2) % p

    def addition(self, elem1, elem2):
        p = self.simple_number
        if not self.is_norm_elem(elem1) or not self.is_norm_elem(elem2):
            raise Exception("Wrong element(s)!!!")
        else:
            return (elem1 + elem2) % p

    def opposite_addition(self, elem):
        p = self.simple_number
        if not self.is_norm_elem(elem):
            raise Exception("Wrong element(s)!!!")
        elif elem == 0:
            return 0
        else:
            return p - elem

    def subtraction(self, minuend, subtrahend):
        if not (self.is_norm_elem(minuend) and self.is_norm_elem(subtrahend)):
            raise Exception("Wrong element(s)!!!")
        else:
            return self.addition(minuend, self.opposite_addition(subtrahend))

    def division_elem(self, dividend, divisor):

        if not (self.is_norm_elem(dividend) and self.is_norm_elem(divisor)) or divisor == 0:
            raise Exception("Wrong element(s)!!!")
        else:
            return self.multiplication(dividend, self.opposite_multiplication(divisor))

    @staticmethod
    def division_modulo(dividend, divisor, p):
        sf = SimpleField(p)
        deg1 = len(dividend) - 1
        deg2 = len(divisor) - 1
        while deg1 >= deg2:
            copy_divisor = [0]*(deg1 - deg2) + divisor

            c = sf.division_elem(dividend[deg1], copy_divisor[deg1])
            v = [(i * c) % p for i in copy_divisor]

            dividend = [sf.subtraction(dividend[i], v[i]) for i in range(0, deg1 + 1)]
            dividend.pop()
            deg1 = len(dividend) - 1

        return dividend

    def binary_field_to_bytes(self, elem):
        p = self.simple_number

        if p != 2:
            raise Exception("Wrong element(s)!!!")
        else:
            return int.to_bytes(elem)

    def binary_field_from_bytes(self, byte_seq):
        p = self.simple_number

        if p != 2:
            raise Exception("Wrong element(s)!!!")
        else:
            return int.from_bytes(byte_seq)
