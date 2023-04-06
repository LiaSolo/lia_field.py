

class Field:

    @staticmethod
    def euclid(elem1, elem2):
        if elem1 == 0:
            return 0, 1
        else:
           x, y = Field.euclid(elem2 % elem1, elem1)
        return y - x * (elem2 // elem1), x

    @staticmethod
    def is_norm_elem(prost, stepen, elem1):
        flag = True
        for e in elem1:
            if e >= prost:
                flag = False
        if len(elem1) != stepen:
            flag = False
        return flag

    @staticmethod
    def plus(prost, stepen, elem1, elem2):

        if not (Field.is_norm_elem(prost, stepen, elem1) and  Field.is_norm_elem(prost, stepen, elem2)):
            print('пошел н**** с такими элементами')
        else:
            sum_elem = list()
            for i in range(0, stepen):
                sum_elem.append((elem1[i] + elem2[i]) % prost)
            print(sum_elem)

    @staticmethod
    def minus(prost, stepen, elem1, elem2):
        if not (Field.is_norm_elem(prost, stepen, elem1) and Field.is_norm_elem(prost, stepen, elem2)):
            print('пошел н**** с такими элементами')
        else:
            sum_elem = list()
            for i in range(0, stepen):
                sum_elem.append((elem1[i] - elem2[i]) % prost)
            print(sum_elem)

    @staticmethod
    def obrat(prost, stepen, elem):
        obr_elem = list()
        for i in range(0, stepen):
            x, y = Field.euclid(elem[i], prost)
            while x <= 0:
                x += prost
            obr_elem.append(x)
        print(obr_elem)
        return obr_elem

    @staticmethod
    def protiv(prost, stepen, elem):
        print()

    @staticmethod
    def multi(prost, stepen, elem1, elem2):
        print()

    @staticmethod
    def div(prost, stepen, elem1, elem2):
        print()

    @staticmethod
    def make_zero():
        print()

    @staticmethod
    def make_one():
        print()




