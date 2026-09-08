from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name: str
    is_active: bool

# input_data = {
#     'id': 101,
#     "name": "CodeByPaxtos",
#     "is_active": 'True' # where pydantic can correct it, it will and where it cannot it will throw error
# }

input_data = {
    'id': 101,
    "name": "CodeByPaxtos",
    "is_active": True
}

user = User(**input_data)

print(user)