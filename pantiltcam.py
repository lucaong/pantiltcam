#!/usr/bin/env python

import pantilthat
from sys import exit

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

app = Flask(__name__)

@app.route('/api/angles', methods=['GET'])
def get_angles():
    pan = pantilthat.get_pan()
    tilt = pantilthat.get_tilt()
    return '{{"pan":{}, "tilt":{}}}'.format(pan + 90, tilt + 90)

@app.route('/api/<direction>/<int:angle>', methods=['POST'])
def set_angle(direction, angle):
    if angle < 0 or angle > 180:
        return '{"error": "out of range"}'

    angle -= 90

    if direction == 'pan':
        pantilthat.pan(angle)
        return '{{"pan":{}}}'.format(angle + 90)

    elif direction == 'tilt':
        pantilthat.tilt(angle)
        return '{{"tilt":{}}}'.format(angle + 90)

    return '{"error": "invalid direction"}'

@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == "__main__":
    app.run(port=9595)
