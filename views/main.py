import flask 
import os 
from flask import send_from_directory
from flask import request
from models import species
from models import animals 
from models import login
from models import userdatacomplete




app=flask (__name__)


    
@app.route('/homepage',methods=['get'])
def home_page(homepage):
    if request.method=='get':
        return homepage
    else:
        return 'error, the page is not being found,try again please.',404
    
@app.route('/species','/id_species',methods=['get','post','delete'])
def species(species,id_species):
    if request.method=='get':
        return species
    else:
        return ' The page could not be found , try again please.',404
def species(species,id_species):
    if request.method=='post':
        species=species.post.query.filter_by(id_species)
        return 'the table have been updated '
    else:
        return 'error,the table could not be updated '
def species(species,id_species):
    if request.method=='delete':
        species=species.delete.query.filter_by(id_species)
        return ' the table/field have been deleted'
    else:
       return 'the table/field  could not be deleted '
   
   
   
   
@app.route('animals',methods=['get'])
def check_animal(animals):
    if request.method=='get':
        return animals
    else:
        return 'The table register animal could not found,try again please',404
@app.route('registeranimals',methods=['post'])
def check_animal(animals):
    if request.method=='post':
        animals=animals.query.post(animals).first()
        return 'the table/field in register animal  have been  updated '
    else:
        return 'the table/field in register animal could not updated'

@app.route('animals',methods=['delete'])
def check_animal(animals):
    pass
             
    
@app.route('/login',methods=['get'])
def userlogin(login):
    if request.method=='get':
        pass
        
@app.route('/login',methods=['post ']) 
def login(login):   
    pass

@app.route('/login',methods=['delete'])
def login(login):
    pass


@app.route('/userdatacomplete',methods=['get'])
def user_datacomplete(userdatacomplete):
     pass
@app.route('/userdatacoplete',methods=['post'])
def userdatacomplete(userdatacomplete):
    pass
@app.route('/userdatacomplete',methods=['delete'])
def userdatacomplete(userdatacomplete):
    pass
    
@app.route('/race',methods=['get'])
def enter_race(race):
    pass
    
@app.route('/race',methods=['post'])
def race(race):
    pass

@app.route('/race',methods=['delete'])
def race(race):
    pass
@app.route('/sign_in',metohds=['get'])
def race(sign_in):
    pass

@app.route('/sign_in',methods=['post'])
def race(sign_in):
    pass


@app.route('/sign_in',methods=['delete'])
def sign_in(sign_in):
    pass

 app.run(debug=True)          
    