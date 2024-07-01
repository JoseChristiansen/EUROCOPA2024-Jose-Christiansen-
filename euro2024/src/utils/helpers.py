import re
from datetime import datetime

def validate_email(email):
    
    # Valida si un correo electrónico es válido.
    # Parameters:
    # email (str): El correo electrónico a validar.
    # Returns:
    # bool: True si el correo es válido, False en caso contrario.
   
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

def validate_phone(phone):

    # Valida si un número de teléfono es válido.
    # Parameters:
    # phone (str): El número de teléfono a validar.
    # Returns:
    # bool: True si el número es válido, False en caso contrario.

    regex = r'^\+?1?\d{9,15}$'
    return re.match(regex, phone) is not None

def calculate_age(birthdate):

    # Calcula la edad basada en la fecha de nacimiento.
    # Parameters:
    # birthdate (str): La fecha de nacimiento en formato 'YYYY-MM-DD'.
    # Returns:
    # int: La edad calculada.

    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def is_perfect_number(n):

    # Verifica si un número es perfecto.
    # Parameters:
    # n (int): El número a verificar.
    # Returns:
    # bool: True si el número es perfecto, False en caso contrario.

    if n < 1:
        return False
    sum_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_divisors == n

def format_currency(value):

    # Formatea un valor numérico a una cadena con formato de moneda.
    # Parameters:
    # value (float): El valor a formatear.
    # Returns:
    # str: El valor formateado como moneda.

    return "${:,.2f}".format(value)

def apply_discount(price, discount):

    # Aplica un descuento a un precio.
    # Parameters:
    # price (float): El precio original.
    # discount (float): El porcentaje de descuento a aplicar.
    # Returns:
    # float: El precio con el descuento aplicado.

    return price * ((100 - discount) / 100)

def load_data_from_file(file_path):

    # Carga datos desde un archivo.
    # Parameters:
    # file_path (str): La ruta del archivo a cargar.
    # Returns:
    # list: Una lista con los datos cargados.

    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def save_data_to_file(file_path, data):

    # Guarda datos en un archivo.
    # Parameters:
    # file_path (str): La ruta del archivo donde se guardarán los datos.
    # data (list): Una lista con los datos a guardar.

    with open(file_path, 'w') as file:
        for line in data:
            file.write(f"{line}\n")
