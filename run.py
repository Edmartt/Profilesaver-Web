import unittest
from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
