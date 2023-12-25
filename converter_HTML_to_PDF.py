from bs4 import BeautifulSoup
import os
import pdfkit
import codecs


person = {
    # Основная информация
    "photo-user": "../Palto.png",
    "FIO": "Макаров Андрей Владимирович",
    "post": "Юрист",
    "city": "г.Москва",
    "removal": "(возможен переезд)",

    # Личная информация
    "citizenship": "Российская Федерация",
    "education-person": "Высшее",
    "date-of-birth": "12 июля 1978 (40 лет)",
    "gender": "Мужской",
    "marital-status": "Женат  (есть дети)",

    # Навыки, контакты, зарплата
    "salary": "100 000 руб.",
    "busyness": "Полная занятость",
    "chart": "Полный день",
    "email": "andrey@simpledoc.ru",
    "phone": "+74950000001",
    "languages": "Английский (разговорный) - 2 года проживал в Лондоне;"
                 "Китайский - 3 месяца обучения;",
    "skills": "Печать, сканирование, копирование документов, Интернет, Электронная почта"
              " Microsoft Word, Microsoft Excel, Microsoft Power Point, Консультант плюс, Гарант",

    # Опыт работы
    "work-experience": {
        "work-experience-1": {
            "work-post": "Юрисконсульт",
            "work-organization": "ГК «Спутник», г. Москва",
            "duration": "май 2016 - настоящее время (2 года)",
            "duties": "Правовое сопровождение деятельности и защита интересов в суде компаний входящих в группу;"
                      "Работа с интеллектуальной собственностью, лицензионными соглашениями, регистрация товарного знака;"
                      "Консультирование сотрудников компании по правовым вопросам в сфере продаж, логистики, аудита и налогообложения;"
                      "Согласование и экспертная оценка договоров в системе электронного документооборота;"
                      "Создание филиалов и обособленных подразделений;",

            "achievements": "Заключение международных договорных отношений с компаниями «Leroy Merlin», «Shell»;"
                            "Сопровождение крупных коммерческих проектов с участием компании «Лукойл»;"
                            "Внедрение современных методов работы с правовой информацией;"
                            "Успешная подготовка изменений в действующее региональное законодательство."
        },
        "work-experience-2": "",
        "work-experience-3": ""
    },

    # Образование
    "education": {
        "education-1": {
            "educational-institution": "Московский государственный университет им Ломоносова",
            "faculty": "Юридический",
            "specialization": "Коммерческое и договорное право",
            "year-of-graduation": "2004 (15 лет назад)",
            "form-of-training": "Очная"
        },
        "education-2": "",
        "education-3": ""
    },

    # Курсы
    "courses": {
        "courses-1": {
            "course-specialization": "Правовое сопровождение международного бизнеса",
            "course-educational-institution": "Международный экзаменационный Центр",
            "course-year-of-graduation": "2016 (3 года назад)",
            "course-citizenship": "3 месяца"
        },
        "courses-2": "",
        "courses-3": ""
    },

    # Дополнительная информация
    "army": "служил",
    "driver-license": "B",
    "recommendations": "Петров Алексей Борисович (ООО «Экспорт+», г. Москва, директор) - +7 (495) 000-00-02",
    "free-time": "Рыбалка, охота, туризм, автомобильный спорт",
    "personal-qualities": "Трудолюбие, отсутствие вредных привычек, инициативность, ответственность, "
                          "коммуникабельность, быстрая обучаемость, хорошая письменная и устная речь, "
                          "самоорганизованность, структурное мышление",
}
Pattern = 'Pattern_1_1'


path_to_file = f'{Pattern}/index.html'
output_path = f'{Pattern}.pdf'


with codecs.open(path_to_file, encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


for key, value in person.items():
    element = soup.find(id=key)
    if element:
        if element.name == 'img':
            element['src'] = value
        elif key == 'languages' or key == 'skills':
            ul = element.find('ul')
            if(key == 'languages'):
                parts = value.split(';')
            else:
                parts = value.split(', ')
            parts = [part.strip() for part in parts if part.strip()]
            for part in parts:
                li = soup.new_tag("li")
                li.string = part
                ul.append(li)
        elif element.name == 'section':
            ul = element.find('ul')
            if ul and value:
                pre_key = next(iter(value))
                html_code = ul.find(id=pre_key)
                ul.clear()
                for s_key, s_value in value.items():
                    if s_value:
                        tag_li = soup.new_tag("li", **{"class": "container list-item"})
                        tag_li.insert(0, html_code)
                        tag_li.li.unwrap()
                        tag_li['id'] = s_key

                        for sub_key, sub_value in s_value.items():
                            temp_element = tag_li.find(id=sub_key)
                            if sub_key in ['duties', 'achievements']:
                                parts = sub_value.split(';')
                                parts = [part.strip() for part in parts if part.strip()]
                                for part in parts:
                                    li = soup.new_tag("li")
                                    li.string = part
                                    temp_element.append(li)
                            else:
                                temp_element.string = sub_value

                        ul.append(tag_li)
                        html_code = ul.find(id=pre_key)
                        pre_key = s_key
            else:
                element.string = value
        else:
            element.string = value

soup.find(id="photo-user")['style'] = 'border: 2px solid #D0D0D0'


with codecs.open(f'{Pattern}/temporary_file.html', "w", "UTF-8") as file:
    file.write(str(soup))

path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

pdfkit.from_file(input=f'{Pattern}/temporary_file.html', output_path=output_path, options={"enable-local-file-access": True, 'margin-top': '0', 'margin-right': '0', 'margin-left': '0', 'margin-bottom': '0'}, configuration=config, verbose=True)

os.remove(f'{Pattern}/temporary_file.html')










'''

*Basic-information
    photo-user, FIO, post, city, removal, 

*Personal-information
    citizenship, education-person, date-of-birth, gender, marital-status
    
*Aside-information:
    salary, busyness, chart, email, phone, languages, skills,    

Work-experience
    work-experience-1, work-post, work-organization, duration, duties, achievements

Education
    educational-institution, faculty, specialization, year-of-graduation, form-of-training

Courses
    course-specialization, course-educational-institution, course-year-of-graduation, course-citizenship

*Additional-information
    army, driver-license, recommendations, free-time, personal-qualities

'''

# import mysql.connector
# from mysql.connector import Error

# def create_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password,
#             database=db_name
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
#
# connection = create_connection("92.246.214.15", "ais_samoylov1874_resume_db", "OmbywTmanixEUxx7cFIjOe42", "ais_samoylov1874_resume_db")