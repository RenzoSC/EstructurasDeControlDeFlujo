"""Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
Muestra el máximo de los números guardado en la lista, muestra los números pares."""
bandera = True
list_num = []
while bandera:
    numero = int(input("Ingresa un número\n"))
    if numero >=0:
        list_num.append(numero)
    else:
        bandera=False
print(list_num)
print("El número más grande entre los que diste fue " + str(max(list_num)))
print("Los números pares entre los que me diste son:\n")
for i in list_num:
    if i%2 == 0:
        print(i, end=", ")
    else:
        pass