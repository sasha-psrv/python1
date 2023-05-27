# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# with open('file.txt', 'w', encoding='utf-8') as file:
#     file.write('первая строка в этом файле')

# with open('file.txt', 'a', encoding='utf-8') as file:
#     file.write('\nвторая строка в этом файле')

# with open('file.txt', 'r', encoding='utf-8') as fd:
#     z = fd.readlines()  
#     for i in z:
#         print(i)
   

def add_contact(f):
    input_name = input('введите имя: ')
    input_last_name = input('введите фамилию: ')
    input_phone = input('введите номер телефона: ')
    data = f'{input_last_name} {input_name} - {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list
    

def print_all(f):
    ard_book = read_all(f)
    for line in ard_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    last_name = input('введите фамилию: ')
    ard_book = read_all(f)
    print(len(ard_book))
    for i in range(len(ard_book)):
        print(i)
        print(ard_book[i])
    # for line in ard_book:
    #     if last_name in line:
    #         print(line)


def main():
    file = 'address_book.txt'
    while True:
        user_choise = input('1 - добавить запись, 2 - прочитать всю тел.книгу, 3 - найти запись, z - для выхода:  ')
        if user_choise == '1':
            add_contact(file)
        elif user_choise == '2':
            print_all(file)
        elif user_choise == '3':
            search_contact(file)
        elif user_choise == 'z':
            print('всего хорошего')
            break


if __name__ == '__main__':
    main()

