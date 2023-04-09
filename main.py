from field import Field
from simple_field import Simple_field

# Simple_field.div_poly([0, 1, 1, 1], [0, 2, 3], 5)
# Simple_field.div_poly([1, 1, 1, 1], [1, 1], 2)
# Simple_field.div_poly([4, 4, 4, 4], [1, 1, 1, 1], 5)

f1 = Field(2, [1, 1, 0, 1], 3)
print(f1.obrat([0, 1, 1]))

f2 = Simple_field(5)
print(f2.obrat(4))
# [1, 1, 0]


