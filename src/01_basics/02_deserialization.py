from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p = Person(first_name="Isaac", last_name="Newton", age=84)

# Dictionary Format
data = {"first_name": "Isaac", "last_name": "Newton", "age": 84}

# This works, but becomes less useful for complex objects / dicts
Person(**data)

# This is the better approach
p = Person.model_validate(data)

incorrect = {"last_name": "Newton"}
try:
    Person.model_validate(incorrect)
except ValidationError as exception:
    print(exception)

# JSON Format
data_json = """
{
    "first_name": "Isaac",
    "last_name": "Newton", 
    "age": 84
}
"""
p = Person.model_validate_json(data_json)
print(p)

data_json_incorrect = """
{
    "first_name": "Isaac",
    "age": 84
}
"""
try:
    Person.model_validate_json(data_json_incorrect)
except ValidationError as exception:
    print(exception)
