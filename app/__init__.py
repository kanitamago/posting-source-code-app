from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object("app.config")

db_url = os.environ["DATABASE_URL"] or "postgresql://localhost/show_code_app"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

from app.views import views
