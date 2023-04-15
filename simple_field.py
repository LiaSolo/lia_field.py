
class Simple_field:
    def __init__(self, prost):
        self.prost = prost

    def is_norm_elem(self, elem):
        p = self.prost

        flag = True

        if elem >= p:
            flag = False

        return flag

    def obrat(self, elem):
        p = self.prost
        if elem == 0 or not self.is_norm_elem(elem):
            print('пошел ты с такими элементами...')

        else:
            return (elem**(p - 2)) % p

    def multi_elem(self, elem1, elem2):
        p = self.prost
        if not self.is_norm_elem(elem1) or not self.is_norm_elem(elem2):
            print('пошел ты с такими элементами...')

        else:
            return (elem1 * elem2) % p

    def plus(self, elem1, elem2):
        p = self.prost
        if not self.is_norm_elem(elem1): # or not self.is_norm_elem(elem2):
            print('пошел ты с такими элементами...')
        else:
            return (elem1 + elem2) % p

    def protiv(self, elem):
        p = self.prost
        if not self.is_norm_elem(elem):
            print('пошел ты с такими элементами...')
        elif elem == 0:
            return 0
        else:
            return p - elem

    def minus(self, umensh, vych):
        if not (self.is_norm_elem(umensh) and self.is_norm_elem(vych)):
            print('пошел ты с такими элементами...')
        else:
            return self.plus(umensh, self.protiv(vych))

    def div_elem(self, delimoe, delitel):
        p = self.prost

        if not (self.is_norm_elem(delimoe) and self.is_norm_elem(delitel)) or delitel == 0:
            print('пошел ты с такими элементами...')
        else:
            return self.multi_elem(delimoe, self.obrat(delitel))


    @staticmethod
    def div_poly(delimoe, delitel, p):
        sf = Simple_field(p)
        deg1 = len(delimoe) - 1
        deg2 = len(delitel) - 1
        while deg1 >= deg2:
            copy_delitel = [0]*(deg1 - deg2) + delitel

            c = sf.div_elem(delimoe[deg1], copy_delitel[deg1])
            v = [(i * c) % p for i in copy_delitel]

            delimoe = [sf.minus(delimoe[i], v[i]) for i in range(0, deg1 + 1)]
            delimoe.pop()
            deg1 = len(delimoe) - 1

        return delimoe

    def binary_field_to_bytes(self, elem):
        p = self.prost

        if p != 2:
            print('пошел ты с такими элементами...')
        else:
            return int.to_bytes(elem)


    def binary_field_from_bytes(self, byte_seq):
        p = self.prost

        if p != 2:
            print('пошел ты с такими элементами...')
        else:
            return int.from_bytes(byte_seq)






