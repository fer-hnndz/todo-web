from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
import os


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()


def create_app():
    load_dotenv()

    HOST = os.environ.get("POSTGRES_HOST")
    PORT = os.environ.get("POSTGRES_PORT")
    DATABASE = os.environ.get("POSTGRES_DB")
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")

    if not all([HOST, PORT, DATABASE, USER, PASSWORD]):
        raise ValueError(
            "Please set the environment variables for PostgreSQL connection."
        )

    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from .models import Task, User  # Register models to ensure they are created

        db.create_all()

    return app
