from field import Field
from simple_field import Simple_field

# Simple_field.div_poly([0, 1, 1, 1], [0, 2, 3], 5)
# Simple_field.div_poly([1, 1, 1, 1], [1, 1], 2)
# Simple_field.div_poly([4, 4, 4, 4], [1, 1, 1, 1], 5)

f1 = Field(2, [1, 1, 1], 2)
# print(f.minus([1, 1], [1, 0]))
# print(f.protiv([1, 0]))


r1 = f1.binary_field_to_bytes([1, 1])
print(r1, f1.binary_field_from_bytes(r1))

f2 = Field(2, [1, 0, 1, 0, 0, 1], 5)
r2 = f2.binary_field_to_bytes([1, 1, 0, 1, 1])
print(r2, f2.binary_field_from_bytes(r2))

f3 = Field(3,  [1, 2, 0, 1], 3)
r3 = f3.binary_field_to_bytes([2, 1, 1])
print(r3, f3.binary_field_from_bytes(r3))

f4 = Simple_field(2)
r4 = f4.binary_field_to_bytes(1)
print(r4, f4.binary_field_from_bytes(r4))


# f = Field(2, [1, 1, 0, 0, 1], 4)
# a = f.obrat([0, 0, 1, 1])
# print(f.multi([1, 1, 1, 1], a))
#
# f = Field(2, [1, 0, 1, 1, 1, 0, 0, 0, 1], 8)
# a = f.obrat([1, 1, 1, 0, 1, 0, 1, 1])
# print(f.multi([1, 0, 1, 0, 0, 1, 1, 0], a))
#
# f = Field(3, [1, 2, 0, 1], 3)
# a = f.obrat([1, 0, 2])
# print(f.multi([0, 1, 1], a))


