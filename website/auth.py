# This is the same as what can be found in the views file just customized for auth.

from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return "<div>The Login Page is here</div>"

@auth.route("/logout")
def logout():
    return "<div>The logout Page is here</div>"

@auth.route("/sign-up")
def sign_up():
    return "<div>The Sign Up Page is here</div>"
