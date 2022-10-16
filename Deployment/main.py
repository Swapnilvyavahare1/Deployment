#pip install flask

from flask import Flask

#initialize the app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

#run the app
app.run()