#!/usr/bin/env python
import os

from app import create_app
from flask.ext.script import Manager, Shell

app = create_app()
manager = Manager(app)

def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def deploy():
    """Run deployment tasks."""
    pass


if __name__ == '__main__':
    manager.run()
