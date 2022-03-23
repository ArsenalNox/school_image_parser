from typing_extensions import Self


class School:
	def __init__(self, root_dir:list) -> None:
		self.root_dir = root_dir


	def set_dirs(self, dirs:list)->Self:
		self.dirs 	  = dirs
		return self 


	def set_files(self, files)->Self:
		self.files    = files 
		return self


	def __repr__(self) -> str:
		return f"{self.root_dir} {self.dirs} {self.files}"
	