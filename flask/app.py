from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def startup():
  return "aggregate data here"

@app.route("/keepalive")
@cross_origin()
def keepalive():
    return "non aggregate data"

if __name__ == "__main__":
  app.run()
