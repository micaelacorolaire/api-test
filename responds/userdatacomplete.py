from pydantic import BaseModel,field

class userdatacomplete(BaseModel):
    user_id:str=field(...,min_length=1)
    user_name:str=field(...,min_length=1)
    user_lastname:str=field(...,min_length=1)
    user_telephone:int=field(...,min_length=1)
    user_email:str=field(...,min_length=1)
    other_phone:int=field(...,min_length=1)
    user_age:int=field(...,min_length=1)
    where_lives:str=field(...,min_length=1)