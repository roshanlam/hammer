class logger:
	def __init__(self, name, level="Information"):
        self.name = name,
        self.console_format = ""
	self._fileformat = ""
        self._level_number = {
            "Info": 0,
            "Warning": 1,
            "Debug": 2,
            "Critical": 3,
            "Error": 4,
        }

	def write():
	"""
	This will write the logs
	"""
	self.make_format(message)
	self.write_file()
	if LEVEL_NUMBER >= self.level:
		print(self.console_format)

	def make_format(self,message):
	
	"""
	Creates the format for the string on how it is going
	to be written. 
	"""
	
	t = datetime.datetime.now()
	DATETIME_FORMAT = "{}--{}--{} {}:{}:{}".format(
		t.year, t.month, t.day, t.hour, t.minute, t.second
	)

	self.console_format = "[{}]: {}".format(self.name, message)
	self.file_format = "[{}]-[{}}]: {}\n".format(
		self.name, DATETIME_FORMAT, message
	)

	
	
	def info(self, message):
	LEVEL_NUMBER = 0
	self.write(message, LEVEL_NUMBER)
	
	def warning(self, message):
	
	LEVEL_NUMBER = 1
	self.write(message, LEVEL_NUMBER)

	def debug(self, message):
	LEVEL_NUMBER = 2
	self.write(message, LEVEL_NUMBER)


