from .organizer import Organizer


def create_organizer(path: str):
    return Organizer(path)