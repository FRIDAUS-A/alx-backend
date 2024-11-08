#!/usr/bin/env python3
"""
     you will create a Config class that has a
     LANGUAGES class attribute equal to ["en", "fr"]
"""
from flask import Flask
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
