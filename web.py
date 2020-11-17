import os
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import configparser
import io
import random #defaultne nainstalovany v python 3
#pip install matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import send_file

config = configparser.ConfigParser()
config.read('./settings/config_local.ini')
print(config['DATABASE']['STRING'])

app = Flask(__name__)

@app.route('/')#,methods=['POST','GET']
def index():
    return render_template("index.html")

@app.route('/fig/')
def fig():
    fig = create_figure()
    img = io.BytesIO()
    
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')



def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == "__main__":
    app.run(debug=True)
