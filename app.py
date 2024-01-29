from flask import Flask
from models import LoginRequest
from validator import validate_body


class IsADependency:
    def get_response(self):
        return {
            "response": "OK"
        }

app = Flask(__name__)

@app.post("/login")
@validate_body(body=LoginRequest)
def login(body, dependencia: IsADependency = IsADependency()):
    return dependencia.get_response()



if __name__ == "__main__":
    app.run(port=5000, debug=True)
