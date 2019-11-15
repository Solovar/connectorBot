from flask import Flask, request, render_template
from flaskwebgui import FlaskUI  # get the FlaskUI class
from classes.JsonData import JsonData


app = Flask(__name__, static_url_path='/static')

# Feed it the flask app instance (check bellow what param you can add)
ui = FlaskUI(app)
json = JsonData.getinstance('static/Json')


# do your logic as usual in Flask
# Normal Routing
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

# Ajax
@app.route("/AJAX/Settings")
def ajaxed_settings():
    json.get("test/persons")
    json_data = json.result().items()
    return render_template('ajax_settings.html', data=json_data)


@app.route("/AJAX/show_tweets/<action>", methods=['GET'])
def ajaxed_tweet(action):
    if action is "auto":
        json.get("twitter/automatedTweet/tweets")
    elif action is "tweet":
        json.get("twitter/watch/tweets")
    return render_template("ajax_show-tweet.html", action=action, data=json.result().items())

'''
@app.route("/get/<json_file_name>")
def json_get(json_file_name):
    
    return x.printing()
 '''
# call the 'run' method
ui.run()
