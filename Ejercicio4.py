"""Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error."""
import time

print("""Bienvenido a nuestra aplicación
====================================================
Por favor ingrese su usuario y contraseña""")
usuario = input("Ingrese un usuario\n")
contraseña = input("Ingrese una contraseña\n")
intentos = 0
while usuario != "pepe" or contraseña != "asdasd":
    print("Usuario o contraseña inválidos")
    intentos +=1
    if intentos > 3:
        print("Ha excedido el límite de intentos... Vuelva a intentarlo en 15s")
        time.sleep(15)
    usuario = input("Ingrese un usuario\n")
    contraseña = input("Ingrese una contraseña\n")
print("Bienvenido de vuelta " + usuario)

