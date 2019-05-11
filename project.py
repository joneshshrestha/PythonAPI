from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/tokens', methods=['POST','GET'])
def entry_page():
    return jsonify({'about': 'hello world!'})

app.run(debug=True)