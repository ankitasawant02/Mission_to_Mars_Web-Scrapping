# Import Dependencies
import os
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask app
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():

    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info = mars_info)

@app.route("/scrape")
def scrape():

    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)

