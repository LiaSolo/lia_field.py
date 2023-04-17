from simple_field import SimpleField


class Field:

    def __init__(self, simple_number, factor_polynom, degree):
        self.simple_number = simple_number
        self.factor_polynom = factor_polynom
        self.degree = degree

    def opposite_multiplication(self, elem):
        p = self.simple_number
        n = self.degree

        if not self.is_norm_elem(elem) or sum(elem) == 0:
            raise Exception("Wrong element(s)!!!")
        else:
            d = p ** n - 2
            result = elem
            for i in range(1, d):
                result = self.multiplication(result, elem)

            return result

    def is_norm_elem(self, elem):
        p = self.simple_number
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
        p = self.simple_number
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
        p = self.simple_number
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
        p = self.simple_number
        q = self.factor_polynom

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            raise Exception("Wrong element(s)!!!")
        else:
            deg1 = len(elem1) - 1
            deg2 = len(elem2) - 1
            answer = [0 for _ in range(0, deg1 + deg2 + 1)]

            for x in range(0, deg1 + 1):
                for y in range(0, deg2 + 1):
                    answer[x + y] += elem1[x] * elem2[y]

            answer = [i % p for i in answer]
            result = SimpleField.division_modulo(answer, q, p)
            return result

    def division(self, dividend, divisor):
        if not (self.is_norm_elem(dividend) and self.is_norm_elem(divisor)):
            raise Exception("Wrong element(s)!!!")
        else:
            return self.multiplication(dividend, self.opposite_multiplication(divisor))

    def zero(self):
        n = self.degree
        return [0 for _ in range(0, n)]

    def one(self):
        n = self.degree
        return [1] + [0 for _ in range(0, n - 1)]

    def binary_field_to_bytes(self, elem):
        p = self.simple_number

        if p != 2:
            raise Exception("Wrong element(s)!!!")
        else:
            return bytes(elem)

    def binary_field_from_bytes(self, byte_seq):
        p = self.simple_number

        if p != 2:
            raise Exception("Wrong element(s)!!!")
        else:
            return list(byte_seq)
