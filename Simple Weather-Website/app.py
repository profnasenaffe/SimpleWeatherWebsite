from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "my api key"

@app.route('/')
def weather_form():
    return render_template('weather_form.html')

@app.route('/', methods=['POST'])
def weather_data():
    user_input = request.form['city']
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        return render_template('weather_form.html', error="No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        return render_template('weather_result.html', city=user_input, weather=weather, temp=temp)
