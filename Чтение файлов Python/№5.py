filename = input("Введите имя файла: ")
lines = []

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")

print("Содержимое файла:")
print(lines)
