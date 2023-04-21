filename = input("Введите имя файла: ")
text = input("Введите текст для добавления: ")

try:
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        print("Текст успешно добавлен в файл.")

    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
        print("Содержимое файла:")
        print(contents)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
