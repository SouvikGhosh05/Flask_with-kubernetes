import os 
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/')
def method_post():
    text=request.form['city'].lower()
    
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"

    querystring = {"city":text}

    headers = {
        "X-RapidAPI-Host": os.getenv('API_HOST'),
        "X-RapidAPI-Key": os.getenv('API_KEY')
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
