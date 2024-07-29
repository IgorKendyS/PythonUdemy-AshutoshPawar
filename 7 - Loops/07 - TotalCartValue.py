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
            print(f"{index}: {product['name']} : {product['description']} : ${product['price']} ")
 
        product_id = int(input("Enter the ID of the product you want to add to the cart:"))
 
        # Check if product already present in cart
        if products[product_id] in cart:
            # In this case, increase the quantity of the product rather than adding it to the cart
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])
 
        # Code to display the current cart contents, including the name, price, and quantity
        print("Here are the contents in your cart:")
        for product in cart:
            print(f"{product['name']} : {product['description']} : ${product['price']} : Quantity: {product['quantity']}")
 
    else:
        break
 
print(f"Thank you! Your final cart contents are: {cart}") 

total = 0
print("Here are the contents in your cart:")
for product in cart:
    print(f"{product['name']} : {product['description']} : ${product['price']} : Quantity: {product['quantity']}")
    total = total + (product['price'] * product['quantity'])
print(f"Cart total is: ${total}")