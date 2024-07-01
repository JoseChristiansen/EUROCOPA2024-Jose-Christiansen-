# Clase de equipos

class Equipo:
    def __init__(self, id, code, name, group):
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def __repr__(self):
        return f"Equipo(id={self.id}, code={self.code}, name={self.name}, group={self.group})"

# Clases de los estadios y todo lo relacionado con ellos

class ProductoRestaurante:
    def __init__(self, name, quantity, price, stock, adicional):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional

    def __repr__(self):
        return f"ProductoRestaurante(name={self.name}, quantity={self.quantity}, price={self.price}, stock={self.stock}, adicional={self.adicional})"


class Restaurante:
    def __init__(self, name, products):
        self.name = name
        self.products = [ProductoRestaurante(**prod) for prod in products]

    def __repr__(self):
        return f"Restaurante(name={self.name}, products={self.products})"


class Estadio:
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = [Restaurante(**rest) for rest in restaurants]

    def __repr__(self):
        return f"Estadio(id={self.id}, name={self.name}, city={self.city}, capacity={self.capacity}, restaurants={self.restaurants})"

# Clase de partidos

class Partido:
    def __init__(self, id, number, home, away, date, group, stadium_id):
        self.id = id
        self.number = number
        self.home = Equipo(**home)
        self.away = Equipo(**away)
        self.date = date
        self.group = group
        self.stadium_id = stadium_id

    def __repr__(self):
        return f"Partido(id={self.id}, number={self.number}, home={self.home}, away={self.away}, date={self.date}, group={self.group}, stadium_id={self.stadium_id})"

# Clase del cliente y de la gestion de tickets con el mismo

class Ticket:
    def __init__(self, id, cliente, partido, tipo_entrada, asiento, precio):
        self.id = id
        self.cliente = cliente
        self.partido = partido
        self.tipo_entrada = tipo_entrada
        self.asiento = asiento
        self.precio = precio

    def __str__(self):
        return f"Ticket(id={self.id}, cliente={self.cliente}, partido={self.partido}, tipo_entrada={self.tipo_entrada}, asiento={self.asiento}, precio={self.precio})"

class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):
        return f"Cliente(id={self.id}, nombre={self.nombre}, cedula={self.cedula}, edad={self.edad})"
