import json

from flask import Flask, Response

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello, world!"

@app.get("/hello/<int:times>")
def repeat_hello(times):

    try: 
        message = "Hello, world!\n" * times
        return Response(message, mimetype="text/plain")

    except ValueError:
            response = {
                "message": "Invalid number as addend",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)