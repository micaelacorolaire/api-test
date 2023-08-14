from pydantic import  BaseModel , field

class species(BaseModel):
    id_species:str=field(...,min_length=1)
    species_name:str=field(...,min_length=1)