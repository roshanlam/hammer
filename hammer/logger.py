


class logger:
    def __init__(self, name, level="Information"):
        self.name = name,
        self._fileformat = ""
        self._level_number = {
            "Info": 0,
            "Warning": 1,
            "Debug": 2,
            "Critical": 3,
            "Error": 4,
        }

