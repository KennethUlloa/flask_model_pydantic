import requests


data = {
    "email": "email@correo.com",
    "password": "1234"
}


response = requests.post("http://localhost:5000/login", json=data)

print(response.json())