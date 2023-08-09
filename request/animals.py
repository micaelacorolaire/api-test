from pydantic import BaseModel ,UUID4,field,HttpUrl

class animalrequest(BaseModel):
    id_animal=UUID4
    age=int
    hair_color=str
    eyes_color=str
    weight=float
    character=str
    teeth=str
    size=str
    diseases=str
    disabilities=str   
    photo_animal=HttpUrl