from flask import Flask, request, json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

content = "tmp"

@app.route("/", methods = ['GET', 'POST'])
@cross_origin()
def startup():
  return content

@app.route("/keepalive", methods = ['GET', 'POST'])
@cross_origin()
def keepalive():
    return "non aggregate data"

content = "tmp"
@app.route("/update", methods = ['GET', 'POST'])
@cross_origin()
def update():
    global content
    content = request.data
    print(request.data)
    return content


if __name__ == "__main__":
    app.run(host='0.0.0.0')
