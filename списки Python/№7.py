list = [3, 5, 1, 9, 2, 8, 7, 4, 6]
min_idx = list.index(min(list))
max_idx = list.index(max(list))
list[min_idx], list[max_idx] = list[max_idx], list[min_idx]
print(list)
