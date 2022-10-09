
from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html") # Return the string 'Hello World!' as a response


@app.route('/process', methods=['POST'])
def process():
    if Dojo.is_valid(request.form):
        Dojo.create_dojo(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def results():
    return render_template("results.html", dojo= Dojo.get_last_dojo())
