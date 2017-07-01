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
