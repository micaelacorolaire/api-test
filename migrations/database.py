import sqlalchemy as db
import os #libreria de python que me da variables del sistema.
from sqlalchemy.orm import sessionmaker,scoped_session #
from sqlalchemy.pool import StaticPool  #tipo de conexion estatica 


if os.environ["STAGE"]=="local":  #variable de entorno local config para probar en local yo,desarrollo
    engine=db.create_engine("postgresql://postgres:root@localhost:5432/PetsDB",echo=True)
else:
    engine=db.create_engine("postgresql://" +  ":".join([os.environ["RDS_USER"], os.environ["RDS_PASS"]])+ "localhost:5432")#para probar en producion
DB_session=scoped_session(sessionmaker(engine))
#string de conexion a la base de datos es como configuracion .