#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    high_val = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        a_dictionary[key] == high_val
    return high_val
