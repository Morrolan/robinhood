__author__ = 'morrolan'

import os
import random

# as this is a third party module lets have some amount of error-checking involved.
try:
    import psutil
except ImportError:
    psutil = None


class Merryman(object):

    __all__ = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def check_for_files(self):
        """
        Here we will do a cursory check for other viable instances of the program.
        I was thinking of somehow writing copies of this file to randomly chosen locations
        and then somehow making those locations available.
        """
        pass

    def hide_oneself(self):
        """
        If I need to hide myself, i will do it here.  I am not not sure what form this will take.

        """
        pass

    @staticmethod
    def check_for_antidote(antidote_file, antidote_key):
        """
        Here we will look for the antidote, which will be a text file of a particular name with particular contents.
        Marion should choose this when spawning the merrymen, and it should be obfuscated in some way that isn't easy
        to find out retrospectively.
        """
        try:
            with open(os.path.normpath(antidote_file)) as _antidote_file:
                _antidote_contents = _antidote_file.read()

                if antidote_key in _antidote_contents:
                    print("STOP THE MERRYMEN FROM DOING THEIR SHIT HERE...")
                    return True
                else:
                    return False

        except IOError:
            _result = random.randint(0, 3)
            if _result == 0:
                # would be nice to have a choice of sentences here.  Maybe create a list and have a random choice chosen
                # and printed from it?
                print("Wench!  Why hath thou not brought forth more Meade?")
            return False

    def talk_to_friar(self):
        """
        Here I will check to see if the Friar is running.  At the moment I don't know how to identify
        a particular running process.  One possibility is to get the PID somehow and stash it somewhere
        for the other brother process to pick up and monitor.

        """
        pass

    def save_friar(self):
        """
        here we need to figure out and watch for the friar dying.

        Ideally it needs to be platform-agnostic, so using something like psutil module would be ideal, if I could get
        it to install on OSX!
        """
        pass







