from pydantic import BaseModel,field

class animalresponse(BaseModel):
    id_race:str=field(...,min_length=1)
    id_animal:str=field(...,min_length=1)
    age:int=field(...,min_length=1)
    hair_color:str=field(...,min_length=1)
    eyes_color:str=field(...,min_length=1)
    weight:float=field(...,min_length=1)
    character:str=field(...,min_length=1)
    teeth:str=field(...,min_length=1)
    size:str=field(...,min_length=1)
    diseases:str=field(...,min_length=1)
    disabilities:str=field(...,min_length=1)