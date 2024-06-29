from csv import DictReader, DictWriter
from os.path import exists

class LenNumberError(Exception):
    def init(self, txt):
        self.txt = txt

def get_info():
    first_name = "Ivan"
    second_name = "Ivanov"
    isvalidnumber = False
    while not isvalidnumber:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Невалидная длина") 
        except ValueError:
            print("Невалидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue
        isvalidnumber = True
    return first_name, second_name, phone_number

def create_file(file_name):
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        r_reader = DictReader(data)
        return list(r_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el.get('телефон') == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    fieldnames = ['имя', 'фамилия', 'телефон']  # Убедимся, что ключи соответствуют fieldnames
    if all(key in obj.keys() for key in fieldnames):
        res.append(obj)
        with open(file_name, 'w', encoding='utf-8', newline="") as data:
            f_writer = DictWriter(data, fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)
        print("Данные успешно записаны в файл.")
    else:
        print("Некорректные данные для записи в файл.")




def copy_line(source_file, dest_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as source_data:
        r_reader = DictReader(source_data)
        data = list(r_reader)

    if line_number <= len(data):
        line_to_copy = data[line_number - 1]
        
        with open(dest_file, 'a', encoding='utf-8', newline="") as dest_data:
            f_writer = DictWriter(dest_data, fieldnames=data[0].keys())  # Используем ключи из первой строки для заголовка
            if not exists(dest_file):
                f_writer.writeheader()

            f_writer.writerow(line_to_copy)
            print(f"Строка {line_number} была успешно скопирована в файл {dest_file}")
    else:
        print("Некорректный номер строки")



def main():
    file_name = str(input("Введите название файла: "))
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует")
                continue
            data = read_file(file_name)
            print(*data)
        elif command == 'c':
            source_file = input("Введите путь к исходному файлу: ")
            dest_file = input("Введите путь к файлу, в который нужно скопировать данные: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_line(source_file, dest_file, line_number)

if __name__ == "__main__":
    main()
