inventario = {

    "pam1" : {
        "cantidad" : 10,
        "color" : "Azul",
        "Talla" : "L"
    },
    "pam2" : {
        "cantidad" : 20,
        "color" : "Verde",
        "Talla" : "M"
    }
}


for i,j in inventario.items():
    print(i,"->",j["cantidad"])

print("Agregue el producto")
codigo = input()
color = input()
Talla = input()
Cantidad = input()

inventario[codigo] = {"cantidad":Cantidad,
                      "color": color,
                      "Talla": Talla}

for i,j in inventario.items():
    print(i,"->",j["cantidad"])


