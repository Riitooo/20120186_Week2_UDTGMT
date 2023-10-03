from project import app
from flask import Flask, render_template, flash, redirect, request
from project.Model.model import ImageProcessor


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} 

#app = Flask(__name__,template_folder='../templates')

image_processor = ImageProcessor(app)


@app.route('/')
def upload_page():
    return render_template('../templates/index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        full_og_filename, full_gs_filename = image_processor.process_image(f)
        print(full_og_filename)
        print(full_gs_filename,"\n")

    return render_template("upload.html", og_image=full_og_filename, gs_image=full_gs_filename)
