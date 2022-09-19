import requests
import json

class cart:
    def __init__(self):
        self.url = 'https://api.demoblaze.com/'
        self.idprod=""
    def addToCartItem(self,userToken):
        with open("items.txt","r") as file:
            item = file.readline()
        payload = json.dumps({
            "id": json.loads(item)["id"],
            "cookie": userToken,
            "prod_id": json.loads(item)["prod_id"],
            "flag": True
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url + "addtocart", headers=headers, data=payload)
        return response.text
    def viewAllTheProductsInTheCart(self,userToken):
        payload = json.dumps({
            "cookie": str(userToken),
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
