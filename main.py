from field import Field
from simple_field import SimpleField

f1 = Field(2, [1, 1, 1], 2)
print(f1.opposite_multiplication([1, 3]))

#
# r1 = f1.binary_field_to_bytes([1, 1])
# print(r1, f1.binary_field_from_bytes(r1))
#
# f2 = Field(2, [1, 0, 1, 0, 0, 1], 5)
# r2 = f2.binary_field_to_bytes([1, 1, 0, 1, 1])
# print(r2, f2.binary_field_from_bytes(r2))
#
# f3 = Field(3,  [1, 2, 0, 1], 3)
# r3 = f3.binary_field_to_bytes([2, 1, 1])
# print(r3, f3.binary_field_from_bytes(r3))
#
# f4 = SimpleField(2)
# r4 = f4.binary_field_to_bytes(1)
# print(r4, f4.binary_field_from_bytes(r4))
