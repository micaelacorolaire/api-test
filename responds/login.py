from pydantic import BaseModel,field

class login (BaseModel):
    id_login:str=field(...,min_length=1)
    user_email:str=field(...,min_length=1)
    user_password:str=field(...,min_length=1)