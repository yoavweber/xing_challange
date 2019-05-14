from flask import Flask, render_template,flash,request,session
from collections import OrderedDict 
import requests
import json
from function import *



app = Flask(__name__)
app.secret_key = 'test_key'



@app.route('/', methods=('GET'))
def hello_world():
    if request.method == 'GET':
        city = request.args.get('city')
        dic_items = {str(get_city_temp(city)):city} # I had to convert to string since the cookie dosn't accept float/int
        session.update(dic_items)
        if len(dict(session)) == 5:
            highest_temp_dic = convert_float(dict(session)) # here i convert it back to float
            hottest_temp = max(highest_temp_dic)
            hottest_city = highest_temp_dic[hottest_temp]
            return '<b>{}</b> is the hottest city with <b>{}<b> degrees'.format(hottest_city,hottest_temp)
            
         
        
        
     
  
    return render_template('weather.html')


