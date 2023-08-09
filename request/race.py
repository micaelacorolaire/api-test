from pydantic import BaseModel ,UUID4,field,HttpUrl

class race(BaseModel):
    id_race=UUID4
    race_name=str
    