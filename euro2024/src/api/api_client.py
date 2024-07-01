import requests
from models import Equipo, Estadio, Partido

class APIClient:
    """
    Clase para interactuar con la API de la Euro 2024 y cargar datos iniciales.
    """

    TEAMS_URL = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
    STADIUMS_URL = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
    MATCHES_URL = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'

    @staticmethod
    def fetch_data(url):
        """
        Realiza una petición GET a la URL proporcionada y retorna los datos en formato JSON.
        """
        response = requests.get(url)
        response.raise_for_status()  # Levanta un error si la petición no fue exitosa
        return response.json()

    @classmethod
    def cargar_equipos(cls):
        """
        Carga los equipos desde la API y retorna una lista de instancias de la clase Equipo.
        """
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json')
        response.raise_for_status()  # Levanta un error si la petición no fue exitosa
        return response.json()

    @classmethod
    def cargar_estadios(cls):
        """
        Carga los estadios desde la API y retorna una lista de instancias de la clase Estadio.
        """
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')
        response.raise_for_status()  # Levanta un error si la petición no fue exitosa
        return response.json()

    @classmethod
    def cargar_partidos(cls):
        """
        Carga los partidos desde la API y retorna una lista de instancias de la clase Partido.
        """
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json')
        response.raise_for_status()  # Levanta un error si la petición no fue exitosa
        return response.json()

    
APIClient.cargar_partidos()