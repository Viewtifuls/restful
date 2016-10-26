# -*- coding: utf-8 -*-

DEFAULT_PORT = 5000
ADDITIVE_FOR_UID = 1000

try:
    from os import getuid

except ImportError:
    def getuid():
        return DEFAULT_PORT - ADDITIVE_FOR_UID

from flask import Flask, render_template, request, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS


app = Flask(__name__)


def count_tags(url):
    protocol = 'http://'
    if url[0:4] != protocol[0:4]:
        url = protocol + url
    try:
        page = urlopen(url).read().decode()
        soup = BS(page)
        count = 0
        for tag in soup.findAll():
            count += 1
    except:
        count = 'Try something else'
    return count


@app.route('/')
def index():
    return render_template('index.html', url = request.args.get('url'))


@app.route('/data')
def data():
    url = request.args.get('url')
    number = count_tags(url)
    return jsonify({"url": url, "number": number})


if __name__ == '__main__':
    app.run(port=getuid() + ADDITIVE_FOR_UID, debug=True)
