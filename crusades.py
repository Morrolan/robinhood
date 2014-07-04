__author__ = 'morrolan'

import sherwood
from time import sleep

# as this is a third party module lets have some amount of error-checking involved.
try:
    import psutil
except ImportError:
    psutil = None


robin = sherwood.Merryman('Robin')
antidote_present = robin.check_for_antidote('marion.txt', 'HELP')


# for process in psutil.process_iter():
#
#     try:
#         print process.name()
#
#         if process.name() == 'mspaint.exe':
#             print "Woo!   Found mspaint.exe at pid: ({0})".format(str(process.pid))
#
#             _pid = process.pid
#
#             while True:
#                 if psutil.pid_exists(_pid) is True:
#                     print "mspaint still exists"
#                 else:
#                     print "mspaint has died :("




            # exit(0)

    # except psutil.AccessDenied:
    #     print "AccessDenied error:  Are you running as Administrator?"




#while antidote_present is False:
#    sleep(100)

# Marion needs to be expanded so that instead of creating objects, she creates complete python scripts that are ran
# via subprocess.call so that each instance, robin, friar or will, all have separate processes