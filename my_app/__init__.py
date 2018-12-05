from flask import Flask
from my_app.crawler.views import views

app = Flask(__name__)
app.register_blueprint(views)
