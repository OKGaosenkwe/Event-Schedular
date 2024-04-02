from datetime import datetime
import unittest


# In-memory storage for events
events = []


# Function to validate date format
def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return date
    except ValueError:
        return None


# Function to validate time format
def validate_time(time_str):
    try:
        time = datetime.strptime(time_str, "%H:%M").time()
        return time
    except ValueError:
        return None


# Function to check for duplicate events
def is_duplicate(title, date_time):
    for event in events:
        if event['title'] == title and event['date_time'] == date_time:
            return True
    return False


# Function to add a new event with improved date and time error handling
def add_event():
    title = input("Enter event title: ")
    description = input("Enter event description: ")

    while True:
        date_str = input("Enter event date (YYYY-MM-DD): ")
        date = validate_date(date_str)

        if date:
            break  # Break out of the loop if date validation succeeds
        else:
            print("Invalid date format. Please use YYYY-MM-DD for date. Try again.")

    while True:
        time_str = input("Enter event time (HH:MM): ")
        time = validate_time(time_str)

        if time:
            break  # Break out of the loop if time validation succeeds
        else:
            print("Invalid time format. Please use HH:MM for time. Try again.")

    date_time = datetime.combine(date, time)

    # Check for duplicate events
    if is_duplicate(title, date_time):
        print("An event with the same title, date, and time already exists.")
        return

    event = {
        "title": title,
        "description": description,
        "date_time": date_time
    }

    events.append(event)
    print("Event added successfully.")


# Function to display all events with numbers
def list_events():
    if not events:
        print("No events available.")
        return

    # Sort events by date and time
    sorted_events = sorted(events, key=lambda x: x["date_time"])

    print("Available Events:")
    for i, event in enumerate(sorted_events, 1):
        print(f"{i}. Title: {event['title']}\n   Description: {event['description']}")
        print(f"   Date and Time: {event['date_time'].strftime('%Y-%m-%d %H:%M')}\n")


# Function to display events with numbers
def display_events_with_numbers():
    if not events:
        print("No events available.")
    else:
        print("Available Events:")
        for i, event in enumerate(events, 1):
            print(f"{i}. {event['title']}")


# Function to delete an event based on number
def delete_event():
    display_events_with_numbers()

    if not events:
        return  # No events available, exit the function

    while True:
        try:
            event_number = int(input("Enter the number of the event to delete: "))
            if 0 <= event_number <= len(events):
                break  # Break out of the loop if the input is a valid event number
            else:
                print("Invalid event number. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    event_to_delete = events[event_number - 1]

    # Ask for confirmation before deleting
    confirm = input(f"Are you sure you want to delete the event '{event_to_delete['title']}'? (yes/no): ").lower()

    if confirm == 'yes':
        events.remove(event_to_delete)
        print("Event deleted successfully.")
    else:
        print("Deletion canceled.")


# Function to search events by date or keyword
def search_events():
    search_term = input("Enter date (YYYY-MM-DD) or keyword to search events: ")

    search_results = []

    for event in events:
        if (search_term in event['title'].lower()) or (search_term in event['description'].lower()) or (
                search_term == event['date_time'].strftime('%Y-%m-%d')):
            search_results.append(event)

    if not search_results:
        print("No matching events found.")
    else:
        print(f"Search Results for '{search_term}':")
        for i, result in enumerate(search_results, 1):
            print(f"{i}. Title: {result['title']}\n   Description: {result['description']}")
            print(f"   Date and Time: {result['date_time'].strftime('%Y-%m-%d %H:%M')}\n")


# Function to edit an existing event
def edit_event():
    display_events_with_numbers()

    if not events:
        return  # No events available, exit the function

    while True:
        try:
            event_number = int(input("Enter the number of the event to edit: "))
            if 0 <= event_number <= len(events):
                break  # Break out of the loop if the input is a valid event number
            else:
                print("Invalid event number. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    event_to_edit = events[event_number - 1]

    print(f"Editing Event: {event_to_edit['title']}")
    print("Leave a field blank to keep the existing value.")

    title = input(f"Enter new title ({event_to_edit['title']}): ") or event_to_edit['title']
    description = input(f"Enter new description ({event_to_edit['description']}): ") or event_to_edit['description']

    while True:
        date_str = input(f"Enter new date (YYYY-MM-DD) ({event_to_edit['date_time'].strftime('%Y-%m-%d')}): ") or \
                   event_to_edit['date_time'].strftime('%Y-%m-%d')
        date = validate_date(date_str)

        if date:
            break  # Break out of the loop if date validation succeeds
        else:
            print("Invalid date format. Please use YYYY-MM-DD for date. Try again.")

    while True:
        time_str = input(f"Enter new time (HH:MM) ({event_to_edit['date_time'].strftime('%H:%M')}): ") or event_to_edit[
            'date_time'].strftime('%H:%M')
        time = validate_time(time_str)

        if time:
            break  # Break out of the loop if time validation succeeds
        else:
            print("Invalid time format. Please use HH:MM for time. Try again.")

    date_time = datetime.combine(date, time)

    # Check for duplicate events
    if is_duplicate(title, date_time) and (
            title.lower() != event_to_edit['title'].lower() or date_time != event_to_edit['date_time']):
        print("An event with the same title, date, and time already exists.")
        return

    event_to_edit['title'] = title
    event_to_edit['description'] = description
    event_to_edit['date_time'] = date_time

    print("Event edited successfully.")


# Main loop for user interface
while True:
    print("\n===== Event Manager =====")
    print("1. Create Event")
    print("2. View Events")
    print("3. Search Events")
    print("4. Edit Event")
    print("5. Delete Event")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_event()
    elif choice == "2":
        list_events()
    elif choice == "3":
        search_events()
    elif choice == "4":
        edit_event()
    elif choice == "5":
        delete_event()
    elif choice == "6":
        print("Exiting Event Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
