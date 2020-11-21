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
from flask import send_file, session
from flask_session import Session

config = configparser.ConfigParser()
config.read('./settings/config_local.ini')
print(config['DATABASE']['STRING'])



app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')#,methods=['POST','GET']
def index():
    session['sequence'] = 0


    session['xs'] = range(100)
    session['ys'] = [random.randint(1, 50) for x in session['xs']]
    return render_template("index.html",len = len(session['ys']),Pokemons =session['ys'])

@app.route('/fig/')
def fig():
    fig = create_figure()
    img = io.BytesIO()
    
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')



def create_figure():
    #global xs
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(session['xs'], session['ys'])
    return fig

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
