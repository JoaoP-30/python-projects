# Shopping cart program

# Este programa de carrinho de compras permite que o usuário insira alimentos e seus preços,
# e depois calcula o total da compra. O usuário pode continuar adicionando alimentos até decidir 
# sair do programa, momento em que o total da compra é exibido.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("----- YOUR CART -----")


for food in foods:
    print(food, end = " ")


for price in prices:
    total += price

print("\n")

print(f"Your total is: ${total:.2f}")


print("----------------------")

