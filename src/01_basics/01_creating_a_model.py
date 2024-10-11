from pydantic import BaseModel, ValidationError


# Creating a Pydantic Model
# This is just a Python class. You can add custom functions, etc - anything you can do with a class.
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


# Instance
p = Person(first_name="Derek", last_name="Bruckner", age=32)
print(str(p))
print(repr(p))
print(p.model_fields)

try:
    Person(last_name="test")
except ValidationError as exception:
    print(exception)


# Custom Properties
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


p = Person(first_name="Derek", last_name="Bruckner", age=32)
print(p.display_name)

try:
    Person(first_name="Derek", last_name="Bruckner", age="32")
except ValidationError as exception:
    print(exception)

# You can change values to the incorrect type
# This behavior can be configured to not allow it to occur
p.age = "thirty two"
print(p)
