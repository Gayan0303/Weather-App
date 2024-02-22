from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) for handling requests from different origins
CORS(app)

# Set the static folder for serving static files like CSS, JavaScript, images, etc.
app.static_folder = 'static'

# Route for the homepage
@app.route('/')  
def index():
    # Render the index.html template
    return render_template('index.html')

# Route for handling POST requests to fetch weather data
@app.route('/weather', methods=['POST'])  
def get_weather():
    # Extract the city from the form data
    city = request.form['city']
    
    # OpenWeatherMap API key
    api_key = '9074344fd51c721b9a4c474fe71ac966'
    
    # Construct the API URL with the city and API key, requesting metric units for temperature
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract weather information from the JSON response
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Return the weather data as JSON
        return jsonify({
            'city': city,
            'description': weather_description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        })
    else:
        # If the request was not successful, return an error message with status code 404
        return jsonify({'error': 'City not found or error fetching data'}), 404

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
