# Meteora
Meteor Shower Data Visualization Map through Kepler.gl.

## Data

The original data is in a CSV format.

The GeoJSON file is created based on the csv file of the original data using the `convert.py` script to create a data structure compatible with Kepler.gl's Trip layer, which allows us to visualize a feature in 4D, by displaying it on the map and through time by animating the feature based on it's location coordinates and a timestamp.

## Preview

![](https://cdn.discordapp.com/attachments/727996037188550728/1141818481692647619/image.png?ex=66280e53&is=6626bcd3&hm=5e5ca56aabdc9b23f799f10e7287db653e91b5b4f926a7df5263f6000a1b4f46&)
![](https://cdn.discordapp.com/attachments/727996037188550728/1142565291398795345/image.png?ex=662822d9&is=6626d159&hm=87bbf95ca66ab7414b891054bcc069075b98be74dafd8840aba7b1d2c0ce8afe&)

## Credit
This project was inspired by Tammo Jan Dijkema ([tammojan](https://github.com/tammojan/meteormap))'s meteor map and Hans van der Kwast ([jvdkwast](https://github.com/jvdkwast)) QGIS version of the metor shower animation: [Animations of Meteor Ground Tracks with the QGIS Temporal Controller](https://www.youtube.com/watch?v=-MpdsqbQsYY).

The project is built using [Kepler.gl](https://github.com/keplergl/kepler.gl) and the data is provided by [Global Meteor Network](https://globalmeteornetwork.org/data/).
