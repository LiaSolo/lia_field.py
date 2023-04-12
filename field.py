from simple_field import Simple_field


class Field:

    def __init__(self, prost, factor, stepen):
        self.prost = prost
        self.factor = factor
        self.stepen = stepen

    def obrat(self, elem):
        p = self.prost
        n = self.stepen

        if not self.is_norm_elem(elem) or sum(elem) == 0:
            print('пошел ты с такими элементами...')
        else:
            d = p ** n - 2
            result = elem
            for i in range(1, d):
                result = self.multi(result, elem)

            return result

    def is_norm_elem(self, elem):
        p = self.prost
        n = self.stepen

        flag = True
        for e in elem:
            if e >= p:
                flag = False
                break
        if len(elem) != n:
            flag = False
        return flag

    def plus(self, elem1, elem2):
        p = self.prost
        n = self.stepen

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            print('пошел ты с такими элементами...')
        else:
            sum_elem = list()
            for i in range(0, n):
                sum_elem.append((elem1[i] + elem2[i]) % p)

            return sum_elem

    def minus(self, elem1, elem2):
        p = self.prost
        n = self.stepen

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            print('пошел ты с такими элементами...')
        else:
            return self.plus(elem1, self.protiv(elem2))

    def protiv(self, elem):
        p = self.prost
        n = self.stepen

        if not self.is_norm_elem(elem):
            print('пошел ты с такими элементами...')
        else:
            protiv_elem = list()
            for i in range(0, n):
                if elem[i] == 0:
                    protiv_elem.append(0)
                else:
                    protiv_elem.append(p - elem[i])
            return protiv_elem

    def multi(self, elem1, elem2):
        p = self.prost
        q = self.factor

        if not (self.is_norm_elem(elem1) and self.is_norm_elem(elem2)):
            print('пошел ты с такими элементами...')
        else:
            deg1 = len(elem1) - 1
            deg2 = len(elem2) - 1
            mult_elem = [0 for i in range(0, deg1 + deg2 + 1)]

            for x in range(0, deg1 + 1):
                for y in range(0, deg2 + 1):
                    mult_elem[x + y] += elem1[x] * elem2[y]

            mult_elem = [i % p for i in mult_elem]
            result = Simple_field.div_poly(mult_elem, q, p)
            return result

    def div(self, delimoe, delitel):
        if not (self.is_norm_elem(delimoe) and self.is_norm_elem(delitel)):
            print('пошел ты с такими элементами...')
        else:
            return self.multi(delimoe, self.obrat(delitel))

    def zero(self):
        n = self.stepen
        return [0 for i in range(0, n)]

    def one(self):
        n = self.stepen
        return [1] + [0 for i in range(0, n - 1)]

    def binary_field_to_bytes(self, elem):
        p = self.prost
        n = self.stepen

        if p != 2:
            print('пошел ты с такими элементами...')
        else:
            return bytes(elem)

    def binary_field_from_bytes(self, byte_seq):
        p = self.prost
        n = self.stepen

        if p != 2:
            print('пошел ты с такими элементами...')
        else:
            return list(byte_seq)