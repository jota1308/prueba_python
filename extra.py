opcion  = input('''decime que queres hacer:
[1] agregar producto
[2] borrar producto
[3] listar productos
[0] salir  
respuesta: ''')                                              # Se le pide al usuario que ingrese una opción

lista_productos = []
while opcion != 0:  # Mientras la opción ingresada no sea 0
    if opcion.isdigit() and int(opcion) in range(4):  # Se verifica que la opción ingresada sea un número entre 0 y 3
        opcion = int(opcion)
        if opcion == 1:  # Agregar producto
            print("agregar producto")
            nombre = input("nombre del producto: ")
            cantidad = int(input("cantidad: "))
            while cantidad < 1:
                print("La cantidad debe ser mayor a 0")
                cantidad = int(input("cantidad: "))
            encontrado = False
            nombre = nombre.lower()

            
            for producto in lista_productos:
                if producto[0] == nombre:  # Verifica si el producto ya existe
                    producto[1] += cantidad  # Suma la cantidad al producto existente
                    encontrado = True
                    break
            
            if not encontrado:
                lista_productos.append([nombre, cantidad]) # Agrega el producto a la lista
        elif opcion == 2:
            print("borrar producto")
            nombre = input("nombre del producto: ")
            for producto in lista_productos:
                if producto[0] == nombre:
                    lista_productos.remove(producto) # Elimina el producto de la lista
                    print("producto eliminado")
                    break
            else:
                print("producto no encontrado")

        elif opcion == 3:
            print("listar productos")
            for producto in lista_productos:
                print(f"Producto: {producto[0]}, Cantidad: {producto[1]}")
        else:
            print("salir")
            exit(1)
    else:
        print("Opción inválida")
        exit(1)
    opcion = input('''decime que queres hacer:
    [1] agregar producto
    [2] borrar producto
    [3] listar productos
    [0] salir
    respuesta: ''')  # Se le pide al usuario que ingrese una opción
