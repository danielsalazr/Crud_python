#tuplas 

#Declaraciones
a = 1,2,3

b= (1,2,3)

print(a[0])
print(a[2])

#Asignacio invalida debido a que las tuplas son inmutables
#a[0] = 10

#metodos tuple

c = (1,1,1,2,3,4)

print(c.count(1)) #Cuenta cuntas veces existe el elemento
print(c.index(2)) #nos indica el indice del elemento en el que aparece por primera vez


# Conjuntos

a = set([1,2,3])
b={3,4,5}  #se parece al diccionario peero no lo es 

#metodo invvalido debido a que los set o conjuntos no tienen un orden implicito
#print(a[1])

#anadir 3 en el conjunto es vano debido a que los conjuntos no pueden repetir elemntos
a.add(3)

a.add(20)
print(a)

#Interseccion
print(a.intersection(b))

#union
print(a.union(b))

#Diferencio
print(a.difference(b))

#eliminar elementos del conjunto
a.remove(20)
print(a)

"""  operadores para sets
>>> A = {1, 2, 3}	# conjunto A
>>> B = {3, 4 ,5}	# conjunto B
>>> A | B		#unión
{1, 2, 3, 4, 5}
>>> A & B	# intersección
{3}
>>> A - B		# diferencia entre A y B
{1, 2}
>>> B - A		# diferencia entre B y A
{4, 5}
"""