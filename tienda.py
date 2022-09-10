
tienda = []
dato = 0
while dato != 5:
    menu = "Tienda \n​"
    menu += "1. Agregar producto\n"
    menu += "2. Mostrar productos\n"
    menu += "3. Buscar productos\n"
    menu += "4. Eliminar producto\n"
    menu += "5. Salir\n"
    print(menu)
    dato = int(input("Digita la opcion: "))
    producto = {}
    if dato == 1:

        codigo = int(input("Ingrese el codigo del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))

        producto['codigo'] = codigo
        producto['nombre'] = nombre
        producto['precio'] = precio

        tienda.append(producto)

    elif dato == 2:
        print(tienda)
    elif dato == 3:
        busqueda = int(input("Ingrese el producto a buscar por el codigo: "))
        for i in tienda:
            if i["codigo"] == busqueda:
                precioNew = int(input("Ingrese el nuevo precio: "))
                i["precio"] = precioNew
    elif dato == 4:
        busqueda = int(input("Ingrese el producto a eliminar: "))
        for i in tienda:
            if i["codigo"] == busqueda:
                i.pop("codigo", busqueda)
                i.pop("nombre", busqueda)
                i.pop("precio", busqueda)
    elif dato == 5:
        print("Vuelva pronto!!")
        break
    else:
        print("Numero incorrecto")
