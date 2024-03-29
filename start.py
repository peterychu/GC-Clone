from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('//')
def new():
    return 'This is an added line!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
