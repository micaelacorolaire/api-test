from sqlalchemy import Column, Integer, String,ForeignKey
from models.base import BaseModel
from sqlalchemy import relationship


class userdatacomplete(BaseModel):
    user_id=Column(int,nullable=True,primarykey=True)
    user_name=Column(str,nullable=False)
    user_lastname=Column(str,nullable=True)
    user_numberphone=Column(int,nullable=True)
    user_email=Column(str,nullable=True)
    other_phone=Column(int,nullable=True)
    user_photo=Column(bool,nullable=False)
    user_age=Column(int,nullable=True)
    where_live=Column(str,nullable=True)
    user_name=relationship("user_name",foreignkeys=[id_login])
    
