from NZA_Law import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Forms import
from NZA_Law.forms import LawyerInfoForm

# Models import
from NZA_Law.models import Lawyer, check_password_hash

# Flask Login import
from flask_login import login_required, login_user, current_user, logout_user

# Home route - Josh
@app.route('/')
def home():
    return render_template("index.html")

# Register route - Mike
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LawyerInfoForm
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username, password, email)
        user = Lawyer(username, email, password)
        db.session.add(user)
        db.session.commit()


# Create Case route - Leland


# Retrieve Case route - Stephanie


# Updating Case route - Stephanie


# Deleting Case route - Stephanie


# Login route - Josh


# Logout route - Josh