"""Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
 excepto que también sea divisible por 400."""

año = int(input("Dame un año\n"))

if (año%4 == 0 and not (año%100 ==0)) or año%400==0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")