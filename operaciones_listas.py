
a=[8,2]
b=[4,2] 

print('Lista 1: ' + str(a))
print('Lista 2: ' + str(b))

# + el operador suma concatena 2 o mas listas
print(a+b)

# * el poerador multiplicacion repite la lista
print(b*3)

#Operaciones con lsitas

#append agrega valores a la lista
a.append(6)
print(a)

#Extender lista agregando iterables
#a.extend(5)
#print(a)

#insert inserta un valor en una posicion deseada de la lista
a.insert(1,9)
print(a)


#saber el primer indice de un elemento en lista
print(a.index(9))

#Eliminar ultimo elemento de la lista
b.pop()
print(b)

#Contar el numero de veces que un elemento aparece en una lista
a.append(9)
print(a)
print(a.count(9))
print(a.count(0))

#invertir el orden de la lista
a.reverse()
print (a)

#ordenar una lista de menor a mayor
a.sort()
print(a)

#Ordenar lista de mayor a menor
#a.sorted()
#print(a)

#Eliminar elemento utilizando slices
del a[-1]
print(a)

#Eliminar un metodo por su valor
a.remove(2)
print(a)

#eliminar todos los elementos de una lista
a.clear()
print(a)

#iterar una lista
a=list(range(0,10))
b=list(range(0,100,2))

c =list(range(0,100,2))

print(c)

import random
#Crear datos aleatorios en una lista
random_number =[]
for i in range(10):
    random_number.append(random.randint(0,15))

#Saber los metodos que podemos ejecutar sobre una lista

dir(random_number)