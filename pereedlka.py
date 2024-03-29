"""
Для решения задач мы будем использовать стандартные библиотеки Python:
- csv, библиотека для работы с файлами формата csv
- random, библиотека для генерации случайных чисел
- string, для облегчения работы со строковыми значениями
"""
import csv
import random
import string


def fio(fio_):
    """
    Функция для 2-го и 3-го задания
    :param fio_: принимает Фамилию Имя и Отчество
    :return: возвращает Фамилию и Имя
    """
    return " ".join(fio_.split()[:2])
# Задание №1
# Все ребята сдали свои проекты и получили оценки на защите, но Хадаров Владимир все прослушал и просит помочь ему
# узнать какую оценку за проект он получил. Пожалуйста, подскажите Владимиру какую оценку он получил. Формат вывода:
# Ты получил: <ОЦЕНКА>, за проект - <id>
# Пока помогали Владимиру, увидели, что многие ученики потеряли свои оценки при выкачке с сайта. Из-за этого нет
# возможности посмотреть общую статистику. Чтобы избежать путаницы поставьте вместо ошибки среднее значение по классу и
# округлите до трех знаков после запятой. Сохраните данные в новую таблицу с названием student_new.csv.


with open("students.csv", encoding="utf-8") as file: # для открытия файла используем конструкцию with open. Для корректной работы с кириллицей указываем кодировку encoding="utf-8"
    reader = list(csv.DictReader(file, delimiter=",", quotechar="'")) # считываем в переменную содержимое в файле в виде объекта DictReader и преобразуем его в список,
    # в результате получается список словарей. Dictreader получает 3 аргумента: файл, разделитель и кавычки, в которые будут помещены ключ и значения словаря.
    _ = input("Введите Фамилию и Имя ученика.")
    score = {}  # создаём пустой словарь, куда будут добавляться классы и оценки, для дальнейшего рассчета среднего значения по классу.
    new_file = [] # список для формирования нового csv файла.

    #---------------------------------------Заполним словарь score--------------------------------
    for row in reader:     # проходимся по каждой строчке считанной таблицы
        if row["score"] != "None":        # если значение оценки не равно None
            if row["class"] not in score:      # если класс отсутствует
                score[row["class"]] = [int(row["score"])]    # создаём класс, в который сразу помещаем первую оценку
            else:
                score[row["class"]].append(int(row["score"]))   # добавляем оценку в класс

    #---------------------------------------Преобразуем значения в словарь score в средние---------------------
    for class_, s in score.items():  # проходимся по каждой строчке считанной таблицы
        score[class_] = round(sum(s)/len(s) if len(s) != 0 else 0, 3)  # посчитаем среднее значение по классу. Функция
        # round(x, y) позволяет сделать округление, где "x" - значение, а "y" - кол-во знаков после запятой.
        # Среднее значение считается, если длина "x" больше нуля, иначе в "x" записывается нуль.

    #---------------------------------------Заменим в таблице значения оценок "None" на средние по классу--------------
    for row in reader:  # проходимся по каждой строчке считанной таблицы
        if row["score"] == "None":  # ищем строки, в которых значение оценки - None
            row["score"] = score[row["class"]]  # изменяем на среднее значение по классу
        new_file.append(row)  # добавляем в список строоку для формирования нового csv файла
        if _ in row["Name"]:  # проверим информацию по интересующему нам ученику
            print(f"Ты получил: {row['score']}, за проект - {row['titleProject_id']}")

with open("students_new.csv", "w", newline="", encoding="utf-8") as file:  # ключ "w" означает запись, а также если
    # файл отсутствует, создаёт его; newline указывает на то, что при записи будет использоваться пустая строка в
    # качестве символа новой строки
    w = csv.DictWriter(file, fieldnames=["id", "Name", "titleProject_id", "class", "score"]) # функция DictWriter
    # принимает два аргумента: файл, куда ведем запись и наименование столбцов
    w.writeheader()  # записываем заголовок, указанный в строке выше
    w.writerows(new_file)  # записываем значение в файл


# Задание 2
# Данные из таблицы student.csv необходимо отсортировать по столбцу оценки(score) с помощью сортировки вставками (В
# задаче нельзя использовать встроенные функции сортировок!). Из полученного списка выделите первых 3х победителей из
# 10 класса. Данные о победителях необходимо вывести в формате:
# <X> класс:
# 1 место: <И. Фамилия>
# 2 место: <И. Фамилия>
# 3 место: <И. Фамилия>
#

with open("students.csv", encoding="utf-8") as file:  # делаем по классу
    reader = list(csv.DictReader(file, delimiter=",", quotechar="'"))  #создаём список с содержимым файла
    scores = {}  # создаём пустой словарь для классов
    for row in reader:  # проходимся по каждой строчке таблицы
        class_ = row["class"]  # для удобства положим переменную в класс
        if class_ not in scores:  # если класса в словаре нет
            scores[class_] = [(row["Name"], int(row["score"]))] if row["score"] != "None" else [] # Добавляем класс, а
            # в него первую карточку ученика, если значение оценки не равно "None", иначе оставляем список пустым
        else:
            for i in range(len(scores[row["class"]])):  # считаем кол-во учеников в классе и проходимся по каждому
                if row["score"] != "None":  # если оценка не равна "None"
                    if scores[row["class"]][i][1] < int(row["score"]):  # Сравниваем значение оценки [1] i-го ученика в
                        # классе и оценки рассматриваемого ученика
                        scores[row["class"]].insert(i, (row["Name"], int(row["score"])))  # Если оценка i-го ученика
                        # меньше, то перед ним ставим рассматриваемого ученика
                        break
            else:
                if row["score"] != "None":  # Если в цикле ничего не поизошло и значение score не равно "None"
                    scores[row["class"]].append((row["Name"], int(row["score"])))

for k, z in scores.items():  # проходимся по словарю с классами
    if "10" in k:  # Нам нужны 10-е классы, так что смотрим наличие 10-ки в номере класса
        print(f"{k} класс.")
        [print(f"{x} Место: {fio(y[0])}") for x, y in enumerate(z[:3], start=1)]
        print("...")


# Задание №3
# Напишите небольшую программу, которая на вход будет получать id проекта (гарантируется, что вводимые числа всегда
# целые), а на выходе будет предоставлять информацию об ученике, который делал этот проект и его оценку за этот проект в
# формате: Проект № <N> делал: <И. Фамилия> он(а) получил(а) оценку - <ОЦЕНКА>. Если по заданному запросу ничего не
# найдено вывести: Ничего не найдено.
# Поиск ученика необходимо осуществить с помощью линейного поиска в файле students.csv.
# Ваша программа должна всегда работать и отключиться только в случае, когда пользователь введет СТОП.


with open("students.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter=",", quotechar="'"))
    while True:
        _ = input("Введите id проекта: ")
        if _ == "СТОП":
            break
        for i in reader:
            if i['titleProject_id'] == _:
                Name_ = fio(i["Name"])
                print(f"Проект № {i['titleProject_id']} делал: {Name_} он(а) получил(а) оценку - {i['score']}.")
                break
        else:
            print("Ничего не найдено")

# Задание №4
# Вам необходимо создать личные кабинеты для каждого пользователя, чтобы каждый из них видел свои достижения и мог лично
# взаимодействовать с вами. Для этого необходимо создать логины и пароли для каждого из школьников. Реализуйте
# методы/функции, которые будут генерировать логины и пароли для пользователей. Логин должен состоять из фамилии и
# инициалов, например, если школьника зовут Соколов Иван Иванович, его логин должен выглядеть как Соколов_ИИ. Также для
# каждого пользователя необходимо сгенерировать пароль, пароль должен состоять из 8 символов, включать в себя заглавные,
# строчные буквы английского алфавита и цифры.
# “0,Сербин Геннадий Михаилович,7,8в,2” → “0,Сербин Геннадий Михаилович,7,8в,2,Сербин_ГМ,fhGi45Bq”
# На вход подается CSV файл, который необходимо записать в список, для каждого элемента сгенерировать логин и пароль,
# после чего дополнить список сгенерированными элементами. Последним этапом полученный список записать в новый
# students_password.csv файл.


def create_initials(s):
    """
    :param s: Принимает ФИО,
    :return: возвращает логин формата Ф_ИО
    """
    names = s.split()  # преобразуем строку в список из трёх элементов
    return f"{names[0]}_{names[1][0]}{names[2][0]}"

def create_password():
    """
    :return: возвращает сгенерированный пароль
    """
    characters = string.ascii_letters + string.digits  # ascii_letters - возвращает в виде строки английский алфавит
    # содержащий прописные и строчные буквы; string.digits - возвращает в виде строки десятичные цифры
    while True:
        password = "".join(random.choice(characters) for _ in range(8))  # генерируем 8-ми значный пароль
        has_lowercase = any(x.islower() for x in password)  # проверяем наличие строчных букв
        has_uppercase = any(x.isupper() for x in password)  # проверяем наличие прописных букв
        has_digit = any(x.isdigit() for x in password)  # проверяем наличие цифр
        if has_digit and has_lowercase and has_uppercase:  # проверяем соответсвует ли пароль условиям
            return password


students_with_password = []  # создаём список для формирования нового файла
with open("students.csv", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter=",", quotechar="'"))
    for row in reader:
        row["login"] = create_initials(row["Name"])
        row["password"] = create_password()
        students_with_password.append(row)

with open("students_password.csv", "w", newline="", encoding="utf-8") as file:
    w = csv.DictWriter(file, fieldnames=["id", "Name", "titleProject_id", "class", "score", "login", "password"])
    w.writeheader()
    w.writerows(students_with_password)

# Задание №5
# В следующем году планируется дополнительный набор школьников на обучение, в связи с этим поиск по ФИО пользователя
# будет работать неэффективно. Необходимо составить хэш-таблицу, в которой будет выстроено соответствие ФИО и значения
# хэша ФИО. На основании этого необходимо составить хэш-таблицу и заменить id ученика на полученный хэш и результат
# записать в csv файл.
# Для хэширования необходимо использовать следующий алгоритм.
# hash(s) = s[0] * p ** 0 + s[1] * p ** 1 + s[2] * p ** 2 + ... + s[n - 1] * p ** n - 1 % m
# где p и m - некоторые выбранные положительные числа
# Рекомендации по выбору чисел p и m.
# Целесообразно сделать p простым числом, примерно равным количеству символов во входном алфавите. Например, если
# входные данные состоят только из строчных букв английского алфавита, можно взять p = 31. Если же входные данные могут
# содержать как прописные, так и строчные буквы, то возможен выбор p = 53. Если используются прописные и строчные буквы
# русского алфавита, а также символ пробел, то возможет выбор p = 67.
# m должно быть большим числом, так как вероятность столкновения двух случайных строк составляет примерно 1/m.
# на практике, m = 2 ** 64 не рекомендуется. Хорошим выбором для m является какое-либо большое простое число. (можно
# использовать m = 10 ** 9 + 9, это большое число, но все же достаточно малое, чтобы можно было выполнять умножение двух
# значений, используя 64-битные целые числа).
# Для вычисления хэша строки s, которая содержит только строчные буквы необходимо преобразовать каждый символ строки s в
# целое число. Можно использовать преобразование a →1, b →2, … z → 26. Преобразование a → 0 не является хорошей идеей,
# поскольку тогда хэши строк a, aa, aaa, … все оцениваются как 0.
# На вход подается CSV файл students.csv результаты необходимо записать в новый students_with_hash.csv файл.


def hash_fio(s, p=67, m=10 ** 9 + 9):
    """
    :param s: Передаваемое ФИО
    :param p: Целое простое число применяемое при расчете хэш значения
    :param m: Целое простое число применяемое при расчете хэш значения
    :return: Возвращает значение рассчитанное значение
    """
    hash_value = 0
    fio_hash = list(map(ord, list(s)))  # преобразуем строку в список
    for i in range(len(fio_hash)):
        hash_value += fio_hash[i] * p ** i
    return hash_value % m

students_with_hash = []  # создаём список для формирования нового файла
with open("students.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=",", quotechar="'")
    for row in reader:
        row['id'] = hash_fio(row["Name"])
        students_with_hash.append(row)

with open("students_with_hash.csv", "w", newline="", encoding="utf-8") as file:
    w = csv.DictWriter(file, fieldnames=["id", "Name", "titleProject_id", "class", "score"])
    w.writeheader()
    w.writerows(students_with_hash)