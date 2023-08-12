from sqlalchemy import column,interger,String
from models.base import BaseModel

class sign_up(BaseModel):
    __tablename__='sign_up'
    __args__={'schema':'public'}
    id_sign_up=column(str,primary_key=True,nullable=False)
    email_to_sign_up=column(str,nullable=False)
    cellphone_to_sign_up=column(int,nullable=False)
    password_to_signup=column(str,nullable=False)
    user_name=column(str,nullable=False)
    
    
