#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed += 1
        print()
    except IndexError:
        print()
    return printed
