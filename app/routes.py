# import app variable instance in order to run application
# also import necessary flask methods
from app import app
from flask import render_template, url_for, redirect



# create route for index page, render index.html file
@app.route('/')
@app.route('/index')
@app.route('/index/<name>', methods=['GET'])
def index(name=''):
    return render_template('index.html', name=name, title='Home')

@app.route('/data')
@app.route('/data/<flag>', methods=['GET'])
def data(flag=False):
    sports = ['Baseball', 'Football', 'Basketball', 'Hockey']
    stats = {
        'David Ortiz': 540,
        'Hank Aaron': 734,
        'Babe Ruth': 690,
        'Sammy Sosa': 605,
        'Mark McGwire': 580
    }

    print(type(flag))


    # print(sports)
    # # when call print within function, prints to debugging terminal

    return render_template('data.html', title='Data', sports=sports, stats=stats, flag=flag)


@app.route('/redirection')
def redirection():
    return redirect(url_for('index'))
