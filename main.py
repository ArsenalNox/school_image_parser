from app import parser as pr 
from app import reader as rd
from typing_extensions import Self

schools_without_foldres = 0
schools_with_foldres    = 0

for school in rd.get_schools():

	if len(school.dirs) == 0:
		#print(f'School {school.root_dir} has not folders...')
		schools_without_foldres += 1 
	else: 
		print(school)
		schools_with_foldres += 1

print(f"""
	Schools without folders: {schools_without_foldres}
	Schools with folders: {schools_with_foldres}
""")