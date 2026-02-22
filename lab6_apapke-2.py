shopping_cart = {}

print(f"Welcome!")

active = True
while active:
    item = input(f"What")
    if (item == "checkout") or (item == "Checkout"):
        active = False
    elif (item == "View") or (item == "view"):
        print(f"++YOUR CART++\n")
    else:
        quantity = input(f"How many?")
        if item not in shopping_cart:
            shopping_cart[item] = quantity
            print(f"{item} {shopping_cart[item]}")