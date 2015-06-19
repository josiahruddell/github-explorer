from flask import Flask, render_template
from flask.ext.restful import Api
from src import api
from src import config


app = Flask(__name__,
    template_folder='src/client',
    static_folder='src/client/static')

# sets configuration (static for this app)
# but would read from an environment variable, etc
c = config.init(app)

# flask-restful app
api_app = Api(app)

# sets up routes to resource mapping
api.init(api_app)

@app.route('/')
def index_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080)