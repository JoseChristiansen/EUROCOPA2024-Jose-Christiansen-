from partido_manager import partidos, estadios

entero_partido = 0
cedula = 0

#Funcion para extraer el numero de partido que eligio el usuario
def cambiar_variable1(numero):
    global entero_partido
    entero_partido = numero

#Funcion para extraer la cedula que ingreso el usuario usuario
def cambiar_variable2(numero):
    global cedula
    cedula = numero

#Funcion para obtener los restaurantes del estadio del partido que el usuario selecciono
def obtener_estadio_restaurante():
    partido = next((p for p in partidos if p['number'] == entero_partido), None)
    if partido is None:
        raise ValueError(f"No se encontró partido con número {entero_partido}")

    # Extraemos el stadium_id del partido
    stadium_id = partido['stadium_id']

    # Buscamos el estadio con el stadium_id correspondiente
    restaurantes = next((e for e in estadios if e['id'] == stadium_id), None)
    if restaurantes is None:
        raise ValueError(f"No se encontró estadio con id {stadium_id}")

    return restaurantes['restaurants']

#Funcion que muestra el menu de opciones 
def mostrar_menu():
    while True:
            print("Siendo miembro de la comunidad VIP tiene privilegios de comprar en nuestros restaurantes.")
            print("Menú de opciones:")
            print("1. Filtrar productos por nombre")
            print("2. Filtrar productos por tipo")
            print("3. Filtrar productos por precio")
            print("4. Mostrar todos los productos")
            print("5. Salir")

            while True:
                opcion_menu = input("Ingrese una opción (1-5): ")

                if opcion_menu not in ["1", "2", "3", "4", "5"]:
                    print("Opción inválida. Intente nuevamente.")
                    continue

                if opcion_menu == "1":
                    # Lógica para filtrar productos por nombre
                    print_filtrar_productos_por_nombre()
                    comprar_producto()
                    break
                elif opcion_menu == "2":
                    # Lógica para filtrar productos por tipo
                    print_filtrar_productos_por_tipo()
                    comprar_producto()
                    break
                elif opcion_menu == "3":
                    # Lógica para filtrar productos por precio
                    print_filtrar_productos_por_precio()
                    comprar_producto()
                    break
                elif opcion_menu == "4":
                    # Lógica para mostrar todos los productos
                    mostrar_productos()
                    comprar_producto()
                    break
                elif opcion_menu == "5":
                    print("Saliendo del menú...")
                    return

def mostrar_productos():
    restaurantes = obtener_estadio_restaurante()
    for supplier in restaurantes:
        print(f"** {supplier['name']} **")
        for product in supplier['products']:
            print(f"  ** {product['name']} **")
            print(f"    Cantidad: {product['quantity']}")
            print(f"    Precio: ${product['price']}")
            print(f"    Stock: {product['stock']}")
            print(f"    Adicional: {product['adicional']}")
            print()

def filtrar_productos_por_nombre():
    restaurantes = obtener_estadio_restaurante()

    while True:
        nombre = input("Ingrese el nombre del alimento que desea comprar: ").strip()
        if not nombre:
            print("Debe ingresar un nombre de alimento. Intente nuevamente.")
        else:
            nombre = nombre.lower()
            nombre = nombre.title()
            filtered_products = [producto for supplier in restaurantes for producto in supplier['products'] if nombre in producto['name']]
            if not filtered_products:
                print("No se encontraron productos con ese nombre. Intente nuevamente.")
            else:
                return filtered_products

def print_filtrar_productos_por_nombre():
    products = filtrar_productos_por_nombre()

    if not products:
        print("No se encontraron productos con ese nombre.")
    else:
        print("{:<30} {:<10} {:<10} {:<10} {:<15}".format("Nombre", "Cantidad", "Precio", "Stock", "Adicional"))
        print("-" * 80)
        for product in products:
            print("{:<30} {:<10} {:<10} {:<10} {:<15}".format(
                product["name"], product["quantity"], product["price"], product["stock"], product["adicional"]
            ))

def filtrar_productos_por_precio():
    restaurantes = obtener_estadio_restaurante()

    while True:
        try:
            precio_min = float(input("Ingrese el precio mínimo que desea pagar: "))
            precio_max = float(input("Ingrese el precio máximo que desea pagar: "))
            if precio_min < 0 or precio_max < 0:
                print("Los precios no pueden ser negativos. Intente nuevamente.")
            elif precio_min > precio_max:
                print("El precio mínimo no puede ser mayor que el precio máximo. Intente nuevamente.")
            else:
                filtered_products = [producto for supplier in restaurantes for producto in supplier['products'] if precio_min <= float(producto['price']) <= precio_max]
                return filtered_products
        except ValueError:
            print("Los precios deben ser números. Intente nuevamente.")

def print_filtrar_productos_por_precio():
    products = filtrar_productos_por_precio()

    if not products:
        print("No se encontraron productos en ese rango de precio.")
    else:
        print("{:<30} {:<10} {:<10} {:<10} {:<15}".format("Nombre", "Cantidad", "Precio", "Stock", "Adicional"))
        print("-" * 80)
        for product in products:
            print("{:<30} {:<10} {:<10} {:<10} {:<15}".format(
                product["name"], product["quantity"], product["price"], product["stock"], product["adicional"]
            ))

def filtrar_productos_por_tipo():
    restaurantes = obtener_estadio_restaurante()

    while True:
        tipo_producto = input("Ingrese el tipo de producto que desea filtrar (plate o package) o 'drink' para filtrar por tipo de bebida: ").lower()
        if tipo_producto in ["plate", "package"]:
            filtered_products = [producto for supplier in restaurantes for producto in supplier['products'] if producto['type'] == tipo_producto]
            return filtered_products
        elif tipo_producto == "drink":
            while True:
                tipo_bebida = input("Ingrese el tipo de bebida que desea filtrar (alcoholic o non-alcoholic): ").lower()
                if tipo_bebida in ["alcoholic", "non-alcoholic"]:
                    filtered_products = [producto for supplier in restaurantes for producto in supplier['products'] if producto['adicional'] == tipo_bebida]
                    return filtered_products
                else:
                    print("Tipo de bebida no válido. Intente nuevamente.")
        else:
            print("Tipo de producto no válido. Intente nuevamente.")

def print_filtrar_productos_por_tipo():
    products = filtrar_productos_por_tipo()

    if not products:
        print("No se encontraron productos de ese tipo.")
    else:
        print("{:<30} {:<10} {:<10} {:<10} {:<15}".format("Nombre", "Cantidad", "Precio", "Stock", "Adicional"))
        print("-" * 80)
        for product in products:
            print("{:<30} {:<10} {:<10} {:<10} {:<15}".format(
                product["name"], product["quantity"], product["price"], product["stock"], product["adicional"]
            ))

def es_numero_perfecto_devuelve_uno_o_cero(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return 1 if suma == numero else 0

carrito = []
def comprar_producto():
    global carrito
    while True:
        print("Elija una opción:")
        print("1. Comprar producto")
        print("2. Volver al menú")
        opcion = input("Ingrese el número de la opción que desea: ").strip()
        if not opcion:
            print("Debe ingresar un número de opción. Intente nuevamente.")
            continue

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto que desea comprar: ").strip()
            if not nombre_producto:
                print("Debe ingresar un nombre de producto. Intente nuevamente.")
                continue

            restaurantes = obtener_estadio_restaurante()
            producto_encontrado = False
            for supplier in restaurantes:
                for producto in supplier['products']:
                    if nombre_producto.lower() in producto['name'].lower():
                        carrito.append(producto)
                        print(f"Producto '{producto['name']}' agregado al carrito.")
                        producto_encontrado = True
                        break
                if producto_encontrado:
                    break

            if not producto_encontrado:
                print("No se encontró el producto. Intente nuevamente.")

        elif opcion == "2":
            mostrar_menu()
            return

        while True:
            opcion = input("Desea seguir comprando (1) o pagar (2)? ")
            if opcion not in ["1", "2"]:
                print("Opción inválida. Intente nuevamente.")
                continue
            if opcion == "1":
                return
            elif opcion == "2":
                print("Carrito:")
                print(carrito)
                for producto in carrito:
                    print(f"  - {producto['name']} - ${producto['price']}")
                subtotal = sum(float(p['price']) for p in carrito)
                if es_numero_perfecto_devuelve_uno_o_cero(cedula) == 1:
                    descuento = "15%"
                    total = (subtotal * 75)/100
                else: 
                    descuento = 0
                total = subtotal 

                print(f"Precio inicial: ${subtotal}")
                print(f"Descuento: ${descuento}")
                print(f"Total: ${total}")
                print("Gracias por su compra!")
                carrito = []
                print("Gracias por su utilizar el sistema!")
                print("Si quiere hacer otra compra de entradas no dudes en utilizar el programa otra vez!")
                return
            

