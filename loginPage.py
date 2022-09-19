import requests
import json
import base64

class login:
    def __init__(self):
        self.url = 'https://api.demoblaze.com/'
        self.userToken=""
    def loginUser(self):
        with open("users.txt","r") as file:
            user = file.readline()
        simplePasswordBytes = json.loads(user)["password"].encode("ascii")
        convertThePasswordToBase64Bytes = base64.b64encode(simplePasswordBytes)
        convertThePasswordToBase64String = convertThePasswordToBase64Bytes.decode("ascii")
        payload = json.dumps({
            "username": str(json.loads(user)["userName"]),
            "password": convertThePasswordToBase64String
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url+"login", headers=headers, data=payload)
        return response.text.split(": ")[1][:-2]
    def signUpUser(self):
        with open("users.txt","r") as file:
            user=file.readline()
        simplePasswordBytes = json.loads(user)["password"].encode("ascii")
        convertThePasswordToBase64Bytes = base64.b64encode(simplePasswordBytes)
        convertThePasswordToBase64String = convertThePasswordToBase64Bytes.decode("ascii")
        payload = json.dumps({
            "username": str(json.loads(user)["userName"]),
            "password": convertThePasswordToBase64String
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url+"signup", headers=headers, data=payload)
        return response.text



