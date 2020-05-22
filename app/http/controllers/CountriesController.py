"""A CountriesController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.stat import stat
from storage.public import sorting

class CountriesController(Controller):
    """CountriesController Controller Class."""

    def __init__(self, request: Request):
        #in this controller's construct method we can find the model stat fetching all of the data from the database and displaying as a list of lists
        stats = stat.all()
        self.list = []
        for x in stats:
            self.list.append(
                [x.country, x.total_cases, x.active_cases, x.recovered_cases, x.total_deaths])

    def show(self,view:View,request:Request):
        #this is the show function in which the list is inherited from the construct method and passed to the template "blades" to be displayed 
        stats=self.list
        return view.render('Covid-19/worldStats',{'stats':stats})

    def sortData(self, view: View, request: Request):
        #this is the function in which we sort data we have created an algorithm that sorts all type of data strings,integers... and it returns them as a list of lists
        #in order to see the algorithm please go to storage->public->sorting.py
        request=request.all(internal_variables=False)
        #the controller gets the request from the route and passes it after sorting the data sortBy is the variable responsible of getting what type of data the user would like
        #to see such as by total cases, total deaths etc...
        liste=self.list
        sortBy=request['sortlist']
        state=request['state']
        if state == 'asc':
            value=1
        else:
            value=0
        stats=sorting.tri_selection(liste,value,sortBy)
        return view.render('Covid-19/worldStats', {'stats': stats})
        #we can assign sortBy to the letters indicated by Yammine n,t,a,r,d in the value of the buttons 