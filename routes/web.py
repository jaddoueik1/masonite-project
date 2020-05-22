"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'HomeController@show'),
    Get('/world-map','MapController@show'),
    Get('/world-statistics','CountriesController@show'),
    Post('/world-statistics','CountriesController@sortData')
]

#this is the routes page where all the routes are sent to the controllers to handle them we can see get and post methods 
#the post method is actually used to get the request from the sorting page and then it goes to the controller