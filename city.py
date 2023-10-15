from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from geopy.geocoders import Nominatim
import requests
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///city_data.db'
db = SQLAlchemy(app)
geolocator = Nominatim(user_agent="city_app")

# Define the State model
class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    state = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


# Define a function to fetch universities based on the city name
def get_universities(city_name):
    api_url = f"http://universities.hipolabs.com/search?name={city_name}"
    response = requests.get(api_url)
    universities_data = response.json()

    universities = []  # Create a list to store university dictionaries

    for university_data in universities_data:
        university = {
            'country': university_data.get('country', 'N/A'),
            'name': university_data.get('name', 'N/A'),
        }
        universities.append(university)

    return universities



@app.route('/')
def index():
    cities = City.query.all()

    def random_color():
        # Generate a random color in hexadecimal format
        return '#{0:02x}{1:02x}{2:02x}'.format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    return render_template('index.html', cities=cities, random_color=random_color)


@app.route('/city/<int:city_id>')
def city_details(city_id):
    city = City.query.get(city_id)
    if city:
        location = geolocator.reverse(f"{city.latitude}, {city.longitude}", exactly_one=True)
        address = location.address if location else "Address not found"

        # Get universities based on the city name
        universities = get_universities(city.name)

        # Fetch education-related news for the city using the News API
        news_api_url = f"https://newsapi.org/v2/everything?q=education+{city.name}&apiKey=fc9d7523a40c49f4b065e623bcf940e5"
        response = requests.get(news_api_url)
        news_data = response.json()
        education_news = news_data.get('articles', [])  # Extract the articles

        return render_template('city.html', city=city, address=address, universities=universities, education_news=education_news)
    else:
        return "City not found", 404







# Define the get_states() function to fetch states
def get_states():
    # Assuming you have a 'State' model with a 'name' attribute
    # Replace 'State' with your actual model name
    states = State.query.all()

    # Extract the state names from the 'State' objects
    state_names = [state.name for state in states]

    return state_names


# Define your routes as shown in your previous code
@app.route('/cities')
def cities():
    # Retrieve and display a list of cities
    cities = City.query.all()
    return render_template('cities.html', cities=cities)



@app.route('/states')
def states():
    # Retrieve and display a list of states
    states = get_states()
    return render_template('states.html', states=states)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Run the Flask app on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
