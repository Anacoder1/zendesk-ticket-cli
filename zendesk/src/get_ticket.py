from ..utils.helpers import get_ticket_by_id, print_ticket_details_extra


def __init__(ticket_id):
    """Fetches the details of a particular ticket requested by user"""
    ticket = get_ticket_by_id(ticket_id)
    if ticket is None:
        print("Ticket not found at the provided URL!")
        return
    print_ticket_details_extra(ticket)
