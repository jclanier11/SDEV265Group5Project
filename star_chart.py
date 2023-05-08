# GitHub repo url: https://github.com/viyaleta/Python-Demos/blob/main/Sky%20Map%20Demo.ipynb

# datetime library
from datetime import datetime
from geopy import Nominatim
from tzwhere.tzwhere import tzwhere
from pytz import timezone, utc
# matplotlib to help display our star map
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle
# skyfield for star data
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos, stellarium
from skyfield.projections import build_stereographic_projection


# Loading Earth and Star Data
# skyfield library to load star data
# de421 shows position of earth and sun in space
eph = load('de421.bsp')
# hipparcos dataset contains star location data
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

# Setting up the Obversation Location
# location = 'Times Square, New York, NY'
when = f'{year}-{month}-{day} {hour}'

# geopy library for latitude and longitute
locator = Nominatim(user_agent='myGeocoder', timeout=3)
location = locator.geocode(location, language='en')
lat, long = location.latitude, location.longitude

# tzwhere and pytz libraries to get the timezone of our location
# convert date string into datetime object
dt = datetime.strptime(when, '%Y-%m-%d %H:%M')
# define datetime and convert to utc based on our timezone
timezone_str = tzwhere().tzNameAt(lat, long)
local = timezone(timezone_str)
# get UTC from local timezone and datetime
local_dt = local.localize(dt, is_dst=None)
utc_dt = local_dt.astimezone(utc)

# skyfield library to define the location and time of our observation and
# define the position of our observer
# find location of earth and sun and set the observer position
sun = eph['sun']
earth = eph['earth']
# define observation time from our UTC datetime
ts = load.timescale()
t = ts.from_datetime(utc_dt)
# define an observer using the world geodetic system data
observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=long).at(t)
position = observer.from_altaz(alt_degrees=90, az_degrees=0)

# Calculate Star Positions
ra, dec, distance = observer.radec()
center_object = Star(ra=ra, dec=dec)

center = earth.at(t).observe(center_object)
projection = build_stereographic_projection(center)
field_of_view_degrees = 180.0

star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

# Build The Star Chart
chart_size = 10
max_star_size = 100
limiting_magnitude = 10
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]

fig, ax = plt.subplots(figsize=(chart_size, chart_size))

fig.canvas.manager.set_window_title('Star Chart')

border = plt.Circle((0, 0), 1, color='#16161d', fill=True)
ax.add_patch(border)

marker_size = max_star_size * 10 ** (magnitude / -2.5)

# And the constellation outlines come from Stellarium.  We make a list
# of the stars at which each edge stars, and the star at which each edge
# ends.

url = ('https://raw.githubusercontent.com/Stellarium/stellarium/master'
       '/skycultures/modern_st/constellationship.fab')

with load.open(url) as f:
    constellations = stellarium.parse_constellations(f)

edges = [edge for name, edges in constellations for edge in edges]
edges_star1 = [star1 for star1, star2 in edges]
edges_star2 = [star2 for star1, star2 in edges]

# The constellation lines will each begin at the x,y of one star and end
# at the x,y of another.  We have to "rollaxis" the resulting coordinate
# array into the shape that matplotlib expects.

xy1 = stars[['x', 'y']].loc[edges_star1].values
xy2 = stars[['x', 'y']].loc[edges_star2].values
lines_xy = np.rollaxis(np.array([xy1, xy2]), 1)

# Draw the constellation lines.

ax.add_collection(LineCollection(lines_xy, colors='#468130'))

ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
           s=marker_size, color='white', marker='.', linewidths=0,
           zorder=2)

horizon = Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizon)

ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_title(f'Star Chart for\n'
             f'{location} at {when}\n'
             f'{utc_dt} UTC')
plt.axis('off')

plt.show(block=False)


