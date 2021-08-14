"""Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
 Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]."""

lista = input("Ingresa una oracion para convertir en lista\n")

listita = lista.split(" ")
print("La lista sería: ")
print(listita)
print("La lista al revés sería: ")
lista_invertida = listita[::-1]
print(lista_invertida)