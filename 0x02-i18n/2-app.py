#!/usr/bin/env python3
"""
    Create a get_locale function
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel_localeselector
def get_locale():
    """browse the language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def welcome():
    """Welcome page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
