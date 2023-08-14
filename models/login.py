from sqlalchemy import Column, Integer, String
from models.base import BaseModel




class data_login(BaseModel):
    __tablename__="Data Login"
    __args__={"schema":"public"}
    id_login=Column(str,primary_key=True,nullable=False)
    user_email=Column(str,nullable=False)
    user_password=Column(str,nullable=False)
    cellphone=Column(int,nullable=False)
    user_name=Column(str,nullable=False)