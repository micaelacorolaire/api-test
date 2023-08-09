from flask import flask 
import os 
from flask import send_from_directory

app=flask (__name__)


    
@app.route('/homepage')
def home_page(homepage):
    #falta desarrollar
    
@app.route('/species',methods=['get','post','delete'])
def species(species):
    #falta desarrollar
    
@app.route('registeranimals',methods=['get','delete','post','put'])
def check_animal(registeranimals):
    #desarrollar
    
@app.route('/user_login',methods=['get','post','delete','put'])
def userlogin(user_login):
    
@app.route('/userdatacomplete',methods=['get','post','put','delete'])
def user_datacomplete(userdatacomplete):
    
@app.route('/enter_user',methods=['get','delete','put','post'])
def enter_user(enter_user):
    
@app.route('/race',methods=['get','delete','put','post'])
def enter_race(race):