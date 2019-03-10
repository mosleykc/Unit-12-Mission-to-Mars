# this file will execute the scrape_mars file
# referencing 12.3.9 and 12.3.10 exercises 
# import dependencies
from flask, import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# create app engine
app = Flask(__name__)

# set up mongo connection and create pymongo app called mars_app
mongo = PyMongo(app, uri ="mongodb://localhost:27017/mars_app")

# create a route called `/scrape` that will import `scrape_mars.py` script and call `scrape` function
@app.route("/scrape")
def scrape():
    # define collection to use
    scrape_mars_data = mongo.db.scrape_mars_data

    # define scrape method and return the dictionary object 
    mars_data = scrape_mars.scrape()

    # add the object to the DB using .update to updat all {}, set upsert to False so not to create a new document each run
    scrape_mars_data.update{}, mars_data, upsert=False

    # use redirect to send code 302 to client and go back to the homepage when complete
    return redirect("/",code=302)

# create route that renders index.html template, the "/" means homepage of webside, use def to define echo
@app.route("/")
def index()
    # use the find_one query method and the return render_template to take in the filename index.html and the content 
    # of scrape_mars_data
    scrape_mars_data = mongo.db.scrape_mars_data.find_one()
    return render_template("index.html",scrape_mars_data=scrape_mars_data)

# Python environment name prompt, 
if__name__ == "__main__":
    app.run(debug=True)
