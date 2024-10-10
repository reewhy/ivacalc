from flask import *
from flask_cors import CORS, cross_origin
from PIL import Image
from werkzeug.utils import secure_filename

from fileinput import filename

from get_prices import process

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

name = 'test.png'
@app.route("/")
@cross_origin()
def homepage():
    global name
    process(name)
    return 'calculating'

@app.route('/success', methods = ['POST'])
def success():
    global name
    if request.method == 'POST':

        print(request.files)
        if 'newimg' not in request.files:
            print('No file part')
            return 'No file'
        file = request.files['newimg']

        if file:
            file.save('../' + file.filename)
            name = file.filename
    return ''

if __name__ == '__main__':
    app.run()