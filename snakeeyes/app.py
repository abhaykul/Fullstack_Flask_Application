from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    # this param looks for a instance module
    app = Flask(__name__, instance_relative_config=True)
    # loads a settings.config module
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        # return app.config['HELLO']
        return "Hello there"

    return app
