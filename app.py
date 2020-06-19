from flask import Flask, render_template, request, send_file, redirect, url_for, after_this_request, abort
import os
import time
from werkzeug.utils import secure_filename
import uuid
from time import sleep
from license import *

UPLOAD_FOLDER = './files/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file_name = ''

value = False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', message = 'Attribution')

def delete(value):
    return value

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputfile']

    if file and file.filename != '' and allowed_file(file.filename):
        filename = str(uuid.uuid4())
        file_name = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print (f'saved as {filename}')
        ret = outhtml(UPLOAD_FOLDER + filename, UPLOAD_FOLDER + filename + '.html', 'My prod')

        if ret: 
            return render_template('wait.html', reffile = filename)
        else:
            return render_template('index.html', message="Wrong File. You can only upload the components.csv file from the BD report")

    return render_template('index.html', message="Wrong File. You can only upload the components.csv file from the BD report")

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    path = UPLOAD_FOLDER + filename + '.html'
    print (f'File name with path = {path}')

    @after_this_request
    def remove_file(response):
        os.remove(path)
        os.remove(UPLOAD_FOLDER + filename)
        return response

    return send_file(path, as_attachment=True)
    
@app.errorhandler(500)
def internal_server_error(e):
    return "Corrupted File!", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')