"""Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente."""

meses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
num = int(input("Dame un número del 1 al 12\n"))
print("La cantidad de días que tiene el mes que elegiste son... " + str(meses[num]), "dias")