



from flask_script import Manager, Server, Command
from flask_migrate import Migrate, MigrateCommand

from api import create_app
from api.extensions import db
from config import config

from mock import LoadData

env = config['development']

print(env.SQLALCHEMY_DATABASE_URI)

app = create_app(env)

migrate = Migrate(app, db)


if __name__ == "__main__":
    manage = Manager(app)
    manage.add_command('db', MigrateCommand)
    manage.add_command("load_dummy", LoadData)
    manage.add_command('runserver', Server('0.0.0.0', port=8000))
    manage.run()