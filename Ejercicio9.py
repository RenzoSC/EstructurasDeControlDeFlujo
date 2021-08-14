"""Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
El programa termina cuando se acierta el número."""

adivinar = int(input("Dame un numero para adivinar\n"))

respuesta = int(input("Intenta adivinar el número\n"))

while adivinar != respuesta:
    if respuesta < adivinar:
        print("El numero que diste es menor al que intentas adivinar")
        respuesta = int(input("Intentalo de nuevo\n"))
    elif respuesta > adivinar:
        print("El numero que diste es mayor al que intentas adivinar")
        respuesta = int(input("Intentalo de nuevo\n"))
    else:
        break
print("PERFECTO LO ADIVINASTE")