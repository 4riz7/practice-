filename = input("Введите имя файла: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")

