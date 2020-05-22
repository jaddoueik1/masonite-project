"""A MapController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
import geopy 
import pandas
import folium 
from folium.plugins import MarkerCluster
from app.stat import stat
import geoip2.database
import requests

class MapController(Controller):
    """MapController Controller Class."""

    def __init__(self, request: Request):
        #this is the map controller this is where the whole map is created
        ipAdress=requests.get('http://wtfismyip.com/text').text.strip()
        reader=geoip2.database.Reader('public/GeoLite2-City.mmdb')
        response=reader.city(ipAdress)
        #these past three lines are responsible of getting the user's location based on his public IP adress so you can tryy
        #and use VPN to get a marker in your new location
        userCountry=response.country.name
        worldMap=folium.Map(tiles='cartodbpositron',zoom_start=3)
        marker_cluster=MarkerCluster().add_to(worldMap)
        locations=stat.all()
        #in this project we decided to use the folium library this is a very useful library and its really easy to use the stat module
        #fetchs all the data we need from the database and its passed in a for loop to add each country's marker and its total cases
        i=0
        for location in locations:
            latitude=float(location.latitude)
            longitude=float(location.longitude)
            cases=str(location.country)+' '+'Total Cases:'+str(location.total_cases)
            radius=5
            if location.country == userCountry:
                folium.Marker(location=[location.latitude,location.longitude],popup=cases,fill=True).add_to(worldMap)
            else:
                folium.CircleMarker(location=[latitude,longitude],radius=radius,popup=cases,fill=True).add_to(marker_cluster)
            i+=1
        self.worldMap=worldMap
        worldMap.save('resources/templates/Covid-19/folium-map.html')
        #then the map is saved as an html file that is included in the heatMap.html file that is located in resources/templates/Covid-19/


    def show(self, view: View):
        return view.render('Covid-19/heatMap')
