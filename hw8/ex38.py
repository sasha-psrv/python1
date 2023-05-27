# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


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


def update_contact(f):
    name = input("Введите имя или фамилию контакта, который хотите изменить: ")
    new_phone = input("Введите новый номер телефона: ")
    
    with open(f, "r", encoding='utf-8') as file:
        lines = file.readlines()
        
    
    found = False
    
    with open(f, "w", encoding='utf-8') as file:
        for line in lines:
            if name.lower() in line.lower():
                file.write(f" {line.split(':')[0]}:{new_phone}\n")
                found = True
            else:
                file.write(line)
    
    if found:
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")


def delete_contact(f):
    name = input("Введите имя или фамилию контакта, который хотите удалить: ")
    
    with open(f, "r", encoding='utf-8') as file:
        lines = file.readlines()
    
    found = False
    
    with open(f, "w", encoding='utf-8') as file:
        for line in lines:
            if name.lower() not in line.lower():
                file.write(line)
            else:
                found = True
    
    if found:
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")



def main():
    file = 'address_book.txt'
    while True:
        user_choise = input('1 - добавить запись, 2 - прочитать всю тел.книгу, 3 - изменить контакт, 4 - удалить контакт, z - для выхода:  ')
        if user_choise == '1':
            add_contact(file)
        elif user_choise == '2':
            print_all(file)
        elif user_choise == '3':
            update_contact(file)
        elif user_choise == '4':
            delete_contact(file)
        elif user_choise == 'z':
            print('всего хорошего')
            break


if __name__ == '__main__':
    main()

