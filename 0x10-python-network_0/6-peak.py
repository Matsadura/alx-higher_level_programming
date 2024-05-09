#!/usr/bin/python3
""" Module that contains the find_peak function """


def find_peak(list_of_integers):
    """
        A function that finds a peak in a list of unsorted integers

        Args:
            list_of_integers (list): The list to go trough

        Return:
            The peak
    """
    for i in range(len(list_of_integers) - 1):
        if i == 0:
            continue
        if list_of_integers[i] > list_of_integers[i + 1] and\
           list_of_integers[i] > list_of_integers[i - 1]:
            return list_of_integers[i]
    if len(list_of_integers) > 0:
        return list_of_integers[0]
