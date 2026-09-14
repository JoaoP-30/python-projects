# Concession Stand

# Este programa simula um quiosque de lanches, permitindo que o usuário 
# selecione itens de um menu e calcule o total da compra.

menu = {"pizza": 3,
        "nachos": 4.50,
        "popcorn": 6,
        "fries": 2.50,
        "chips": 1,
        "pretzel": 3.50,
        "soda": 3,
        "lemonade": 4.25
}

cart = []
total = 0

print("---------------- MENU ----------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)


print("------------- Your Order ----------------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print("")
print(f"Total is: ${total:.2f}")