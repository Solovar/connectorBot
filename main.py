from flask import Flask
from flask import request
from flaskwebgui import FlaskUI  # get the FlaskUI class
from classes.MakeVisual import MakeVisual
from classes.JsonData import JsonData


app = Flask(__name__, static_url_path='/static')

# Feed it the flask app instance (check bellow what param you can add)
ui = FlaskUI(app)


# do your logic as usual in Flask

@app.route("/")
def index():
    x = MakeVisual()
    x.add_html_from_file('console')
    return x.printing()


@app.route("/Twitter")
def twitter():
    x = MakeVisual()
    x.add_html_from_file('twitter')
    return x.printing()


@app.route("/Twitter", methods=['POST'])
def twitter_post():
    x = MakeVisual()
    x.add_html_from_file('twitter')
    return x.printing()


@app.route("/Twitter/Auto")
def tweet_auto():
    x = MakeVisual()
    x.add_html_from_file('twitter-auto')
    return x.printing()


@app.route("/Twitter/New")
def tweet_new():
    x = MakeVisual()
    x.add_html_from_file('twitter-new')
    return x.printing()


@app.route("/Settings")
def settings():
    x = MakeVisual()
    x.add_html_from_file('settings')
    return x.printing()


'''
@app.route("/get/<json_file_name>")
def json_get(json_file_name):
    
    return x.printing()
 '''
# call the 'run' method
ui.run()
