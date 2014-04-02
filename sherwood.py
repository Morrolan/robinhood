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
        """

        :param name:
        """
        self.name = name
        self.pid = self.get_pid
        self.start()

    @property
    def get_name(self):
        """


        :return:
        """
        return self.name

    @staticmethod
    def get_pid():
        """

        :return:
        """
        if psutil is not None:
            pids = None

            for process in psutil.process_iter():
                try:
                    process_name = process.name()
                    if process_name.startswith('python'):
                        pids.append(process.pid)
                except psutil.AccessDenied:
                    # we pass here purely because we simply don't have access to all process data and we don't want our
                    # code to crash purely because we haven't accounted for differing security levels.
                    pass

            return pids

    def start(self):
        """
        Lets do some basic setup stuff that is cleaner in here than in __init__, like printing.

        """
        print("I am:  {0}".format(str(self.name)))
        print("Python PIDs:  {0}".format(str(self.pid())))

    def check_for_files(self):
        """
        Here we will do a cursory check for other viable instances of the program.
        I was thinking of somehow writing copies of this file to randomly chosen locations
        and then somehow making those locations available.
        """
        pass

    def hide_self(self):
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

                    return True

                else:
                    # Don't terminate the merrymen as no antidote has been found
                    return False

        except IOError:
            _result = random.randint(0, 3)
            if _result == 0:
                # would be nice to have a choice of sentences here.  Maybe create a list and have a random choice chosen
                # and printed from it?
                _response_list = ["Wench!  Why hath thou not brought forth more Meade?",
                                  "Wench!  Come hither and remove your undergarments!",
                                  "I hath been poisoned and Marion has ventured forth for an antidote, \
                                  but alas I fear she will not returneth in time!",
                                  "Where art though my fair Marion?"]

                _response_length = len(_response_list)
                _response_string = str(_response_list[random.randint(0, _response_length - 1)])

                print(_response_string)

            return False

    def find_others(selfself):
        """


        """
        pass

    def talk_to_others(self):
        """
        Here I will check to see if the Friar is running.  At the moment I don't know how to identify
        a particular running process.  One possibility is to get the PID somehow and stash it somewhere
        for the other brother process to pick up and monitor.

        """
        pass

    def save_others(self):
        """
        here we need to figure out and watch for the friar dying.

        Ideally it needs to be platform-agnostic, so using something like psutil module would be ideal, if I could get
        it to install on OSX!
        """
        pass







