"""stat Model."""

from config.database import Model


class stat(Model):
    """stat Model."""
    #this is the stat model that fetches data from the stats database using the following parameters
    __fillable__=['country','longitude','latitude','total_cases','active_cases','recovered_cases','total_deaths']