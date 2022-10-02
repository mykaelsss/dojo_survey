
from flask import Flask, render_template, request, redirect, session
# Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'anothersecretkeythatyoushouldntbesearchingfor'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html") # Return the string 'Hello World!' as a response


@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    print(request.form)
    return render_template("results.html", name = session['name'], location = session['location'], language = session['language'], comments = session['comments'])


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, port=5001)    # Run the app in debug mode.
