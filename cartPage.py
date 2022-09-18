import requests
import json
class cart:
    def __init__(self):
        self.url = 'https://api.demoblaze.com/'
        self.idprod=""
    def viewAllTheProductsInTheCart(self,userName):
        payload = json.dumps({
            "cookie": str(userName),
            "flag": True
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url+"viewcart", headers=headers, data=payload)
        return json.loads(response.text)["Items"]
    def viewDetailsOfAProduct(self,idProduct):
        payload = json.dumps({
            "id": idProduct
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url+"view", headers=headers, data=payload)
        return json.loads(response.text)