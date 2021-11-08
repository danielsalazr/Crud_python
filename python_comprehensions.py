lista_de_numeros = list(range(100))

print(lista_de_numeros)

#numeros pares List comprehensions
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)


#Dictionary comprehensions
student_uid =[1,2,3]
students = ['juan', 'jose','vladimir']
#con el comprehensions convertimos dos listas en un diccionario
student_with_uid = { uid: student for uid, student in zip(student_uid, students)}
print(student_with_uid)

#Set comprehensions
import random
random_numbers = []
for i in range(18):
    random_numbers.append(random.randint(1,3))
print(random_numbers)

#asignacion de numeros a un conjunto
non_repeated= {number for number in random_numbers}

print(non_repeated)