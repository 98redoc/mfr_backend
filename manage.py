import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from micro_flaskr import create_app, db
from micro_flaskr.models import *


app = create_app()
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)


# cli for database
manager.add_command('db', MigrateCommand)

@manager.command
def run():
	app.run()


if __name__ == "__main__":
	manager.run()
