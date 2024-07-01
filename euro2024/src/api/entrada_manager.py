from models import Cliente
from partido_manager import mostrar_partidos, format_partidos_por_pais, format_partidos_por_estadio, format_partidos_por_fecha, partidos, estadios
from restaurante_manager import cambiar_variable1, cambiar_variable2, mostrar_menu
import os

entero_partido = 0
cedulita = 0

def registrar_asientos(archivo, asientos):
    with open(archivo, 'w') as f:
        for asiento, estado in asientos.items():
            f.write(f"{asiento}:{estado}\n")

def leer_asientos(archivo):
    if os.path.exists(archivo):
        asientos = {}
        with open(archivo, 'r') as f:
            for linea in f:
                asiento, estado = linea.strip().split(':')
                asientos[int(asiento)] = estado
        return asientos
    else:
        return None

def registrar_cliente():
    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre.isalpha():
            break
        print("Nombre inválido. Debe contener solo letras.")

    while True:
        cedula = input("Ingrese la cédula del cliente: ")
        if cedula.isdigit() and 7 <= len(cedula) <= 8:
            break
        print("Cédula inválida. Debe tener entre 7 y 8 dígitos.")

    while True:
        try:
            edad = int(input("Ingrese la edad del cliente: "))
            if 0 <= edad <= 110:
                break
            print("Edad inválida. Debe ser un número entre 0 y 110.")
        except ValueError:
            print("Edad inválida. Debe ser un número entero.")

    cliente = Cliente(nombre, cedula, edad)
    cambiar_variable2(cliente.cedula)
    return cliente

def partido_elegido():
    while True:
        try:
            numero_partido = input("""Si quiere elegir alguno de estos partidos, ingrese el número del partido, si no ingrese el número 50:  """)
            global entero_partido
            entero_partido = int(numero_partido)
            cambiar_variable1(entero_partido)
            if entero_partido > 0 and entero_partido <= 36:
                return entero_partido
            elif numero_partido == "50":
                eleccion_de_partido()
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Opción inválida.")

def obtener_estadio():
    numero_partido = partido_elegido()

    while True:
        tipo_entrada = input("""Ingrese el tipo de entrada que quiere comprar:
                             1. General: sin acceso a restaurante
                             2. VIP: con acceso a restaurante
                             """)
        if tipo_entrada in ["1", "2"]:
            break
        else:
            print("Opción inválida. Debe ingresar 1 o 2.")

    partido = next((p for p in partidos if p['number'] == numero_partido), None)
    if partido is None:
        raise ValueError(f"No se encontró partido con número {numero_partido}")

    stadium_id = partido['stadium_id']

    estadio = next((e for e in estadios if e['id'] == stadium_id), None)
    if estadio is None:
        raise ValueError(f"No se encontró estadio con id {stadium_id}")

    if tipo_entrada == "1":
        estadio_general = {
            'id': estadio['id'],
            'name': estadio['name'],
            'capacity': estadio['capacity']
        }
        return estadio_general
    else:
        return estadio

def eleccion_asiento():
    estadio = obtener_estadio()
    capacidad = estadio['capacity'][1] if 'restaurants' in estadio else estadio['capacity'][0]

    archivo_asientos = f"asientos_{estadio['id']}.txt"
    asientos = leer_asientos(archivo_asientos)

    if asientos is None:
        asientos = {i: 'Disponible' for i in range(1, capacidad + 1)}
        registrar_asientos(archivo_asientos, asientos)

    print("Asientos disponibles:")
    for asiento, disponibilidad in asientos.items():
        print(f"Asiento {asiento}: {disponibilidad}")

    while True:
        asiento_elegido = int(input("Ingrese el número de asiento que desea: "))
        if asiento_elegido in asientos:
            if asientos[asiento_elegido] == 'Disponible':
                asientos[asiento_elegido] = 'No disponible'
                print(f"Asiento {asiento_elegido} reservado con éxito!")
                break
            else:
                print("Lo sentimos, ese asiento no está disponible. Por favor, elija otro.")
        else:
            print("Lo sentimos, ese asiento no existe. Por favor, elija otro.")
    
    registrar_asientos(archivo_asientos, asientos)
    if 'restaurants' in estadio:
        precio_entrada(75)
    else:
        precio_entrada(35)

def precio_entrada(precio):
    cliente = registrar_cliente()
    cedula = cliente.cedula
    if es_numero_vampiro(cedula):
        print(f"¡Felicidades! Usted tiene un número vampiro. Se le aplicará un 50% de descuento.")
        descuento = 50
    else:
        descuento = 0

    precio_con_descuento = precio * (1 - descuento / 100)
    iva = (precio_con_descuento * 16) / 100
    precio_final = precio_con_descuento * 1.16
    print(f"""Su facturación final sería:
                 Precio de entrada: {precio} 
                 Descuento: {descuento}%
                 IVA: {iva}
                 Total a Pagar: {precio_final}""")      
    mostrar_menu()

def es_numero_vampiro(cedula):
    digitos = [int(d) for d in cedula]
    productos = [d * (d + 1) // 2 for d in digitos]
    suma_productos = sum(productos)
    return suma_productos == int(cedula)

def eleccion_de_partido():
    while True:
        partido = input("""Indique el partido de su elección, para observarlos puedes:
                    1. Mostrar todos los partidos
                    2. Mostrar por país de su elección
                    3. Mostrar por estadio de su elección
                    4. Mostrar por fecha de su elección
                    >> """)
        if partido in ["1", "2", "3", "4"]:
            break
        print("Opción inválida. Debe elegir una opción entre 1 y 4.")

    if partido == "1":
        mostrar_partidos()
        eleccion_asiento()
    elif partido == "2":
        format_partidos_por_pais()
        eleccion_asiento()
    elif partido == "3":
        format_partidos_por_estadio()
        eleccion_asiento()
    elif partido == "4":
        format_partidos_por_fecha()
        eleccion_asiento()

eleccion_de_partido()
