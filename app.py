from flask import Flask
from flask import request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/trusted')
def trusted():
    return render_template('trusted.html')


@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/real')
def real():
    return render_template('real.html')


if __name__ == '__main__':
    app.run()
