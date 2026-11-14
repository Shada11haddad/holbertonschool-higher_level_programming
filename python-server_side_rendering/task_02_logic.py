#!/usr/bin/python3
"""Task 2: dynamic template with loops and conditions."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items list read from items.json."""
    try:
        with open('items.json', 'r') as f:
            item_list = json.load(f).get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
