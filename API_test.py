import loginPage
import cartPage

cart = cartPage.cart()
user = loginPage.login()

def signUpUserAndloginUserAndaddToCartItem():
    user.signUpUser()
    userToken = user.loginUser()
    user.userToken = userToken
    cart.addToCartItem(user.userToken)

signUpUserAndloginUserAndaddToCartItem()

def testIfNumberOfItemsInTheCardIsOne():
    numberOfItemsInTheCard = len(cart.viewAllTheProductsInTheCart(user.userToken))
    assert numberOfItemsInTheCard == 1

def testIfItemIdEqual3():
    idItem = cart.viewAllTheProductsInTheCart(user.userToken)[0]["prod_id"]
    cart.idprod = idItem
    assert idItem == 3

def testIfThePriceOfTheSelectedPhoneEqual650():
    priceOfItem = cart.viewDetailsOfAProduct(cart.idprod)["price"]
    assert priceOfItem == 650

def testIfTheTitleOfTheSelectedPhoneIsNexus6():
    titleOfItem = cart.viewDetailsOfAProduct(cart.idprod)["title"]
    assert titleOfItem == "Nexus 6"
