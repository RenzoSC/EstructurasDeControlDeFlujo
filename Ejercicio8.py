"""Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de 
todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación.
 Por ejemplo 5! = 1x2x3x4x5=120"""
num = int(input("Ingrese un número para calcular su factorial\n"))
x = num
factorial = 1
while num>=1:
    factorial *= num 
    num -= 1
print("El factorial de " + str(x) + " es " + str(factorial))