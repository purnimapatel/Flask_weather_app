import requests
from flask import Flask, render_template, request
import configparser


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods = ['POST'])
def results():
    city_name = request.form['city_name']
    api_key = "40f2aad59fa86762c55d14cbc770afb6"
    data = results_api(city_name)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    return render_template('results.html',location=location, temp = temp, feels_like= feels_like, weather = weather, pressure = pressure , humidity = humidity)


def results_api(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=40f2aad59fa86762c55d14cbc770afb6&units=metric".format(city_name)
    r = requests.get(api_url)
    return r.json()
results_api("Lucknow")
    
if __name__ == '__main__':
    app.run(debug=True)
