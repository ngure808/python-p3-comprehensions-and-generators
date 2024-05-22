#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [i for i in num_list if i % 2 == 0]
    return (num_list)
    pass

def make_exclamation(sentence_list):
    modified_list = [sentence + "!" for sentence in sentence_list]
    return modified_list
    pass
