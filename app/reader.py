"""
Модуль, который считывает содержимое папки data_in
"""

import os
import pprint as pp

#pp = pprint.PrettyPrinter(indent=5)

def read_root_data()->list:
    """
        Возращает содержимое корня папки data_in
    """
    in_folder_names = os.listdir('data_in/')
    return in_folder_names


def read_schools_contents(school_list:list)->list:
    """
    
    """
    
    schools = []

    for school in school_list:

        work_dir = f'data_in/{school}'

        school_name = school

        school_dirs  = os.listdir(work_dir)

        school_categories = []

        for subdir in school_dirs:
            subdir_name = subdir
            subdir_files = []

            if os.path.isdir(f'data_in/{school}/{subdir}/До'):
                for category_content in os.listdir(f'data_in/{school}/{subdir}/До'):
                    subdir_files.append(category_content)

            elif os.path.isdir(f"data_in/{school}/{subdir}"):
                for category_content in os.listdir(f'data_in/{school}/{subdir}'):
                    subdir_files.append(category_content)

            school_categories.append({
                "subdir_name": subdir,
                "files": subdir_files
                })
        schools.append({
            "name": school,
            "cats": school_categories
            })

    return schools

def read_data():
    return read_schools_contents(read_root_data())

