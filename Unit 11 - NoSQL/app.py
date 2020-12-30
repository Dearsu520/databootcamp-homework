from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars as sm

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    high_res_img = [(i['img_url'], i['title']) for i in mars_data['high_resolution_images']]
    return render_template("index.html", mars_data=mars_data, high_res_img=high_res_img)

@app.route("/scrape")
def scrape():
    updated_mars_data = sm.scrape_all()
    mongo.db.mars_data.update({}, updated_mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)