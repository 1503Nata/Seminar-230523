#Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных.

"""with open('data.txt', 'w', encoding='utf-8') as file:
    data = ["Иванов Сергей Семенов - 8-1111111111 \n", "Князев Олег Игоревич - 8-2222222222 \n", "Сергеев Иван Петрович - 8-3333333333 \n"]
    file.writelines(data)"""
    
"""Создание функции для просмотра содержимого справочника"""  
def show_data():
    with open('data.txt', 'r', encoding='utf-8') as data:
        telbook = data.read()
    return telbook

"""Создание функции для добавления новой строки справочника"""
def new_data():
    with open('data.txt', 'a', encoding='utf-8') as data:
        data.write(input('Добавьте новый контакт: '+ '\n') )
    
"""Создание функции для поиска нужного контакта в справочнике"""
def find_data():
    with open('data.txt', 'r', encoding='utf-8') as data:
        telbook = data.read().split('\n')
        temp = input('Введите информацию для поиска: ')
        for i in telbook:
            if temp in i:
                print(i)

"""Создание функции для удаления записи из справочника"""
def delete_person(name):
    
    with open("data.txt", "w", encoding="utf8" ) as data:
        persons = data.read()
        for person in persons:
            if name != person:
                data.write(person)

"""Создание функции для изменения записи"""
def change_person(new_name, old_name):
    with open("data.txt", "w", encoding="utf8" ) as data:
        persons = data.read()
        for person in persons:
            if  old_name != person:
                data.write(person)
            else:
                data.write(new_name + "\n")

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-чтение файла, 1-поиск информации, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '0':
        print(show_data())
    elif mode == '1':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('Какой контакт Вы хотите удалить : ')
        delete_person(name)
    elif mode == '4':
        old_name = input('Какой контакт Вы хотите переименовать?: ')
        new_name = input('Введите новое название контакта: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('Режим не выбран')