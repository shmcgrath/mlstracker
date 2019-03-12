from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    team = {'fullname': 'DC United'}
    seasons = [
        {
            'competition': {'fullname': 'MLS Regular Season'},
            'year': 2018
        },
        {
            'competition': {'fullname': 'MLS Regular Season'},
            'year': 2017
        },
        {
            'competition': {'fullname': 'MLS Regular Season'},
            'year': 2016
        }
    ]

    return render_template('index.html', title='Team Homepage', team=team,
        seasons=seasons)
