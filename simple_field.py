
class Simple_field:
    def __init__(self, prost):
        self.prost = prost

    def obrat(self, elem):
        p = self.prost
        return (elem**(p - 2)) % p

    def multi_elem(self, elem1, elem2):
        p = self.prost
        return (elem1 * elem2) % p

    def plus(self, elem1, elem2):
        p = self.prost
        return (elem1 + elem2) % p

    def protiv(self, elem):
        p = self.prost
        if elem == 0:
            return 0
        else:
            return p - elem

    def minus(self, umensh, vych):
        return self.plus(umensh, self.protiv(vych))

    def div_elem(self, delimoe, delitel):
        p = self.prost
        x = self.obrat(delitel)
        while x < 0:
            x += p
        return self.multi_elem(delimoe, x)


    @staticmethod
    def div_poly(delimoe, delitel, p):
        sf = Simple_field(p)
        deg1 = len(delimoe) - 1
        deg2 = len(delitel) - 1
        while deg1 >= deg2:
            copy_delitel = [0]*(deg1 - deg2) + delitel

            c = sf.div_elem(delimoe[deg1], copy_delitel[deg1])
            v = [i * c for i in copy_delitel]

            delimoe = [sf.minus(delimoe[i], v[i]) for i in range(0, deg1 + 1)]
            delimoe.pop()
            deg1 = len(delimoe) - 1

        return delimoe




