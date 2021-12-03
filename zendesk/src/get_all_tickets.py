from ..utils.config import SUPPORT_BASE_URL
from ..utils.helpers import (
    get_tickets_per_page_and_return_next_page,
    print_tickets_page,
)


def __init__(page_size=25):
    """Prints details of all tickets of user in a paginated manner (25 tickets per page)"""
    next_page = (
        f"https://{SUPPORT_BASE_URL}/api/v2/tickets?page[size]={page_size}"
    )
    page = 1
    while next_page != "" and next_page is not None:
        print(f"Going through Page {page}...")
        tickets, next_page = get_tickets_per_page_and_return_next_page(
            next_page
        )

        if next_page == "":
            print("Unable to find tickets any more!")
            return

        print_tickets_page(tickets)

        if len(tickets) < page_size:
            print("All tickets are covered!")
            break

        page += 1
        choice = input(f"Would like to go to page {page} [y/n] ").lower()
        if choice not in ["y", "n"]:
            print("you entered the wrong choice. Try again!")
            exit(1)
        if choice == "n":
            print("Thanks! Have a great day.")
            exit(0)
