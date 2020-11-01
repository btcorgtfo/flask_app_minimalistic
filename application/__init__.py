from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    with app.app_context():


        from application.routes import routes

        # register blueprints

        app.register_blueprint(routes.user_interface)

        return app
