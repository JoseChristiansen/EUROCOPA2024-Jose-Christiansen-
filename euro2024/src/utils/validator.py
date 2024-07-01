from datetime import datetime
from src.api.models import Ticket, Client

def validate_ticket(ticket: Ticket) -> bool:

    if not Ticket.exists(ticket.code):
        return False
    
    if ticket.used:
        return False
    
    return True

def validate_client_age(client: Client) -> bool:

    if client.age < 18:
        return False
    
    return True

def validate_id_number(id_number: str) -> bool:

    def is_perfect_number(number: int) -> bool:
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    
    try:
        id_num = int(id_number)
        return is_perfect_number(id_num)
    except ValueError:
        return False

def validate_event_date(event_date: str) -> bool:

    try:
        event_date_obj = datetime.strptime(event_date, '%Y-%m-%d')
        return event_date_obj > datetime.now()
    except ValueError:
        return False
