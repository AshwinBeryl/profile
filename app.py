from encodings.utf_8 import encode
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('ashwinberyl.html')

if __name__ == '__main__':
    app.run(debug=True)