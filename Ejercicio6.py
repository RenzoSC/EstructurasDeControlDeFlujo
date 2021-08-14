"""Programa que lea un carácter por teclado y compruebe si es una letra mayúscula."""
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letra = input("Ingrese una letra:\n")

if letra in mayusculas:
    print("Es una letra mayúscula")
else:
    print("Es minúscula")

"""Otra forma:"""

from string import ascii_uppercase

if letra in ascii_uppercase:
    print("Es una letra mayúscula")
else:
    print("Es minúscula")