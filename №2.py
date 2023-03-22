def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    result.sort()
    return result

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 4, 7, 8]
print(common_elements(list1, list2))  # выводит [3, 7]
