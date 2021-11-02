rae = {}
rae['pizza'] = 'La mejor comida del mundo mundial'  # anadir items al diccionario
rae['pasta'] = 'La comida mas sabrosa de italia mama mia'

print(rae)

#Retornar el valor de un item del diccionario
print(rae['pizza'])

# Retornar un valor del diccionario con manejo de errores

print(rae.get('helado', None))  #Elemento no existente
print(rae.get('pasta', None))   #Elemento existente

#Retornar una lista de las llaves
print(rae.keys())

#Retornar una listade los valores
print(rae.values())

#Retornar una lista de los items
print(rae.items())


for key in rae.keys():
    print(key)

for key in rae.values():
    print(key)

for key,value in rae.items():
    print(key, value)