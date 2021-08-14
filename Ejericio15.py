"""Dado una lista, hacer un programa que indique si está ordenada o no."""

lista = []
bandera = True
while bandera:
    numero = input("Ingresa un número.\nIngrese 'q' para terminar\n")
    if numero == "q":
        bandera = False
    else:
        lista.append(int(numero))

listadeverdad = lista.copy()
lista.sort()

if listadeverdad == lista:
    print("Está ordenado")
else:
    print("No está ordenado")