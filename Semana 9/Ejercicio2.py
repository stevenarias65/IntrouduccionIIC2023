lista = [20,65,12,2,8,65,48,1,5,8]
pares=[]
impares = []
contador = 0

while contador < len(lista):

    if lista[contador] %2 == 0:
        pares.append(lista[contador])
    else:
        impares.append(lista[contador])
    contador = contador +1 


print(pares,impares)
