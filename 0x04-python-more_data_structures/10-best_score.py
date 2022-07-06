#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return(None)
    return(max(zip(a_dictionary.values(), a_dictionary.keys()))[1])


