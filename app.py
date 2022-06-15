from encodings.utf_8 import encode
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)