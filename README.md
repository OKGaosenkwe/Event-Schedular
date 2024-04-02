# Event-Schedular

This is a simple event scheduler application developed in Python. It allows users to create, view, and delete events. Each event consists of a title, description, date, and time. The application stores events in an in-memory structure (a dictionary), without the need for external database or file storage.

## Features:

<ins>Event Creation:</ins> Users can add new events by providing a title, description, date, and time. Input validation ensures that the date and time are in the proper format (YYYY-MM-DD for date, HH:MM for time).

<ins>Listing Events:</ins> All events can be displayed sorted by date and time. Each event includes all its details.

<ins>Deleting Events:</ins> Users can delete specific events based on their title. If the event does not exist, an appropriate message is displayed.

<ins>User Interface:</ins> The application provides a simple text-based interface in the command line, with options to create, view, and delete events.
