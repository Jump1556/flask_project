import json
import time

from flask import render_template

from app import application


@application.route('/')
def index():
    return "Hi"


@application.route('/pink')
def show_time():
    return render_template(
        'pink.html',
        now=time.strftime("%c")
    )


@application.route('/stock')
def stock():
    with open('app/data/stock.json') as data_file:
        data = json.load(data_file)
    print(data)
    return render_template(
        'stock.html',
        stocks=data
    )
