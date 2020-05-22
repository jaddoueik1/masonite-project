from orator.migrations import Migration


class Countries(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('countries') as table:
            table.increments('id')
            table.string('country')
            table.string('longitude')
            table.string('latitude')
            table.string('total_cases')
            table.string('active_cases')
            table.string('recovered_cases')
            table.string('total_deaths')
            table.timestamps()
        pass

