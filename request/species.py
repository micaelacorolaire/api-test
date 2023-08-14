from pydantic import BaseModel ,UUID4,field,HttpUrl

class species(BaseModel):
    id_species=UUID4
    species_name=str