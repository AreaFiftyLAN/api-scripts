import os
import time
from subprocess import call

while True:
    choice = input(
            "1. Get information\n" +
            "2. Get emails from users with an account\n" +
            "3. Get emails from users with a ticket\n" +
            "4. Get emails from users without a ticket\n" +
            "5. Get amount of tickets a user bought\n" +
            "6. Get seats with owners\n" +
            "7. Get all pickup addresses\n" +
            "8. Add a consumption\n" +
            "9. Delete a team\n" +
            "10. Reserve a seat for a ticket\n" +
            "11. Reserve a seat without a ticket\n" +
            "12. Reserve a seat for a ticket and remove the current owner\n" +
            "13. Reserve an entire seatgroup without a ticket\n" +
            "14. Add a seatgroup to the seat layout\n" +
            "15. Add all the seatgroups (edit for personal layout)\n" +
            "Q. Quit\n\n" +
            "What would you like to do: ")
    print()

    if choice == "Q":
        print("Quitting.")
        break
    elif choice == "1":
        call(["python3.5", "tasks/lanstats.py"])
    elif choice == "2":
        call(["python3.5", "tasks/usersmails.py"])
    elif choice == "3":
        call(["python3.5", "tasks/userstickets.py"])
    elif choice == "4":
        call(["python3.5", "tasks/userswithoutticket.py"])
    elif choice == "5":
        call(["python3.5", "tasks/usersorders.py"])
    elif choice == "6":
        call(["python3.5", "tasks/usersseats.py"])
    elif choice == "7":
        call(["python3.5", "tasks/ticketpickup.py"])
    elif choice == "8":
        call(["python3.5", "tasks/addconsumption.py"])
    elif choice == "9":
        call(["python3.5", "tasks/deleteteam.py"])
    elif choice == "10":
        call(["python3.5", "tasks/reserveseat.py"])
    elif choice == "11":
        call(["python3.5", "tasks/reserveseatnoticket.py"])
    elif choice == "12":
        call(["python3.5", "tasks/reserveseatdropowner.py"])
    elif choice == "13":
        call(["python3.5", "tasks/reserveseatgroupnoticket.py"])
    elif choice == "14":
        call(["python3.5", "tasks/addseatgroup.py"])
    elif choice == "15":
        call(["python3.5", "tasks/addallseatgroups.py"])
    else:
        print("Option {} is not valid. Please try again.".format(choice))

    print()
    time.sleep(1)
