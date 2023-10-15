from city import app, db, City

# Sample city data
city_data = [
    {"name": "Alabama", "state": "Montgomery", "latitude": 32.3777, "longitude": -86.3006},
    {"name": "Alaska", "state": "Anchorage", "latitude": 61.1650, "longitude": -149.8580},
    {"name": "Arizona", "state": "Phoenix", "latitude": 33.4484, "longitude": -112.0740},
    {"name": "Arkansas", "state": "Little Rock", "latitude": 34.7465, "longitude": -92.2896},
    {"name": "California", "state": "Los Angeles", "latitude": 34.0522, "longitude": -118.2437},
    {"name": "Colorado", "state": "Denver", "latitude": 39.7392, "longitude": -104.9903},
    {"name": "Connecticut", "state": "Hartford", "latitude": 41.7637, "longitude": -72.6851},
    {"name": "Delaware", "state": "Dover", "latitude": 39.1582, "longitude": -75.5244},
    {"name": "Florida", "state": "Jacksonville", "latitude": 30.3322, "longitude": -81.6557},
    {"name": "Georgia", "state": "Atlanta", "latitude": 33.7490, "longitude": -84.3880},
    {"name": "Hawaii", "state": "Honolulu", "latitude": 21.3069, "longitude": -157.8583},
    {"name": "Idaho", "state": "Boise", "latitude": 43.6150, "longitude": -116.2023},
    {"name": "Illinois", "state": "Chicago", "latitude": 41.8781, "longitude": -87.6298},
    {"name": "Indiana", "state": "Indianapolis", "latitude": 39.7681, "longitude": -86.1570},
    {"name": "Iowa", "state": "Des Moines", "latitude": 41.5868, "longitude": -93.6250},
    {"name": "Kansas", "state": "Topeka", "latitude": 39.0558, "longitude": -95.6890},
    {"name": "Kentucky", "state": "Louisville", "latitude": 38.2527, "longitude": -85.7585},
    {"name": "Louisiana", "state": "Baton Rouge", "latitude": 30.4515, "longitude": -91.1871},
    {"name": "Maine", "state": "Augusta", "latitude": 44.3072, "longitude": -69.7810},
    {"name": "Maryland", "state": "Baltimore", "latitude": 39.2904, "longitude": -76.6122},
    {"name": "Massachusetts", "state": "Boston", "latitude": 42.3601, "longitude": -71.0589},
    {"name": "Michigan", "state": "Detroit", "latitude": 42.3314, "longitude": -83.0458},
    {"name": "Minnesota", "state": "Minneapolis", "latitude": 44.9778, "longitude": -93.2650},
    {"name": "Mississippi", "state": "Jackson", "latitude": 32.2988, "longitude": -90.1848},
    {"name": "Missouri", "state": "Kansas City", "latitude": 39.0997, "longitude": -94.5786},
    {"name": "Montana", "state": "Helena", "latitude": 46.5898, "longitude": -112.0391},
    {"name": "Nebraska", "state": "Lincoln", "latitude": 40.8136, "longitude": -96.7026},
    {"name": "Nevada", "state": "Las Vegas", "latitude": 36.1699, "longitude": -115.1398},
    {"name": "New Hampshire", "state": "Concord", "latitude": 43.2081, "longitude": -71.5376},
    {"name": "New Jersey", "state": "Trenton", "latitude": 40.2206, "longitude": -74.7597},
    {"name": "New Mexico", "state": "Santa Fe", "latitude": 35.6828, "longitude": -105.9378},
    {"name": "New York", "state": "New York City", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "North Carolina", "state": "Raleigh", "latitude": 35.7796, "longitude": -78.6382},
    {"name": "North Dakota", "state": "Bismarck", "latitude": 46.8083, "longitude": -100.7837},
    {"name": "Ohio", "state": "Columbus", "latitude": 39.9612, "longitude": -82.9988},
    {"name": "Oklahoma", "state": "Oklahoma City", "latitude": 35.4676, "longitude": -97.5164},
    {"name": "Oregon", "state": "Portland", "latitude": 45.5051, "longitude": -122.6750},
    {"name": "Pennsylvania", "state": "Philadelphia", "latitude": 39.9526, "longitude": -75.1652},
    {"name": "Rhode Island", "state": "Providence", "latitude": 41.8240, "longitude": -71.4128},
    {"name": "South Carolina", "state": "Columbia", "latitude": 34.0007, "longitude": -81.0348},
    {"name": "South Dakota", "state": "Pierre", "latitude": 44.3683, "longitude": -100.3500},
    {"name": "Tennessee", "state": "Nashville", "latitude": 36.1627, "longitude": -86.7816},
    {"name": "Texas", "state": "Houston", "latitude": 29.7604, "longitude": -95.3698},
    {"name": "Utah", "state": "Salt Lake City", "latitude": 40.7608, "longitude": -111.8910},
    {"name": "Vermont", "state": "Montpelier", "latitude": 44.2601, "longitude": -72.5754},
    {"name": "Virginia", "state": "Richmond", "latitude": 37.5407, "longitude": -77.4360},
    {"name": "Washington", "state": "Seattle", "latitude": 47.6062, "longitude": -122.3321},
    {"name": "West Virginia", "state": "Charleston", "latitude": 38.3498, "longitude": -81.6326},
    {"name": "Wisconsin", "state": "Milwaukee", "latitude": 43.0389, "longitude": -87.9065},
    {"name": "Wyoming", "state": "Cheyenne", "latitude": 41.1399, "longitude": -104.8202}
]


# Add cities to the database
with app.app_context():
    for data in city_data:
        city = City(name=data["name"], state=data["state"], latitude=data["latitude"], longitude=data["longitude"])
        db.session.add(city)
    db.session.commit()

print("Cities added to the database.")

