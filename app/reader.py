"""
Модуль, который считывает содержимое папки data_in
"""

import os
from app.classes import School

def read_root_data()->list:
	"""
		Возращает содержимое корня папки data_in
	"""
	in_folder_names = os.listdir('data_in/')
	return in_folder_names


def read_schools_contents(school_list:list)->list[School]:
	"""
	
	"""
	
	schools = []

	for school in school_list:
		
		school_content = School(f'data_in/{school}')

		work_dir = f'data_in/{school}'

		school_dirs  = []
		school_files = []

		for root, dirs, files in os.walk(f'data_in/{school}'):
			dirs = [ name for name in os.listdir(work_dir) if os.path.isdir(os.path.join(work_dir, name)) ]
			school_dirs.append(dirs)
			school_files.append(files)

		school_content.set_dirs(dirs).set_files(files)

		schools.append(school_content)

	return schools


def get_schools()->list[School]:
	return read_schools_contents(read_root_data())
