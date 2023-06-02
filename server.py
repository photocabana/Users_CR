from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models import user
from flask_app.controllers import users #controllers go here
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    return render_template("read.html", user = user.User.get_user())

@app.route('/second')
def second_page():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_page():
    user.User.new_user(request.form)
    return redirect('/')



if __name__=="__main__":   
    app.run(debug=True) 

# debug needs to be set to False when deployed.
# We shared a video showing how the information leaked by this feature and help hackers.

