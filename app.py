# app.py
from flask import Flask, render_template, jsonify
import random
from dotenv import load_dotenv
load_dotenv()  # Automatically looks for a .env file in the current directory or parent directories


app = Flask(__name__)

# List of gifts
gifts = [
    {"image": "static/img/pouch.jpg", "description": "🎁 A Roll-up pencil case!"},
    {"image": "static/img/throw.jpg", "description": "🎁 A Throw!"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_gift', methods=['GET'])
def get_gift():
    selected_gift = random.choice(gifts)
    return jsonify(selected_gift)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
