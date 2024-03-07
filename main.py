from organizer.help_functions import show_multiline_info
from organizer import create_organizer
from sys import argv as sysArgs

path: str

if __name__ == "__main__":
    try:
        path = sysArgs[1]
    except IndexError:
        show_multiline_info(
            "There is no parameter. Give: RELATIVE or ABSOLUTE goal path.",
            "Ex. 'main.py ./' or 'main.py C:/users/'",
        )
        exit(0)
    
    organizer = create_organizer(path)
    organizer.start()
