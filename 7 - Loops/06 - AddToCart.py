products = [
    {"name": "Smartphone", "price": 500, "description": "A handheld device used for communication and browsing the internet."},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that is easy to carry around."},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music."},
    {"name": "Smartwatch", "price": 300, "description": "A wearable device used for fitness tracking and receiving notifications."},
    {"name": "Bluetooth speaker", "price": 100, "description": "A portable speaker that connects wirelessly to devices using Bluetooth technology."}
]
cart = []
 
while True:
    choice = input("Do you want to continue shopping? ")
 
    if choice == "y":
        print("Here is a list of products and their prices:")
        for index, product in enumerate(products):
            print(f"{index}: {product['name']}: {product['description']}: ${product['price']}")
        product_id = int(input("Enter the ID of the product you want to add to the cart: "))
        cart.append(products[product_id])
        print(f"Current cart contents are: {cart}")
    else:
        break
    
print("Here are the contents in your cart:")
for product in cart:
    print(f"{product['name']}: ${product['price']}")