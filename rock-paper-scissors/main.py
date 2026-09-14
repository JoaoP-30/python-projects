# Rock-Paper-Scissors Game

# Este é um jogo de Pedra-Papel-Tesoura que permite ao usuário jogar contra o computador.

import random

options = ("pedra", "papel", "tesoura")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Escolha uma opção (pedra, papel, tesoura): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Empate!")
    elif player == "pedra" and computer == "tesoura":
        print("Você ganhou!")
    elif player == "papel" and computer == "pedra":
        print("Você ganhou!")
    elif player == "tesoura" and computer == "papel":
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    if not input("Jogar novamente? (s/n): ").lower() == "s":
        running = False 

print("Até a próxima!")