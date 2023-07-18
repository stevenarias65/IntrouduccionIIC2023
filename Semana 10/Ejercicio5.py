import os 

os.system("clear")

diccionario = {
                'nombre' : 'Carlos', 
                'edad' : 48, 
                'cursos': ['Python','Fortran','Matlab'] 
            }

Variable = diccionario.keys()
print(type(Variable))
print("Datos: ", Variable)
print(diccionario.keys())

for i in diccionario.keys():
    print("Impimiendo variable i",i)
print("---------------------")
for i in diccionario.values():
    print("Impimiendo variable i",i)
print("---------------------")

for clave,valor in diccionario.items():
    print("Impimiendo variable i",clave,valor)
