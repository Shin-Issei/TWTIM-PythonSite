# Here is where we are going to store our views for our site.

from flask import Blueprint

# What Blueprint means is that there are a bunch of views/routes 

views = Blueprint('views', __name__)

@views.route("/") # Home page route
def home():
    return "<h1>Test</h1>"
