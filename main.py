from random import randint
from app import parser as pr 
from app import reader as rd

import pprint
import os 
import mysql.connector
import shutil 


sqlConnection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='min'
        )

cursor = sqlConnection.cursor()

def is_school_insered(school_name):
    sql = f"""
    SELECT 
        * 
    FROM educational
    WHERE `name` = '{school_name}'
    """
    cursor.execute(sql)

    result = cursor.fetchall()
    return result


def get_all_munipals_list():
    sql = """
    SELECT 
        *
    FROM munipal 
    """
    cursor.execute(sql)

    return cursor.fetchall()


def insert_new_school(school_name):
    sql = f"""
    INSERT INTO educational(
            `name`,
            `name_full`,
            `address`,
            `region`,
            `project_capacity`,
            `factial_capacity`
            )
    VALUES (
            '{school_name}',
            '{school_name}',
            'г. Оренбург ул. X/Y',
            '36',
            '0',
            '0'
            )
    """

    cursor.execute(sql)
    sqlConnection.commit()
    return cursor.lastrowid


def get_school_id(school_name):
    sql = f"""
    SELECT 
        * 
    FROM educational
    WHERE name LIKE "%{school_name}%"
    """
    cursor.execute(sql)
    return cursor.fetchall()[0]


def insert_school_photo(school_id, category_id, photo_path):
    sql = f"""
    INSERT INTO photos_edu(
            `schid`,
            `category`,
            `path`,
            `thumb`
            )
    VALUES (
            {school_id},
            {category_id},
            '{photo_path}',
            '{photo_path}'
            )
    """
    cursor.execute(sql)
    sqlConnection.commit()
    return cursor.fetchall()


def get_category_id_by_name(cat_name):
    sql = f"""
    SELECT 
        *
    FROM photo_categories 
    WHERE name LIKE "%{cat_name}%"
    """
    cursor.execute(sql)
    return cursor.fetchall()


pp = pprint.PrettyPrinter(indent=4)


#Check if input and data folders exist 
if not os.path.exists('data_in'):
    os.mkdir('data_in')

if not os.path.exists('data_out'):
    os.mkdir('data_out')

schools = rd.read_data()

all_categories = []

for school in schools:
    print(school['name'], end=' ')
    isInserted = is_school_insered(school['name'])
    if not isInserted:
        print(f'Inserting school {school["name"]}')
        school_id = insert_new_school(school['name'])

    else: 
        school_id = get_school_id(school['name'])[0]
            
    if not os.path.exists(f'/srv/http/projects/ministery/img/{school_id}'):
        try: 
            os.mkdir(f'/srv/http/projects/ministery/img/{school_id}')
        except Exception as err:
            print(err)
            exit()

    #print(f"\n   {school['name']}")
    for cat in school['cats']:
        try:
            category_id = get_category_id_by_name(cat['subdir_name'])[0][0]
        except Exception as err:
            category_id = 16
    

        if cat['subdir_name'] not in all_categories:
            all_categories.append(cat['subdir_name'])

        #pprint.pprint(cat['subdir_name'])
        for photo in cat['files']:
            photo_ext = str(photo).split('.')[-1]
            photo_path_to = f"/home/vladislav/programming/python/school_image_parser/data_in/{school['name']}/{cat['subdir_name']}/До"
            photo_new_name = f"{school_id}-{randint(1,100)}-{randint(1,100)}-{randint(1,10)}.{photo_ext}"
            file_path_current = f"{photo_path_to}/{photo}"
            
            try:
                shutil.copy(file_path_current, f"/srv/http/projects/ministery/img/{school_id}/{photo_new_name}")
            except Exception as err:
                print(err)
            print('.',end='')
            insert_school_photo(school_id, category_id, f"img/{school_id}/{photo_new_name}")

    print('')

#print(all_categories)
#print(len(all_categories))
