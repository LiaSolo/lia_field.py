from simple_field import PrimeField


class Field:

    def __init__(self, prime_number, factor_polynom):
        self.prime_number = prime_number
        self.factor_polynom = factor_polynom
        self.degree = len(factor_polynom) - 1

    def fast_power(self, base, exp):
        if exp == 0:
            return self.one()
        temp = self.fast_power(base, int(exp / 2))
        temp = self.multiplication(temp, temp)

        if exp % 2 == 0:
            return temp
        else:
            return self.multiplication(base, temp)

    def opposite_multiplication(self, elem):
        p = self.prime_number
        n = self.degree

        if not self.is_norm_elem(elem) or sum(elem) == 0:
            raise Exception("Wrong element(s)!!!💔")
        else:
            d = pow(p, n) - 2
            result = self.fast_power(elem, d)

            return result

    def is_norm_elem(self, elem):
        p = self.prime_number
        n = self.degree

        flag = True
        for e in elem:
            if e >= p:
                flag = False
                break
        if len(elem) != n:
            flag = False
        return flag

    def addition(self, elem1, elem2):
        p = self.prime_number
        n = self.degree

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            raise Exception("Wrong element(s)!!!")
        else:
            answer = list()
            for i in range(0, n):
                answer.append((elem1[i] + elem2[i]) % p)

            return answer

    def subtraction(self, minuend, subtrahend):
        if not (self.is_norm_elem(minuend) and self.is_norm_elem(subtrahend)):
            raise Exception("Wrong element(s)!!!")
        else:
            return self.addition(minuend, self.opposite_addition(subtrahend))

    def opposite_addition(self, elem):
        p = self.prime_number
        n = self.degree

        if not self.is_norm_elem(elem):
            raise Exception("Wrong element(s)!!!")
        else:
            answer = list()
            for i in range(0, n):
                if elem[i] == 0:
                    answer.append(0)
                else:
                    answer.append(p - elem[i])
            return answer

    def multiplication(self, elem1, elem2):
        p = self.prime_number
        q = self.factor_polynom

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            raise Exception("Wrong element(s)!!!💔")
        else:
            deg1 = len(elem1) - 1
            deg2 = len(elem2) - 1
            answer = [0 for _ in range(0, deg1 + deg2 + 1)]

            for x in range(0, deg1 + 1):
                for y in range(0, deg2 + 1):
                    answer[x + y] += elem1[x] * elem2[y]

            answer = [i % p for i in answer]
            result = PrimeField.division_poly(answer, q, p)
            return result

    def division(self, dividend, divisor):
        if not (self.is_norm_elem(dividend) and self.is_norm_elem(divisor)):
            raise Exception("Wrong element(s)!!!💔")
        else:
            return self.multiplication(dividend, self.opposite_multiplication(divisor))

    def zero(self):
        n = self.degree
        return [0 for _ in range(0, n)]

    def one(self):
        n = self.degree
        return [1] + [0 for _ in range(0, n - 1)]

    def binary_field_to_bytes(self, elem):
        p = self.prime_number

        if p != 2:
            raise Exception("Wrong element(s)!!!💔")
        else:
            number = self.from_elem_to_int(elem)
            byte_number = number.to_bytes(1)
            return byte_number

    def binary_field_from_bytes(self, byte_number):
        p = self.prime_number

        if p != 2:
            raise Exception("Wrong element(s)!!!💔")
        else:
            number = int.from_bytes(byte_number)
            return self.from_int_to_elem(number)

    def from_elem_to_int(self, elem):
        p = self.prime_number
        length = len(elem)
        number = 0
        coef = 1
        for i in range(0, length):
            number += elem[i] * coef
            coef *= p

        return number

    def from_int_to_elem(self, number):
        p = self.prime_number
        d = self.degree
        elem = list()
        while number // p > 0:
            elem.append(number % p)
            number //= p

        elem.append(number % p)
        while len(elem) < d:
            elem.append(0)
        while len(elem) > d:
            elem.pop()
        return elem
