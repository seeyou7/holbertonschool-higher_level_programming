#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary)
    for key in new_dic:
        print(f'{key}: {a_dictionary[key]}')
