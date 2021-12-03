import requests
from tabulate import tabulate
import json
from .config import SUPPORT_BASE_URL, AUTH_EMAIL, AUTH_PASSWORD


def zendesk_get_api_call(url, email, password):
    """Makes a GET API request to url, for a user authenticating with email and password"""
    try:
        response = requests.get(url, auth=(email, password))
    except Exception as e:
        print(f"Error occurred while establishing a connection to {url}")
        print(f"Reason: {e}")
        return None
    if response.status_code != 200:
        print("Status:", response.status_code, "Problem with the request")
        print(
            f'Reason: {json.loads(response.text).get("error", None)}: {json.loads(response.text).get("description", None)}'
        )
        return None
    return response


def get_ticket_by_id(ticket_id):
    """Fetches details about a specific ticket"""
    url = f"https://{SUPPORT_BASE_URL}/api/v2/tickets/{ticket_id}.json"
    response = zendesk_get_api_call(url, AUTH_EMAIL, AUTH_PASSWORD)
    if not response:
        return None
    data = response.json()
    return data.get("ticket")


def print_ticket_details_extra(ticket):
    """Prints various details of a specific ticket"""
    headers = [
        "ID",
        "Assignee_ID",
        "Requester_ID",
        "Group_ID",
        "Type",
        "Created At",
        "Updated At",
        "Subject",
        "Tags",
    ]
    blank_str = ", "
    description = ticket.get("description")
    tickets_to_print = [
        ticket["id"],
        ticket["assignee_id"],
        ticket["requester_id"],
        ticket["group_id"],
        ticket["type"],
        ticket["created_at"],
        ticket["updated_at"],
        ticket["subject"],
        blank_str.join(ticket["tags"]),
    ]
    print(tabulate([tickets_to_print], headers=headers, tablefmt="fancy_grid"))
    print("\n------------- Additional data -------------\n")
    print("DESCRIPTION:")
    print(description)
    print()
    additional_headers = [
        "URL",
        "Organization ID",
        "Ticket Form ID",
        "Submitter ID",
    ]
    additional_tickets_to_print = [
        ticket["url"],
        ticket["organization_id"],
        ticket["ticket_form_id"],
        ticket["submitter_id"],
    ]
    print(
        tabulate(
            [additional_tickets_to_print],
            headers=additional_headers,
            tablefmt="fancy_grid",
        )
    )


def get_tickets_per_page_and_return_next_page(page_url):
    """Fetches a page of tickets at a time"""
    page_resp = zendesk_get_api_call(page_url, AUTH_EMAIL, AUTH_PASSWORD)
    if not page_resp:
        return [], ""
    data = page_resp.json()
    tickets = data.get("tickets")
    return tickets, page_resp.json().get("links", {}).get("next")


def print_tickets_page(tickets):
    """Prints variety of details about tickets when all tickets are requested"""
    if len(tickets) == 0:
        print("All tickets are covered!")
        return
    headers = [
        "ID",
        "Assignee_ID",
        "Requester_ID",
        "Type",
        "Created At",
        "Updated At",
        "Subject",
        "Tags",
    ]
    blank_str = ", "
    tickets_to_print = [
        [
            t["id"],
            t["assignee_id"],
            t["requester_id"],
            t["type"],
            t["created_at"],
            t["updated_at"],
            t["subject"],
            blank_str.join(t["tags"]),
        ]
        for t in tickets
    ]
    print(tabulate(tickets_to_print, headers=headers, tablefmt="fancy_grid"))
    return True
