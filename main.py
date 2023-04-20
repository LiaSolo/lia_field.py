from field import Field


class RandomGenerator:
    def __init__(self, a, c):
        self.a = a
        self.k = len(a)
        self.c = c
        self.x = [[0] * 8] * self.k
        self.field = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1])

    def generator(self):
        result = self.c
        a = self.a
        f = self.field
        k = self.k
        x = self.x

        for i in range(0, k):
            temp = f.multiplication(a[i], x[i])
            result = f.addition(temp, result)

        answer = x.pop(0)
        x += [result]
        return f.binary_field_to_bytes(answer)


