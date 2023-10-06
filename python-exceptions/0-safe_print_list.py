#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tot_element = 0
    try:
        for i in my_list:
            if tot_element < x:
                print(i, end="")
                tot_element += 1
            else:
                break
    except TypeError:
        pass
    finally:
        print()
    return tot_element
