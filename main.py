from flask import Flask
from flaskwebgui import FlaskUI  # get the FlaskUI class
from classes.MakeVisual import MakeVisual


app = Flask(__name__)

# Feed it the flask app instance (check bellow what param you can add)
ui = FlaskUI(app)


# do your logic as usual in Flask

@app.route("/")
def index():
    x = MakeVisual()
    x.add_html('console')
    return x.print()


@app.route("/Twitter")
def twitter():
    x = MakeVisual()
    x.add_html('twitter')
    print(x.print())
    return x.print()


@app.route("/Settings")
def settings():
    x = MakeVisual()
    x.add_html('settings')
    return x.print()


# call the 'run' method
ui.run()
