from time import time
from pydantic import BaseModel, ValidationError


class Circle(BaseModel):
    center: tuple[int, int]
    radius: int


print(Circle.model_fields)  # Both are required


class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int


print(
    Circle.model_fields
)  # 'center': FieldInfo(annotation=tuple[int, int], required=False, default=(0, 0))
Circle(radius=1)

data = {"radius": 1}
data_json = """
{
    "radius": 1
}
"""

Circle.model_validate(data)
Circle.model_validate_json(data_json)

Circle(center=(1, 1), radius=2)

# Must be careful when providing a default
c = Circle(radius=2)
c.center = "junk"  # Pydantic doesn't stop this. We must configure


# Pydantic also doesn't validate the default value. It trusts the dev by default
class Circle(BaseModel):
    center: tuple[int, int] = "junk"
    radius: int


c = Circle(radius=2)
print(c)


def extend_list(_list: list = []) -> list[int]:
    _list.append(int(time()))
    return _list


my_times = extend_list()
print(my_times)  # A single value

my_new_times = extend_list()
print(
    my_new_times
)  # holds two values now. This is a problem for when you define a default, or it can be.
# The list gets added at compile time, which causes the function state to become persistent / modified.


class Model(BaseModel):
    my_list: list[
        int
    ] = []  # Valid in pydantic. There is no shared list between instances. A new instance is made everytime.
