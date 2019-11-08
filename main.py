from flask import Flask
from flask import request
from flask import Flask, render_template
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
    # route = request.url_rule
    # print(route)
    """data = {"persons": {'anna': {"age": 20}}}
    json.update(data, "test")"""
    return render_template('console.html')


@app.route("/Twitter")
def twitter():
    route = str(request.url_rule)
    """data = {"persons": {'anna': {"age": 100}}}
    json.update(data, "test")"""
    return render_template('twitter.html', route=route)


@app.route("/Twitter/Auto")
def tweet_auto():
    route = str(request.url_rule)
    return render_template('twitter-auto.html', route=route)


@app.route("/Twitter/New")
def tweet_new():
    route = str(request.url_rule)
    return render_template('twitter-new.html', route=route)


@app.route("/Settings")
def settings():
    return render_template('settings.html')


@app.route("/AJAX/Settings")
def ajaxed_settings():
    json.get("test/persons")
    json_data = json.result().items()
    return render_template('ajax_settings.html', data=json_data)


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
