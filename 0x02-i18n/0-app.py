#!/usr/bin/env python3
"""
    setup a basic Flask app in 0-app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
    """Welcome page"""
    return render_template('0-index.html')
