# Meteora
Meteor Shower Data Visualization Map through Kepler.gl.

## Data

The original data is in a CSV format.

The GeoJSON file is created based on the csv file of the original data using the `convert.py` script to create a data structure compatible with Kepler.gl's Trip layer, which allows us to visualize a feature in 4D, by displaying it on the map and through time by animating the feature based on it's location coordinates and a timestamp.

## Preview

![](https://cdn.discordapp.com/attachments/727996037188550728/1141818481692647619/image.png)
![](https://cdn.discordapp.com/attachments/727996037188550728/1142565291398795345/image.png)

## Credit
This project was inspired by Tammo Jan Dijkema ([tammojan](https://github.com/tammojan/meteormap))'s meteor map and Hans van der Kwast ([jvdkwast](https://github.com/jvdkwast)) QGIS version of the metor shower animation: [Animations of Meteor Ground Tracks with the QGIS Temporal Controller](https://www.youtube.com/watch?v=-MpdsqbQsYY).

The project is built using [Kepler.gl](https://github.com/keplergl/kepler.gl) and the data is provided by [Global Meteor Network](https://globalmeteornetwork.org/data/).