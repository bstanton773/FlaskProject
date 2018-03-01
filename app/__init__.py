from flask import Flask
from config import Config

app2 = Flask(__name__)
app2.config.from_object(Config)

#setup Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app2)
migrate = Migrate(app2, db)

from app import routes

