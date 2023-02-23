import random

lista_nombres = ["Ithamar", "Leo", "Nacho", "Allan", "Jose", "Cris", "Carlos"]

random.shuffle(lista_nombres)


for indice, nombre in enumerate(lista_nombres):
    print(indice, nombre)

# 0 Allan
# 1 Jose
# 2 Cris
# 3 Nacho
# 4 Ithamar
# 5 Leo
# 6 Carlos