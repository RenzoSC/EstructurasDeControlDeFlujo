"""Pedir un número por teclado y mostrar la tabla de multiplicar"""

num = int(input("Dame un número\n"))

print("La tabla de multiplicar del número " + str(num) + "es: ")

for i in range(1,11):
    print(num * i)