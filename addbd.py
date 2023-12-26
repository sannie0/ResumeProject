import mysql.connector
from datetime import datetime
from mysql.connector import Error

# Словарь с данными пользователя
user_data = {
    "surname": "Иванов",
    "name": "Иван",
    "patronymic": "Иванович",
    "photo": "ivanov_photo.jpg",
    "post": "Инженер",
    "desired_table": "Желаемая таблица",
    "busyness": "Полная занятость",
    "work_schedule": "Гибкий график",
    "phone": "12345678901",
    "email": "ivanov@example.com",
    "service_in_army": True,
    "driver_license": "Категория B",
    "recommendations": "Рекомендации от предыдущего работодателя",
    "classes_in_free_time": "Чтение, спорт",
    "personal_qualities": "Ответственность, коммуникабельность",
    "start_of_work_1": datetime(2010, 1, 1),
    "end_of_work_1": datetime(2015, 12, 31),
    "position_1": "Инженер-программист",
    "organization_1": "IT Company",
    "responsibilities_and_achievements_1": "Разработка программного обеспечения",
    "start_of_work_2": datetime(2010, 1, 1),
    "end_of_work_2": datetime(2015, 12, 31),
    "position_2": "Инженер-программист",
    "organization_2": "IT Company",
    "responsibilities_and_achievements_2": "Разработка программного обеспечения",
    "start_of_work_3": datetime(2010, 1, 1),
    "end_of_work_3": datetime(2015, 12, 31),
    "position_3": "Инженер-программист",
    "organization_3": "IT Company",
    "responsibilities_and_achievements_3": "Разработка программного обеспечения",
    "course_name_1": "Course 1",
    "educational_institution_1": "University 1",
    "year_of_graduation_1": 2023,
    "duration_1": "3 months",
    "course_name_2": "Course 2",
    "educational_institution_2": "University 2",
    "year_of_graduation_2": 2023,
    "duration_2": "6 months",
    "course_name_3": "Course 3",
    "educational_institution_3": "University 3",
    "year_of_graduation_3": 2023,
    "duration_3": "1 year",
    "university_1":"value",
    "faculty_1":"value",
    "specialization_1":"value",
    "year_graduation_1":datetime(2015, 12, 31),
    "form_education_1":"value",
    "university_2":"value",
    "faculty_2":"value",
    "specialization_2":"value",
    "year_graduation_2":datetime(2015, 12, 31),
    "form_education_2":"value",
    "university_3":"value",
    "faculty_3":"value",
    "specialization_3":"value",
    "year_graduation_3":datetime(2015, 12, 31),
    "form_education_3":"value",
    "city":"value",
    "citizenship":"value",
    "birthdate":datetime(2015, 10, 31),
    "gender":"value",
    "marital_status":"value",
    "form_education":"value"
}

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

connection = create_connection("92.246.214.15", "ais_samoylov1874_resume_db", "OmbywTmanixEUxx7cFIjOe42", "ais_samoylov1874_resume_db")

# # Подключение к базе данных
# conn = mysql.connector.connect(
#     host="92.246.214.15",
#     user="ais_samoylov1874_resume_db",
#     password="OmbywTmanixEUxx7cFIjOe42",
#     database="ais_samoylov1874_resume_db"
# )

cursor = connection.cursor()

# Вставка данных в таблицу additional_information
insert_additional_info_query = """
INSERT INTO additional_information (service_in_army, driver_license, recommendations, classes_in_free_time, personal_qualities)
VALUES (%s, %s, %s, %s, %s);
"""

cursor.execute(insert_additional_info_query, (
    user_data["service_in_army"],
    user_data["driver_license"],
    user_data["recommendations"],
    user_data["classes_in_free_time"],
    user_data["personal_qualities"],
))

# Получение ID вставленной записи
additional_info_id = cursor.lastrowid

# Вставка данных в таблицу work_experience
insert_work_experience_query = """
INSERT INTO work_experience (
    start_of_work_1, end_of_work_1, position_1, organization_1, responsibilities_and_achievements_1,
    start_of_work_2, end_of_work_2, position_2, organization_2, responsibilities_and_achievements_2,
    start_of_work_3, end_of_work_3, position_3, organization_3, responsibilities_and_achievements_3
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

cursor.execute(insert_work_experience_query, (
    user_data["start_of_work_1"], user_data["end_of_work_1"], user_data["position_1"],
    user_data["organization_1"], user_data["responsibilities_and_achievements_1"],
    user_data["start_of_work_2"], user_data["end_of_work_2"], user_data["position_2"],
    user_data["organization_2"], user_data["responsibilities_and_achievements_2"],
    user_data["start_of_work_3"], user_data["end_of_work_3"], user_data["position_3"],
    user_data["organization_3"], user_data["responsibilities_and_achievements_3"],
))

# Получение ID вставленной записи
work_experience_id = cursor.lastrowid

# Вставка данных в таблицу courses_and_trainings
insert_courses_and_trainings_query = """
INSERT INTO courses_and_trainings (
    course_name_1, educational_institution_1, year_of_graduation_1, duration_1,
    course_name_2, educational_institution_2, year_of_graduation_2, duration_2,
    course_name_3, educational_institution_3, year_of_graduation_3, duration_3
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

cursor.execute(insert_courses_and_trainings_query, (
    user_data.get("course_name_1"), user_data.get("educational_institution_1"),
    user_data.get("year_of_graduation_1"), user_data.get("duration_1"),
    user_data.get("course_name_2"), user_data.get("educational_institution_2"),
    user_data.get("year_of_graduation_2"), user_data.get("duration_2"),
    user_data.get("course_name_3"), user_data.get("educational_institution_3"),
    user_data.get("year_of_graduation_3"), user_data.get("duration_3"),
))

# Получение ID вставленной записи
courses_and_trainings_id = cursor.lastrowid

# Вставка данных в таблицу education_information
insert_education_info_query = """
INSERT INTO education_information (
    university_1, faculty_1, specialization_1, year_graduation_1, form_education_1,
    university_2, faculty_2, specialization_2, year_graduation_2, form_education_2,
    university_3, faculty_3, specialization_3, year_graduation_3, form_education_3
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

cursor.execute(insert_education_info_query, (
    user_data.get("university_1"), user_data.get("faculty_1"),
    user_data.get("specialization_1"), user_data.get("year_graduation_1"), user_data.get("form_education_1"),
    user_data.get("university_2"), user_data.get("faculty_2"),
    user_data.get("specialization_2"), user_data.get("year_graduation_2"), user_data.get("form_education_2"),
    user_data.get("university_3"), user_data.get("faculty_3"),
    user_data.get("specialization_3"), user_data.get("year_graduation_3"), user_data.get("form_education_3"),
))

# Получение ID вставленной записи
education_info_id = cursor.lastrowid


# Вставка данных в таблицу personal_information
insert_personal_info_query = """
INSERT INTO personal_information (
    city, citizenship, birthdate, gender, marital_status, form_education
)
VALUES (%s, %s, %s, %s, %s, %s);
"""

cursor.execute(insert_personal_info_query, (
    user_data.get("city"),
    user_data.get("citizenship"),
    user_data.get("birthdate"),
    user_data.get("gender"),
    user_data.get("marital_status"),
    user_data.get("form_education"),
))

# Получение ID вставленной записи
personal_info_id = cursor.lastrowid


# Вставка данных в таблицу personal_information
insert_basic_info_query = """
INSERT INTO basic_information (
    surname, name, patronymic, photo, post, desired_table, busyness, work_schedule, phone, email,
    personal_information_id, education_information_id, work_experience_id, courses_and_trainigs_id, additional_information_id
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

cursor.execute(insert_basic_info_query, (
    user_data["surname"], user_data["name"], user_data["patronymic"], user_data["photo"], user_data["post"],
    user_data["desired_table"], user_data["busyness"], user_data["work_schedule"], user_data["phone"], user_data["email"],
    personal_info_id, education_info_id, work_experience_id, courses_and_trainings_id, additional_info_id,
))

# Подтверждение изменений в базе данных
connection.commit()

# Закрытие соединения
cursor.close()
connection.close()

