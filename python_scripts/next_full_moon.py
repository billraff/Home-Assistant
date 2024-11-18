import ephem
from datetime import datetime, timedelta

# Initialize moon and observer
moon = ephem.Moon()
observer = ephem.Observer()

# Set observer's location (you can set to your latitude and longitude)
observer.lat = '30.552867813401615'  # Replace with your latitude
observer.lon = '-97.74448947317995'  # Replace with your longitude

# Calculate the next full moon
next_full_moon = ephem.next_full_moon(datetime.utcnow())
hass.states.set("sensor.next_full_moon", next_full_moon.datetime().isoformat())

