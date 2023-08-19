import pandas as pd
from datetime import datetime, timedelta
import geojson

"""
The data used in this project is not fit to work with Kepler.gl's Trip layer, which is a feature layer that allows us to animate a feature traveling between multiple locations, while the original data only has  long/lat coordinates for both starting and ending locations (which is great for the Arc layer in Kepler.gl) it is possible to create a GeoJSON file with the right data structure.

For the sake of Trip layer visualization in Kepler.gl I need to create intermediate travel points between starting and ending point within a GeoJSON file, for this, I'm taking the lat/long coordinates and elevation height for both start and end of observation of the feature (meteor) and with the data of the start of observation combined with the data of duration (how long did the meteor last) I can create a data structure that works with the Trip layer.

Original data is by Global Meteor Network at https://globalmeteornetwork.org/data/
"""

# Data CSV file
csv_file = 'meteors.csv'
data = pd.read_csv(csv_file)

# Holding GeoJSON features in a list
features = []

# Calculate intermediate points
def calculate_intermediates(start_coords, end_coords, duration, num_points):
    intermediates = []
    for i in range(num_points + 1):
        ratio = i / num_points
        lat = start_coords[1] + ratio * (end_coords[1] - start_coords[1])
        lon = start_coords[0] + ratio * (end_coords[0] - start_coords[0])
        elev = start_coords[2] + ratio * (end_coords[2] - start_coords[2])
        timestamp = start_time + timedelta(seconds=ratio * (duration * 4))  # Adjusted duration (exageration for visual purpose only)
        intermediates.append([round(lon, 4), round(lat, 4), elev, int(timestamp.timestamp() * 1000)]) # [lon, lat, elvation, timestamp]
    return intermediates

# Loop through each row in the CSV input
for index, row in data.iterrows():
    start_coords = [row['LonBeg'], row['LatBeg'], row['Ht_beg (km)']]
    end_coords = [row['LonEnd'], row['LatEnd'], row['Ht_end (km)']]
    start_time = datetime.strptime(row['Start (UTC)'].strip(), '%Y-%m-%d %H:%M:%S.%f')
    duration = row['Duration (s)']
    num_intermediates = 1  # Adjust the number of intermediate points as needed

    intermediates = calculate_intermediates(start_coords, end_coords, duration, num_intermediates)
    
    coordinates = [[round(start_coords[0], 4), round(start_coords[1], 4), start_coords[2], int(start_time.timestamp() * 1000)]] + intermediates + [[round(end_coords[0], 4), round(end_coords[1], 4), end_coords[2], int((start_time + timedelta(seconds=duration)).timestamp() * 1000)]]

    properties = {
        "Start (UTC)": row['Start (UTC)'],
        "Average Speed": row['V_avg (km/s)'],
        "Duration (s)": row['Duration (s)'],
        "Peak": row['Peak (abs mag)'],
        "Stations": row['Stations'],
        "Shower": row['Shower'],
        "Radiant RA": row['Radiant RA'],
        "Radiant DEC": row['Radiant DEC']
    }

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": coordinates
        },
        "properties": properties
    }

    features.append(feature)

# Create a GeoJSON FeatureCollection
geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# Write GeoJSON to a file
output_geojson = 'meteors.geojson'
with open(output_geojson, 'w') as outfile:
    geojson.dump(geojson_data, outfile, indent=2)

print("GeoJSON file generated successfully!")
