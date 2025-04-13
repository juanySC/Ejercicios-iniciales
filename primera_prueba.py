#usando sets para los conjutos

tv = {'Annelis', 'Anibal', 'Lalo', 'Elsa'}
fut = {'Anibal', 'Willys', 'Lalo', 'Elsa'}
maquillaje = {'Annelis', 'Juany', 'Elsa'}

#union de conjuntos

unionPer = tv| fut | maquillaje
print("Union")
print(unionPer)
#cuenta el numero de personas
print(len(unionPer)) 

#interseccion de conjuntos (quienes comparten gustos)
print("Interseccion")
interPer = tv & fut & maquillaje

print(interPer)
print(len(interPer))

#diferencia en conjuntos (quita elementos repetidos)
print("Diferencia")
difPer1 = fut - tv
difPer2 = tv - maquillaje

print(difPer1)
print(len(difPer1))
print(difPer2)
print(len(difPer2))

#diferencia simetrica  (que estan en uno o en otro, pero no en ambos)
print("Diferencia simetrica")
dsPer = tv ^ fut

print(dsPer)
print(len(dsPer))

#si quiero que solo les guste una cosa por ejemplo del fut
print("Solo le gusta el futbol")
uno = fut - maquillaje - tv
print(uno)
