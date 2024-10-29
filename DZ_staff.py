from tabulate import tabulate
head = ['Имя', 'Фамилия', 'Возраст', 'Должность']
def print_staffs(staffs):

    table = tabulate(staffs, headers=head, tablefmt='grid')
    print(table)

def load_staffs(filename='staff_info.txt'):
    staffs = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    staffs.append(parts)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Будет создан новый файл.")
    return staffs

def save_staffs(staffs, filename='staff_info.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        table = tabulate(staffs, headers=head, tablefmt='grid')
        file.write(table)

def add_staff(staffs):
    f_name = input('Введите имя сотрудника: ')
    s_name = input('Введите фамилию сотрудника: ')
    age = input('Введите возраст сотрудника: ')
    post = input('Введите должность сотрудника: ')
    staffs.append([f_name, s_name, age, post])
    print('Сотрудник добавлен')
    save_staffs(staffs)

def rename_staff(staffs):
    print_staffs(staffs)
    index = int(input("Введите номер сотрудника, которого хотите переименовать: ")) - 1
    if 0 <= index < len(staffs):
        new_f_name = input('Введите новое имя: ')
        new_s_name = input('Введите новую фамилию: ')
        staffs[index][0] = new_f_name
        staffs[index][1] = new_s_name
        print('Сотрудник переименован')
        save_staffs(staffs)
    else:
        print('Неверный номер сотрудника')

def search_staff(staffs):
    search_query = input('Введите имя, фамилию, возраст или должность для поиска: ')
    found = False
    for i, staff in enumerate(staffs):
        if search_query.lower() in ''.join(staff).lower():
            print(f'Сотрудник найден: {i + 1}. {", ".join(staff)}')
            found = True
    if not found:
        print('Сотрудник не найден')

def delete_staff(staffs):
    print_staffs(staffs)
    index = int(input("Введите номер сотрудника, которого хотите удалить: ")) - 1
    if 0 <= index < len(staffs):
        del staffs[index]
        print('Сотрудник удален')
        save_staffs(staffs)
    else:
        print('Неверный номер сотрудника')

def menu(staffs):
    while True:
        print('--- Информационная система Сотрудники ---')
        print('1. Ввод данных')
        print('2. Редактирование')
        print('3. Удаление')
        print('4. Поиск')
        print('5. Вывод информации на экран')
        print('6. Выход')

        choice = input('Выберите номер операции: ')

        if choice == '1':
            add_staff(staffs)
        elif choice == '2':
            rename_staff(staffs)
        elif choice == '3':
            delete_staff(staffs)
        elif choice == '4':
            search_staff(staffs)
        elif choice == '5':
            print(print_staffs(staffs))
        elif choice == '6':
            print('До свидания!')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

staffs = load_staffs()
menu(staffs)