import mysql.connector
from datetime import datetime
from mysql.connector import Error
from collections import defaultdict


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("92.246.214.15", "ais_samoylov1874_resume_db", "OmbywTmanixEUxx7cFIjOe42",
                               "ais_samoylov1874_resume_db")


def read_from_table(connection, table_name):
    cursor = connection.cursor(dictionary=True)
    select_query = f"SELECT * FROM {table_name};"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


basic_information_dic = read_from_table(connection, "basic_information")
personal_information_dic = read_from_table(connection, "personal_information")
work_experience_dic = read_from_table(connection, "work_experience")
education_information_dic = read_from_table(connection, "education_information")
courses_and_trainings_dic = read_from_table(connection, "courses_and_trainings")
additional_information_dic = read_from_table(connection, "additional_information")

# print(basic_information_dic)

all_information = basic_information_dic.copy()

one_person_info_full = {}

work = work_experience_dic

keys_to_exclude = ['id']


for person in all_information:
    if person.get('id') == 2:
        one_person_info_full = person.copy()
        personal_info_id = person.get('personal_information_id')
        education_info_id = person.get('education_information_id')
        work_experience_id = person.get('work_experience_id')
        courses_and_trainings_id = person.get('courses_and_trainigs_id')
        additional_info_id = person.get('additional_information_id')

        for personal in personal_information_dic:
            if personal_info_id == personal.get('id'):
                for key, value in personal.items():
                    if key not in keys_to_exclude:
                        one_person_info_full[key] = value

        for additional in additional_information_dic:
            if additional_info_id == additional.get('id'):
                for key, value in additional.items():
                    if key not in keys_to_exclude:
                        one_person_info_full[key] = value

        for courses in courses_and_trainings_dic:
            if courses_and_trainings_id == courses.get('id'):
                for key, value in courses.items():
                    if key not in keys_to_exclude:
                        one_person_info_full[key] = value

        for education in education_information_dic:
            if education_info_id == education.get('id'):
                for key, value in education.items():
                    if key not in keys_to_exclude:
                        one_person_info_full[key] = value

        for work in work_experience_dic:
            if work_experience_id == work.get('id'):
                for key, value in work.items():
                    if key not in keys_to_exclude:
                        one_person_info_full[key] = value


print(one_person_info_full)


connection.close()