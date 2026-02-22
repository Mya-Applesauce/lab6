shopping_cart = {}

print(f"Hail and well met! Welcome to mine infinite store! We hath ev'rything thy heart desireth, and many things it doth not! Simply entere whatsoever thou wisheth, and it shalt be provided. Thou mayest also entere ""view"" to gaze upon thine cart at any time. Entere ""checkout"" when thou art finished.")

active = True
while active:
    item = input(f"What dost thou seeketh?")
    if (item == "checkout") or (item == "Checkout"):
        active = False
    elif (item == "View") or (item == "view"):
        print(f"++THINE CART++")
        for thing in shopping_cart:
            print(f"{thing}: {shopping_cart[thing]}")
        print(f"++++++++++++++")
    else:
        quantity = int(input(f"How many?"))
        if item not in shopping_cart:
            shopping_cart[item] = quantity
        else:
            shopping_cart[item] += quantity
        print(f"*{shopping_cart[item]} {item} hath been added to thine cart.")

print("++THINE FINAL CART++")
for thing in shopping_cart:
            print(f"{thing}: {shopping_cart[thing]}")
print("++++++++++++++++++++\n")
print("I thanketh thee for thy patronage!")