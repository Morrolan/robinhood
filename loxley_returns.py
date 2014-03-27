__author__ = 'morrolan'

import sherwood
from time import sleep

# as this is a third party module lets have some amount of error-checking involved.
try:
    import psutil
except ImportError:
    psutil = None


robin = sherwood.Merryman('Robin')
print "Name: " + str(robin.get_name)
antidote_present = robin.check_for_antidote('marion.txt', 'HELP')


for p in psutil.process_iter():

    try:
        print p.name()

        if p.name() == 'python.exe':
            print "Woo!   Found Python at pid: ({0})".format(str(p.pid))
            exit(0)

    except psutil.AccessDenied:
        print "AccessDenied error:  Are you running as Administrator?"




#while antidote_present is False:
#    sleep(100)

# Marion needs to be expanded so that instead of creating objects, she creates complete python scripts that are ran
# via subprocess.call so that each instance, robin, friar or will, all have separate processes


#friar = sherwood.Merryman('friar')