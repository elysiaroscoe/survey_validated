from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def display_survey():
    return render_template("index.html")

@app.route('/post_survey', methods = ["POST"])
def post_survey():
    Dojo.submit_survey(request.form)
    return redirect(f"/result/{id}")

@app.route("/result/<int:id>")
def display_result(id):
    dojo = Dojo.get_survey({"id" : id})
    return render_template('result.html', dojo = dojo)