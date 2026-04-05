from pydantic import BaseModel, EmailStr, ValidationError, conint

class Person(BaseModel):
    name: str
    email: EmailStr          
    age: conint(gt=0, lt=120)  

examples = [
    {"name": "Ali", "email": "ali@example.com", "age": 25},
    {"name": "Sara", "email": "saraexample.com", "age": 30}, 
    {"name": "John", "email": "john@example.com", "age": -5}, 
]

for i, data in enumerate(examples, start=1):
    try:
        person = Person(**data)
        print(f"Exemple {i}: Validé -> {person}")
    except ValidationError as e:
        print(f"Exemple {i}: Erreur de validation")
        print(e)