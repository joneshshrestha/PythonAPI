# Import the frameworks
from flask import Flask, jsonify, request

# Create an instance of Flask
app = Flask(__name__)

@app.route('/')
def index(): 
    return("hello")

app.run(debug=True)