# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True)
import pyscreenshot
import flask
from io import BytesIO

app = flask.Flask(__name__)

@app.route('/screen.png')
def serve_pil_image():
    img_io = BytesIO()
    pyscreenshot.grab().save(img_io, 'PNG', quality=50)
    img_io.seek(0)
    return flask.send_file(img_io, mimetype='image/png')

@app.route('/')
def serve_img():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)