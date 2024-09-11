#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed = 0
        for i in range(x):
            print(my_list[i], end='')
            printed += 1
        print()
        return printed
    except:
        print()
        return 0
