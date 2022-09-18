import loginPage
import cartPage

userToken=loginPage.login().loginUser("Yafi","108010")
cart=cartPage.cart()

def testIfNumberOfItemsInTheCardIsOne():
    numberOfItemsInTheCard = len(cart.viewAllTheProductsInTheCart(userToken))
    assert numberOfItemsInTheCard == 1

def testIfItemIdEqual3():
    idItem = cart.viewAllTheProductsInTheCart(userToken)[0]["prod_id"]
    cart.idprod = idItem
    assert idItem == 3
testIfItemIdEqual3()
def testIfThePriceOfTheSelectedPhoneEqual650():
    priceOfItem = cart.viewDetailsOfAProduct(cart.idprod)["price"]
    assert priceOfItem == 650

def testIfTheTitleOfTheSelectedPhoneIsNexus6():
    titleOfItem = cart.viewDetailsOfAProduct(cart.idprod)["title"]
    assert titleOfItem == "Nexus 6"
