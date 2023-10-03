from flask import Flask
import os

app = Flask("project")

from project.Controller import *

app.static_folder=os.path.abspath("static\\upload_photo")
app.static_url_path=''

UPLOAD_FOLDER = os.path.join("static","upload_photo")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
