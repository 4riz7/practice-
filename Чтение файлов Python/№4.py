filename = input("Введите имя файла: ")
n = int(input("Введите количество строк для чтения: "))

try:
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.readlines()[-n:]
        print("Последние", n, "строк файла:")
        for line in contents:
            print(line, end="")
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
