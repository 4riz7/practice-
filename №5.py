def print_sequence():
    n = int(input())
    if n == 0:
        return
    print_sequence()
    print(n)
