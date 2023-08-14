from sqlalchemy import Column, Integer, String,ForeignKey
from models.base import BaseModel
from sqlalchemy import relationship

class race(BaseModel):
    __tablename__="Race"
    __args__={"schema":"public"}
    id_race=Column(str,primary_key=True,nullable=False)
    race_name=Column(str,nullable=False)
    race=(relationship("race",backpopulates=[id_animal]))
    species_name=(relationship("species",backpopulates=[id_species]))
