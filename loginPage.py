import requests
import json
import base64


class login:
    def __init__(self):
        self.url = 'https://api.demoblaze.com/login'
    def loginUser(self,userName,password):
        samplePasswordBytes = password.encode("ascii")
        convertThePasswordToBase64Bytes = base64.b64encode(samplePasswordBytes)
        convertThePasswordToBase64String = convertThePasswordToBase64Bytes.decode("ascii")
        payload = json.dumps({
            "username": str(userName),
            "password": convertThePasswordToBase64String
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url, headers=headers, data=payload)
        return response.text.split(": ")[1][:-2]
