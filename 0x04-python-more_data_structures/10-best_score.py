#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    mkey = list(a_dictionary.keys())[0]

    for key in a_dictionary.keys():
        if a_dictionary[mkey] < a_dictionary[key]:
            mkey = key
    return mkey
