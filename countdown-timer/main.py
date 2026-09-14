# Countdown Timer

# Este programa de contagem regressiva permite que o usuário insira 
# um tempo em segundos e o programa exibirá a contagem regressiva em horas, 
# minutos e segundos. Quando o tempo chegar a zero, o programa exibirá uma mensagem indicando que o tempo acabou.

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x / 60)) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("TIME'S UP!")