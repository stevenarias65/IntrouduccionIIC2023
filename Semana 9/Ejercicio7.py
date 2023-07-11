diccionario = {'nombre' : 'Carlos', 
               'edad' : 48, 
               'cursos': ['Python','Fortran','Matlab']
              }


print(diccionario['edad'])

colores = {
    "Amarillo" : "Yellow",
    "Verde" : "Green",
    "Azul" : "Blue",
    "Rojo" : ["red","Rojito","Otro Rojo"]
}

print(colores["Rojo"][2])

colores["Blanco"] = "white"

colores["Rojo"].append("rojo Obligado")

print(colores["Rojo"])