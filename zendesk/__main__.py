from .src import get_all_tickets, get_ticket
import os

TERM_SIZE = os.get_terminal_size()


def main():
    """Contains code which runs everytime the CLI is initiated."""
    print(
        f"""
                          _                _     
 ____   ___   _ __     __| |   ___   ___  | | __ 
|_  /  / _ \ | '_ \   / _` |  / _ \ / __| | |/ / 
 / /  |  __/ | | | | | (_| | |  __/ \__ \ |   <  
/___|  \___| |_| |_|  \__,_|  \___| |___/ |_|\_\  
    """
    )
    while True:
        print(
            f"""
        Choose one of the followings options to proceed:
            1. Get all tickets (default: 25 per page)
            2. Get a specific ticket
            3. Exit"""
        )
        choice = input()
        if choice == "1":
            print()
            get_all_tickets.__init__(25)
        elif choice == "2":
            print()
            get_ticket.__init__(input("Enter the ticket id: "))
        elif choice == "3":
            print("Thanks! Have a nice day.")
            exit(0)
        else:
            print("\nWrong choice entered! Please retry.")
        print("\n" + "=" * TERM_SIZE.columns)


if __name__ == "__main__":
    main()
