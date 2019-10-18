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
    # print(x.make())
    return x.make()


# call the 'run' method
ui.run()
