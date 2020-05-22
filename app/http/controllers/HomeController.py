"""A HomeController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class HomeController(Controller):
    """HomeController Controller Class."""

    def __init__(self, request: Request):
        """HomeController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        #this is the index show function that just renders the index.html file
        return view.render('Covid-19/index')
