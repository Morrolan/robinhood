__author__ = 'morrolan'

import os
#import psutil


def check_for_files():
    """
    Here we will do a cursory check for other viable instances of the program.
    I was thinking of somehow writing copies of this file to randomly chosen locations
    and then somehow making those locations available.
    """
    pass


def hide_oneself():
    """
    If I need to hide myself, i will do it here.  I am not not sure what form this will take.

    """
    pass


def check_for_antidote():
    """
    Here we will look for the antidote, which will be a text file of a particular name with particular contents.

    """
    with open(os.path.normpath(r"mead.txt")) as __antidote_file:
        __antidote_contents = __antidote_file.read()

        if __antidote_contents == "STOP":
            print("STOP THE MERRYMEN FROM DOING THEIR SHIT HERE...")


def save_friar():
    """


    """
    pass


def talk_to_friar():
    """
    Here I will check to see if the Friar is running.  At the moment I don't know how to identify
    a particular running process.  One possibility is to get the PID somehow and stash it somewhere
    for the other brother process to pick up and monitor.

    """
    pass

check_for_antidote()