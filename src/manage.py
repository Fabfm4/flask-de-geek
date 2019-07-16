# -*- coding: utf-8 -*-
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from whereareyou import app, models


migrate = Migrate(app, models.db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
