max1 = max2 = 0

while True:
    x = int(input())
    if x == 0:
        break
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x

print(max2)
