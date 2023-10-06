#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:

        high_val = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == high_val:
                return (key)
