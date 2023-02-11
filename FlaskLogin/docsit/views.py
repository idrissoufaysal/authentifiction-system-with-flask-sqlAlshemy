from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required 
def Accueil():
    return render_template("Accueil.html", user=current_user)
    