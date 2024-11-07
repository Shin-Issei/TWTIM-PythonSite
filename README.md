# TWTIM-PythonSite

Following the Tech With Tim Video Tutorial!

The read me will just be the notes from each section of the video.

# INTRO

The idea behind the tutorial is to make a notes app with user authentication utilizing flask.

# Project Demo

Just a sponsor segment but the demo was at least cool.

# Directory structure

There is a specific way to organize our web project in order to keep the information needed straight.

We made the following files: 
auth, views, models, and __init__ 

basically auth is for user auth
views is for the front end
models is for the backend
and init is to initialize something that I don't quite get yet.

# Flask Setup

Why not Django? Flask is less complicated and faster for smaller projects knowing both may be advangateous. 

I have always thought that I could make things from scratch but considering that I just installed 3 packages created by who knows who god knows when I think that the whole 'real coders code from scratch' mentality is good and dead...Thank God.

# Creating a Flask App

So the point of __init__ was so that we can modularize our code. 

in main.py you will see a directive that allows us to import from the website folder but the folder isn't a python module right? Well, because of __init__ it actually is and that allows us to export functions and methods! Pretty cool eh?

So where are we right now? :

- The flask dependencies are installed
- The boiler plate is set up
- The app is capable of being run
- The server can go live without errors but doesn't have any routes
- This is the hypest shit.

# Creating Routes/Views

While I still don't really *get* what Flask is 
as an object or anything like that I am beginning to understand...nothing...Let's just keep going.

The way that routes work is by making functions that return valid html 
That is the point of the blueprint object.

Once we create the route the app has no idea that the route exists until we regisiter it. 

In order to register the URLs go to init.py

!!! HAZARD WARNING !!!

So I got the following error.

AttributeError: 'function' object has no attribute 'register'

I didn't know what that meant. I couldn't figure out that I had named something improperly.

So in the auth.py file i put the following:

    from flask import Blueprint


    auth = Blueprint('auth', __name__)

    @auth.route("/")
    def auth(): << This is where the error is! Flask tried register the *function* instead of the *blueprint object* we needed to register.
        return "<div></div>"

So the lessions to glean from this section of the tutorial is the following

- First there must be a server
- Then once the server can run then you need routes
- The server listens for the request to the given route and returns the function
- the return value of the function is just text that is HTML that the browser can parse
- Instead of having the whole page be just a few lines of html we are going to learn how to
make something with more structure appear. 
- Ohh dis is gon' be gud! :D