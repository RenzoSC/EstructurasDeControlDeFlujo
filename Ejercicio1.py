"""Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero. """

a = int(input("Dame un número\n"))
b = int(input("Dame otro numero\n"))

if (a+b) >0:
    print("La suma es positiva")
elif (a+b) == 0:
    print("La suma da como resulado 0")
else:
    print("La suma es negativa")