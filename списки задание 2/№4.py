list = [3, 8, 12, 5, 7, 17, 21]
print(len(list))
print(list[-2])
print(list[::-1])
if 5 in list or 17 in list:
    print("YES")
else:
    print("NO")
del list[1]
del list[-1]
print(list)
