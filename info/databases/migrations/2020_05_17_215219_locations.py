from orator.migrations import Migration


class Locations(Migration):

    def up(self):
        with self.schema.create('locations') as table:
            table.increments('id')
            table.string('country')
            table.string('longitude')
            table.string('latitude')
            table.string('codes')
            table.string('country_code')
            table.string('continent_code')
        pass

