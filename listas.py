countries= ['Mexico', 'colombia','Venezuela', 'Argentina' ]

ages = [12,18,24,34,50]

print(id(countries))

print(id(ages))


receta =['Ensalada', 2, 'Lechugas', 5, 'jitomates']

countries[0] = 'Ecuador'

print(countries)

global_countries = countries

print(id(global_countries)) #Apunta al mismo lugar que countries

countries[0]= 'Guatemala'

print(id(countries))

print(global_countries) #Aqui obtuvimos nuestro primer bug

#Para evitarlo podemos utilizar 

import copy

global_countries = copy.copy(countries)

countries[0]= 'Holanda'

#De esta manera se copian las listas de forma adecuada
print(countries)
print(global_countries)

for coutry in countries:
    print(coutry)
