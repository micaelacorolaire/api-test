from pydantic import BaseModel,UUID4,field

class loginrequest(BaseModel):
    id_login=UUID4
    user_email=str
    user_password=str
