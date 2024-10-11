from pydantic import BaseModel, ValidationError


class Coordinate(BaseModel):
    x: float
    y: float


p1 = Coordinate(x=1.1, y=2.2)
print(p1)
print(Coordinate.model_fields)

p2 = Coordinate(x=0, y="1.2")
print(p2)
print(type(p2.x), type(p2.y))  # Pydantic switched the values to floats for us


class Model(BaseModel):
    field: str


Model(field="Python")

try:
    Model(field=100)
except ValidationError as exception:
    print(exception)


class Contact(BaseModel):
    email: str


init_json_data = """
{
    "email": "example@domain.net"
}
"""

Contact.model_validate_json(init_json_data)

new_json_data = """
{
    "email": {
        "personal": "someone@something.com",
        "work": "someone@work.edu"
    }
}
"""
try:
    Contact.model_validate_json(new_json_data)
except ValidationError as exception:
    print(exception)

new_data = {"email": {"personal": "someone@something.com", "work": "someone@work.edu"}}

# No Validation Error...because the value comes in as a string which doesn't coerce
print(Contact(email=str(new_data["email"])))
