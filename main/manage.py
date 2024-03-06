from flask_migrate import Migrate, MigrateCommand
from flask.cli import FlaskGroup

from main import app, db

migrate = Migrate(app, db)
cli = FlaskGroup(app)

cli.add_command('db', MigrateCommand)

if __name__ == '__main__':
    cli()
