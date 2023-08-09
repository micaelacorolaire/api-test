from sqlalchemy import Column, Integer, String,ForeignKey
from models.base import BaseModel
from sqlalchemy import relationship

class species(BaseModel):
    __tablename__="species"
    __args__={"schema":"public"}
    id_species=Column(int,primary_key=True,nullable=False)
    species_name=Column(str,nullable=False)
