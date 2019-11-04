from flask import Flask
from flask import request
from flaskwebgui import FlaskUI  # get the FlaskUI class
from classes.MakeVisual import MakeVisual
from classes.JsonData import JsonData


app = Flask(__name__, static_url_path='/static')

# Feed it the flask app instance (check bellow what param you can add)
ui = FlaskUI(app)
json = JsonData.getinstance('static/Json')


# do your logic as usual in Flask

@app.route("/")
def index():
    x = MakeVisual()
    """data = {"persons": {'anna': {"age": 20}}}
    json.update(data, "test")"""
    x.add_html_from_file('console')
    return x.printing()


@app.route("/Twitter")
def twitter():
    x = MakeVisual()
    """data = {"persons": {'anna': {"age": 100}}}
    json.update(data, "test")"""
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
    x.add_script('settings.js')
    x.add_html_from_file('settings')
    return x.printing()


@app.route("/AJAX/Settings")
def ajaxed_settings():
    x = MakeVisual()
    json.get("test/persons")
    return_data = ''
    for key, val in json.result().items():
        return_data += "<li>" + key + " is: " + str(val['age']) + " years old</li>"
    x.add_plain_html(return_data)
    return x.ajax_priting()


@app.route("/AJAX/show_tweets")
def ajaxed_tweet():
    x = MakeVisual()
    json.get("test/persons")
    return_data = ''
    for key, val in json.result().items():
        return_data += "<li>" + key + " is: " + str(val['age']) + " years old</li>"
    x.add_plain_html(return_data)
    return x.ajax_priting()

'''
@app.route("/get/<json_file_name>")
def json_get(json_file_name):
    
    return x.printing()
 '''
# call the 'run' method
ui.run()
