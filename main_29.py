# Сканер резюме с использованием Python
#
# pip install resume-parser


from resume_parser import resumeparse   # библиотека для получения данных из резюме


def scan_resume(resume):    # функция для получения данных из резюме
    data = resumeparse.read_file(resume)    # получение данных из файла
    for i, j in data.items():    # перебор ключей и значений в словаре
        print(f"{i}:>>{j}") # вывод на экран ключей и значений


scan_resume("Aman Kharwal.docx")    # вызов функции для получения данных из резюме
