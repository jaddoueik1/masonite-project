"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'geopyController@show'),
]
