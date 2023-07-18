##Quiero hacer una lista de personajes del señor de los anillos

personales = []

p = {
    "nombre" : "Gandalf",
    "clase" : "Mago",
    "raza" : "Humano"
}

personales.append(p)

p = {
    "nombre" : "Legolas",
    "clase" : "Arquero",
    "raza" : "Elfo"
}

personales.append(p)

p = {
    "nombre" : "Gimli",
    "clase" : "Guerrero",
    "raza" : "Enano"
}

personales.append(p)

print(len(personales))

print(personales[0]["raza"])

