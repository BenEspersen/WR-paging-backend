from flask import Flask

app = Flask(__name__)

@app.after_request
def configure_origin(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    return resp

@app.route("/")
def API_online():
    return "API Online!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1335, debug=True)