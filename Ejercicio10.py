"""Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5."""

numeros = [1,2,3,4,5]

for i in numeros:
    print("Esta es la tabla de multiplicar del " + str(i))
    print("=============================================")
    for x in range(1,11):
        print(i*x)


