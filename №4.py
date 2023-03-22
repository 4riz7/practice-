queens = []
for i in range(8):
    queens.append(tuple(map(int, input().split())))

is_beat = False

# Проверяем каждую пару ферзей на угрозу друг другу
for i in range(8):
    for j in range(i + 1, 8):
        if queens[i][0] == queens[j][0] or \
           queens[i][1] == queens[j][1] or \
           abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
            is_beat = True

if is_beat:
    print("YES")
else:
    print("NO")
