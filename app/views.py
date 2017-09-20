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
    return render_template(
        'stock.html',
        name="Spasmalgon",
        qt="1",
        form="Tablet",
        action="Spasmolytic drugs"
    )
