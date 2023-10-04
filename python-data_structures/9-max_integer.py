#!/usr/bin/python3
def max_integer(my_list=[]):
    big_num = my_list[0]
    if my_list == "":
        return None
    for i in my_list[1:]:
        # iterate starting from the seconde element
        if i > big_num:
            big_num = i
            return big_num
