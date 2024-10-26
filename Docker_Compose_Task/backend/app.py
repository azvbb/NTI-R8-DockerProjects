from flask import Flask, request
from pathlib import Path

app = Flask(__name__)
data_file = Path("/app/data/data.txt")

@app.route('/save', methods=['POST'])
def save():
    text = request.form['text']
    with data_file.open("a") as f:
        f.write(text + "\n")
    return 'Text saved.'

app.run(host='0.0.0.0', port=5000)
