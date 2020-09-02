import flask


app = flask.Flask(__name__)


@app.route('/')
def main():
    return flask.render_template('index.html')


@app.route('/departures/<departure>/')
def departures():
    return flask.render_template('departure.html')


@app.route('/tours/<id>/')
def tours():
    return flask.render_template('tour.html')


app.run()
