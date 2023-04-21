filename = input("Введите имя файла: ")
content = ""

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            content += line
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")

print("Содержимое файла:")
print(content)
