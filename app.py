from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.static_folder = 'static'
@app.route('/')  # Endpoint for rendering the template
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])  # Endpoint for handling POST requests
def get_weather():
    city = request.form['city']
    api_key = '9074344fd51c721b9a4c474fe71ac966'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return jsonify({
            'city': city,
            'description': weather_description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        })
    else:
        return jsonify({'error': 'City not found or error fetching data'}), 404

if __name__ == '__main__':
    app.run(debug=True)
