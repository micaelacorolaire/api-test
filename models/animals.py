from sqlalchemy import Column, Integer, String,ForeignKey,HttpUrl
from models.base import BaseModel
from sqlalchemy import relationship

class animals(BaseModel):
    ___tablename__="Animals"
    __args__={"schema":"public"}
    id_race=Column(int,ForeignKey=True,nullable=False)
    id_animal=Column(int,primary_key=True,nullable=False)
    age=Column(int,nullable=False)
    hair_color=Column(str,nullable=False)
    eyes_color=Column(str,nullable=False)
    weight=Column(float,nullable=False)
    character=Column(str,nullable=False)
    teeth=Column(str,nullable=False)
    size=Column(str,nullable=False)
    diseases=Column(str,nullable=False)
    disabilities=Column(str,nullable=False)  
    photo_animal=Column(HttpUrl,nullable=False) 
