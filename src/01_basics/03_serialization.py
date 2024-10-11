from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


# Two Instances
derek = Person(first_name="Derek", last_name="Bruckner", age=32)
newton = Person(first_name="Isaac", last_name="Newton", age=84)

print(newton.__dict__)

# Produce a Dictionary
newton.model_dump()  # Highly configurable
print(newton.model_dump(include=["last_name"]))
print(newton.model_dump(exclude=["first_name", "age"]))
# Produce a JSON string
newton.model_dump_json()
print(newton.model_dump_json(indent=2))
