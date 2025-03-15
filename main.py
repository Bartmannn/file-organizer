"""
    Title: File organizer
    Author: Bartosz Bohdziewicz
    Date: 07.03.2024 y.
"""

from organizer.help_functions import show_multiline_info
from organizer import create_organizer
from sys import argv as sysArgs

if __name__ == "__main__":
    try:
        path: str = sysArgs[1]
    except IndexError:
        show_multiline_info(
            "There is no parameter. Give: RELATIVE or ABSOLUTE goal path.",
            "Ex. 'python3 main.py ./' or 'python3 main.py C:/users/'",
        )
        exit(0)
    
    organizer = create_organizer(path)
    organizer.start()
