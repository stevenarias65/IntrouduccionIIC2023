oracion = "Hola como esta mi nombre es ronald"

lista = oracion.split()

lista[lista.index("ronald")] = "Brandom"

nuevaOracion = " ".join(lista)

print(nuevaOracion)


