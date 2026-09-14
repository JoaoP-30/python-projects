# Simple Calculator

# Esse programa é uma calculadora simples que permite ao usuário 
# realizar operações básicas de adição, subtração, multiplicação e divisão entre dois números. 
# O usuário insere os números e o operador desejado, e o programa exibe o resultado da operação.

operator = input("Enter operator (+, -, *, /): ")

if operator not in ('+', '-', '*', '/'):
    print("Invalid operator!")

else:    
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    if operator == '+':
        print(str(num1) + " " + operator + " " + str(num2) + " = " + str(num1 + num2))


    if operator == '-':
        print(str(num1) + " " + operator + " " + str(num2) + " = " + str(num1 - num2))


    if operator == '*':
        print(str(num1) + " " + operator + " " + str(num2) + " = " + str(num1 * num2))
        

    if operator == '/':
        
        if num2 == 0:
            print("It's not possible to divide by 0!")
        else:
            print(str(num1) + " " + operator + " " + str(num2) + " = " + str(num1 / num2))
