# -*- coding: utf-8 -*-

try:
    from os import getuid

except ImportError:
    def getuid():
        return 4000

from flask import Flask, request, render_template
from pprint import pformat

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template(
		"index.html",
		username=request.args.get('name', 'Anonymous')
		
	)
	
@app.route("/test/<int:first>")
@app.route("/test/<int:first>/<int:second>")
def divides(first, second=3):
	second = int(request.args.get('second', 0))
	return "Yes" if number % second == 0 else "Now"

@app.route("/test/<anyhing>")
def anything_str(anything):	
	return anything
@app.route("/hello/")
@app.route("/hello/<username>")
def hello(username='Anonymus'):
	return "HELLO, {}".format(username)


if __name__ == "__main__":
    app.run(port=getuid() + 1000, debug = True)