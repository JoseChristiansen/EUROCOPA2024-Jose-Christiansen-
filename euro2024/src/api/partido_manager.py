from api_client import APIClient

partidos = APIClient.cargar_partidos()
estadios = APIClient.cargar_estadios()
equipos = APIClient.cargar_equipos()


#Formateo de partidos
def formatear_partido(partido, estadios):
    home_team = partido['home']['name']
    away_team = partido['away']['name']
    date = partido['date']
    group = partido['group']
    stadium_id = partido['stadium_id']
    stadium_name = next((estadio['name'] for estadio in estadios if estadio['id'] == stadium_id), 'Estadio no encontrado')
    return f"Partido {partido['number']}: {home_team} vs {away_team} - Fecha: {date} - Grupo: {group} - Estadio: {stadium_name}"

#Funcion para mostrar todos los partidos de formateados para que se vean bien en la consola
def mostrar_partidos():
    for partido in partidos:
        print(formatear_partido(partido, estadios))

#Filtra los partidos por pais
def filtrar_partidos_por_pais(partidos):
    def get_pais_by_id(pais_id):
        pais_names = {
            1: "Albania",
            2: "Austria",
            3: "Belgium",
            4: "Croatia",
            5: "Czech Republic",
            6: "Denmark",
            7: "England",
            8: "France",
            9: "Georgia",
            10: "Germany",
            11: "Hungary",
            12: "Italy",
            13: "Netherlands",
            14: "Poland",
            15: "Portugal",
            16: "Romania",
            17: "Scotland",
            18: "Serbia",
            19: "Slovakia",
            20: "Slovenia",
            21: "Spain",
            22: "Switzerland",
            23: "Turkey",
            24: "Ukraine"
        }
        pais_name = pais_names.get(int(pais_id), "Pais no encontrado")
        return pais_name

    while True:
        pais_id = input("""Ingrese el numero correspondiente al pais:
                        
                        1. Albania
                        2. Austria
                        3. Belgium
                        4. Croatia
                        5. Czech Republic
                        6. Denmark
                        7. England
                        8. France
                        9. Georgia
                        10. Germany
                        11. Hungary
                        12. Italy
                        13. Netherlands
                        14. Poland
                        15. Portugal
                        16. Romania
                        17. Scotland
                        18. Serbia
                        19. Slovakia
                        20. Slovenia
                        21. Spain
                        22. Switzerland
                        23. Turkey
                        24. Ukraine

                        >>""")
        if pais_id.isdigit() and 1 <= int(pais_id) <= 24:
            break
        print("Ingrese un número válido entre 1 y 24.")

    pais_name = get_pais_by_id(pais_id)
    partidos_filtrados = [partido for partido in partidos if partido['home']['name'] == pais_name or partido['away']['name'] == pais_name]
    return partidos_filtrados


#Formatea la lista de diccionarios de  filtrar_partidos_por_pais
def format_partidos_por_pais():
    partidos_filtrados = filtrar_partidos_por_pais(partidos)
    for partido in partidos_filtrados:
        estadio_id = partido['stadium_id']
        estadio_name = next((estadio['name'] for estadio in estadios if estadio['id'] == estadio_id), 'Estadio no encontrado')
        print(f"Partido {partido['number']}:")
        print(f"  Fecha: {partido['date']}")
        print(f"  Grupo: {partido['group']}")
        print(f"  Estadio: {estadio_name}")
        print(f"  Equipo Local: {partido['home']['name']} ({partido['home']['code']})")
        print(f"  Equipo Visitante: {partido['away']['name']} ({partido['away']['code']})")
        print("")
        

def filtrar_partidos_por_estadio(partidos, estadios):
    def get_estadio_by_id(estadio_id):
        estadio_names = {
            1: "Estadio Olímpico de Berlín",
            2: "Carbajal Medina S.L.",
            3: "Allianz Arena",
            4: "Signal Iduna Park",
            5: "MHPArena",
            6: "Veltins-Arena",
            7: "Volksparkstadion",
            8: "Deutsche Bank Park",
            9: "Estadio Rhein Energie",
            10: "Red Bull Arena",
            11: "Merkur Spiel-Arena"
        }
        estadio_name = estadio_names.get(int(estadio_id), "Estadio no encontrado")
        return next((estadio for estadio in estadios if estadio['name'] == estadio_name), None)

    while True:
        estadio_id = input("""Ingrese el numero correspondiente al estadio:
                        
                        1. Estadio Olímpico de Berlín
                        2. Carbajal Medina S.L.
                        3. Allianz Arena
                        4. Signal Iduna Park
                        5. MHPArena
                        6. Veltins-Arena
                        7. Volksparkstadion
                        8. Deutsche Bank Park
                        9. Estadio Rhein Energie
                        10. Red Bull Arena
                        11. Merkur Spiel-Arena

                        >>""")
        if estadio_id.isdigit() and 1 <= int(estadio_id) <= 11:
            break
        print("Ingrese un número válido entre 1 y 11.")

    estadio_filtrado = get_estadio_by_id(estadio_id)
    partidos_filtrados = [partido for partido in partidos if partido['stadium_id'] == estadio_filtrado['id']]
    return partidos_filtrados


#Formatea la lista de diccionarios de filtrar_partidos_por_estadio
def format_partidos_por_estadio():
    partidos_filtrados = filtrar_partidos_por_estadio(partidos, estadios)
    for partido in partidos_filtrados:
        estadio_id = partido['stadium_id']
        estadio_name = next((estadio['name'] for estadio in estadios if estadio['id'] == estadio_id), 'Estadio no encontrado')
        print(f"Partido {partido['number']}:")
        print(f"  Fecha: {partido['date']}")
        print(f"  Grupo: {partido['group']}")
        print(f"  Estadio: {estadio_name}")
        print(f"  {partido['home']['name']} ({partido['home']['code']}) vs {partido['away']['name']} ({partido['away']['code']})")
        print("")



#Filtrar por fecha
def filtrar_partidos_por_fecha(partidos):
    print("Ingrese el número correspondiente a la fecha:")
    print("1. 2024-06-14")
    print("2. 2024-06-15")
    print("3. 2024-06-16")
    print("4. 2024-06-17")
    print("5. 2024-06-18")
    print("6. 2024-06-19")
    print("7. 2024-06-20")
    print("8. 2024-06-21")
    print("9. 2024-06-22")
    print("10. 2024-06-23")
    print("11. 2024-06-24")
    print("12. 2024-06-25")
    print("13. 2024-06-26")

    while True:
        fecha_partido = input(">> ")
        if fecha_partido.isdigit() and 1 <= int(fecha_partido) <= 13:
            break
        print("Ingrese un número válido entre 1 y 13.")

    fechas_disponibles = {
        1: "2024-06-14",
        2: "2024-06-15",
        3: "2024-06-16",
        4: "2024-06-17",
        5: "2024-06-18",
        6: "2024-06-19",
        7: "2024-06-20",
        8: "2024-06-21",
        9: "2024-06-22",
        10: "2024-06-23",
        11: "2024-06-24",
        12: "2024-06-25",
        13: "2024-06-26"
    }

    fecha_filtrada = fechas_disponibles.get(int(fecha_partido), "Fecha no encontrada")
    partidos_filtrados = [partido for partido in partidos if partido['date'] == fecha_filtrada]
    return partidos_filtrados


#Formatea la lista de diccionarios de filtrar_partidos_por_fecha
def format_partidos_por_fecha():
    partidos_filtrados = filtrar_partidos_por_fecha(partidos)
    for partido in partidos_filtrados:
        estadio_id = partido['stadium_id']
        estadio_name = next((estadio['name'] for estadio in estadios if estadio['id'] == estadio_id), 'Estadio no encontrado')
        print(f"Partido {partido['number']}:")
        print(f"  Fecha: {partido['date']}")
        print(f"  Grupo: {partido['group']}")
        print(f"  Estadio: {estadio_name}")
        print(f"  {partido['home']['name']} ({partido['home']['code']}) vs {partido['away']['name']} ({partido['away']['code']})")
        print("")




