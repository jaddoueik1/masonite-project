"""Location Model."""

from config.database import Model


class Location(Model):
    """Location Model."""
    __fillable__=['country','longitude','latitude','codes','country_code','continent_code']