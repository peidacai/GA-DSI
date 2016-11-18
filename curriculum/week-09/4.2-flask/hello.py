import flask
app = flask.Flask(__name__)

@app.route('/')
def hello():
    return '''
    <body>
    <h2> Hello World! blah </h2>
    </body>
    '''


@app.route('/greet/<name>')
def greet(name):
    "Say hello to your first parameter"
    print hello()
    print 'aaa'
    return "Hello, %s!" %name

if __name__ == '__main__':
    app.run(debug = True)