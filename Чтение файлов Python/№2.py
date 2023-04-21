filename = input("Введите имя файла: ")
n = int(input("Введите количество строк для чтения: "))

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if line:
                print(line)
            else:
                break
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
