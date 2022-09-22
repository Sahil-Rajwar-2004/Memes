from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    res = json.loads(requests.request("GET",url).text)
    meme_large = res["preview"][-2]
    subreddit = res["subreddit"]
    return meme_large,subreddit

@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html",meme_pic = meme_pic,subreddit = subreddit)

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug = True)

