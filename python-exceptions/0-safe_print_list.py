#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    if type(x) != int:
        raise ValueError("x is not an integer")

    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break

    print()

    return count
