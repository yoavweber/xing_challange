from flask import Flask, render_template,flash,request,session
from collections import OrderedDict 
import requests
import json
from function import *



app = Flask(__name__)
app.secret_key = 'test_key'



@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        city = request.form['city1']
        dic_items = {str(get_city_temp(city)):city} # I had to convert to string since the cookie dosn't accept float/int
        session.update(dic_items)
        if len(dict(session)) == 2:
            highest_temp_dic = convert_float(dict(session))
            hottest_temp = max(highest_temp_dic)
            hottest_city = highest_temp_dic[hottest_temp]
            return '<b>{}</b> is the hottest city with <b>{}<b> degrees'.format(hottest_city,hottest_temp)
            
         
        
        
     
  
    return render_template('weather.html')


