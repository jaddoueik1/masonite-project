"""A mapController Module."""

import geopy 
import pandas
import folium 
from folium.plugins import MarkerCluster
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

class mapController(Controller):
    """mapController Controller Class."""

    def __init__(self, request: Request):
        csvFile=pandas.read_csv('public/database.csv')
        worldMap=folium.Map(tiles='cartodbpositron')
        marker_cluster=MarkerCluster().add_to(worldMap)
        for i in range(len(csvFile)):
            latitude=csvFile.iloc[i]['lattitude']
            longitude=csvFile.iloc[i]['longitude']
            cases=str(csvFile.iloc[i]['countryName'])+' '+'Total Cases:'+ str(csvFile.iloc[i]['total_cases'])
            radius=5
            folium.CircleMarker(location=[latitude,longitude],radius=radius,popup=cases,fill=True).add_to(marker_cluster)
        worldMap.save('resources/templates/map.html')

    def show(self, view: View):
        return view.render('map')
