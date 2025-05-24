import flask

app = flask.Flask(__name__)

@app.route('/')

@app.route('/')
def index():
    return "Hello I'm your flask server with Ai redirecting to the right place"

if __name__ == '__main__':
    app.run(debug=True)
