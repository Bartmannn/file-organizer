from .configure import Config
from shutil import move
import os


class Organizer:

    def __init__(self, path):
        self.path = path
        self.files = os.listdir(self.path)
        self.configuration = Config()

    def start(self):
        confirm_options = ["y", "yes", "t", "tak"]
        user_option = input(f"\nFolder '{self.path}' will be reorganized. Do you want continue? [y/n] ").lower()
        if not user_option in confirm_options:
            print("Organizing aborted. . .\n")
            exit(0)
        else:
            print("Organizing has started. . . ", end="")

        for file in self.files:
            if self.configuration.is_excluded(file):
                continue

            file_name, file_ext = os.path.splitext(file)
            file_ext = file_ext.replace(".", "")

            dest_path: str = self.configuration.get_path(file_ext)
            if dest_path == None:
                continue

            dest_path = dest_path.replace(".", self.path) # running program from app path
            
            if os.path.exists(dest_path):
                move(self.path+"/"+file, dest_path+"/"+file)
            else:
                os.makedirs(dest_path)
                move(self.path+"/"+file, dest_path+"/"+file)

        print("Done\n")
