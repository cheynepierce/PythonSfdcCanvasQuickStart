import os
from canvas import app

from flask import Flask, render_template, request

from util import SignedRequest

@app.route('/', methods=['POST', 'GET'])
def main():
    consumer_secret = os.environ['CANVAS_CONSUMER_SECRET']
    signed_request = request.form['signed_request']
    sr = SignedRequest(consumer_secret, signed_request)
    request_json = sr.verifyAndDecode()
    return render_template('main.html', request_json=request_json)

@app.route('/callback')
def callback():
    return render_template('callback.html')
	
@app.errorhandler(500)
def serverError(e):
    return render_template('500.html'), 500