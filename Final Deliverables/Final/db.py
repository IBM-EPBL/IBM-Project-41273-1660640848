from flask import Flask,render_template
import ibm_db

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCerficate=DigiCertGlobalRootCA.crt;UID=gqx98810;PWD=shidQiWRftvLQAf5",'  ',' ')

print(conn)
print("Connection Successful...")




import requests,json
from flask import Flask,render_template


app = Flask(__name__)    

url = "https://news-api14.p.rapidapi.com/top-headlines"

querystring = {"country":"us","language":"en","pageSize":"10","category":"sports"}

headers = {
    "X-RapidAPI-Key": "25fe4c134cmsh2998c03a51ef787p13796bjsne1b8bb773157",
    "X-RapidAPI-Host": "news-api14.p.rapidapi.com"
}

def getnews():
    
    
    response = requests.get(url, headers=headers, params=querystring)
    d=json.loads(response.text)
    dict=d['articles']
    print(dict[0]['title'])
    return render_template("index.html",dict=dict)