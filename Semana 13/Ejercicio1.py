try:
    numero1 = 2
    numero2 = 3
    lista = [1,2,3,4]
    diccionario = {"nombre" : "Ronald"}
    #numero2 = int(input())
    print(numero1/numero2)

    print(lista[3])
    print(diccionario["nombre"])
    print("Hola mundo")

except ZeroDivisionError:
    print("Error, no se puede dividir entre 0")
except TypeError:
    print("Error, Deben de ser numeros para poder dividir")
except IndexError:
    print("Error, Indice no existe")
except KeyError:
    print("Error, Clave no existe en el diccionario")
except Exception:
    print("Error, ha ocurrido un error, verique la informacion")
else:
    print("Se ejecuta si no hay errores")


