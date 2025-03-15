from .consts import CONFIG_FILE_NAME, COMMENT_CHAR
from .help_functions import show_multiline_info
from os import getcwd

class Config:

    def __init__(self):
        self.dest_paths: dict = {}
        self.excluded_files: list = []

        self.read_configure_file()

    def read_configure_file(self):
        try:
            config_file = open(CONFIG_FILE_NAME, "r", encoding="utf-8")
        except FileNotFoundError:
            print("\nConfiguration file not found. Generating new one... ", end="")
            if self.generate_config_file():
                print("Done")
            show_multiline_info(
                f"If you want change subdirectories for given extenstion or add new one, modify {CONFIG_FILE_NAME}.",
                "If you are ready, run programm again.",
            )
            exit(0)
        else:
            for line in config_file.readlines():
                # TODO: Use regex
                if line[0] == COMMENT_CHAR or line == "\n":
                    continue
                ext, target = line.replace("\n", "").replace(" ", "").split(":")
                if ext == "exclude":
                    self.excluded_files.append(target)
                else:
                    self.dest_paths[ext] = target
            config_file.close()

    def generate_config_file(self) -> bool:
        video_path = "./videos/"
        photo_path = "./photos/"
        audio_path = "./audio/"
        text_path = "./texts/"
        app_path = "./apps/"

        basic_config = {
            "exe": app_path,
            "msi": app_path,

            "txt": text_path,
            "pdf": text_path,
            "docx": text_path,

            "jpg": photo_path,
            "png": photo_path,
            "gif": photo_path,

            "mp4": video_path,

            "mp3": audio_path
        }

        to_exclude = ["configure.py", "main.py", "organizer.py", "help_functions.py", "consts.py", CONFIG_FILE_NAME]

        with open(CONFIG_FILE_NAME, "w", encoding="utf-8") as config_file:
            config_file.write(f"{COMMENT_CHAR} You can use ABSOLUTE (ex. C:/users) or RELATIVE (ex. ./) path.\n")
            config_file.write(f"{COMMENT_CHAR} It does not matter if there is / or not at the end of path.\n")

            config_file.write(f"\n{COMMENT_CHAR} Supported Extensions: \n")
            for ext, path in basic_config.items():
                config_file.write(f"{ext} : {path}\n")

            config_file.write(f"\n{COMMENT_CHAR} Exclusions:\n")
            for excluded in to_exclude:
                config_file.write(f"exclude : {excluded}\n")

        return True

    def get_path(self, ext:str) -> str:
        result: str

        try:
            result = self.dest_paths[ext]
        except KeyError:
            return None
        
        return result

    def is_excluded(self, file:str) -> bool:
        return (file in self.excluded_files)
