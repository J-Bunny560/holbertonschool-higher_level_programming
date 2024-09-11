#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list and returns the real number of elements printed.

    Args:
        my_list (list): The list to print elements from. Defaults to an empty list.
        x (int): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """
    try:
        printed = 0
        for i in range(x):
            print(my_list[i], end='')
            printed += 1
        print()
        return printed
    except IndexError:
        print()
        return printed
