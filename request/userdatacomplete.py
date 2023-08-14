from pydantic import Basemodel,UUID4,field,HttpUrl

class userdatacompleterequest(Basemodel):
    user_id=UUID4
    user_name=str
    user_lastname=str
    user_phonenumer=int
    user_email=str
    other_phone=int
    user_photo=HttpUrl
    user_age=int
    where_live=str