__author__ = 'morrolan'

import sherwood
from time import sleep

# as this is a third party module lets have some amount of error-checking involved.
try:
    import psutil
except ImportError:
    psutil = None


robin = sherwood.Merryman('Robin')
print "Name: " + robin.name
antidote_present = robin.check_for_antidote('marion.txt', 'HELP')

for p in psutil.process_iter():
    #print(p)
    print p.name()

#while antidote_present is False:
#    sleep(100)

# Marion needs to be expanded so that instead of creating objects, she creates complete python scripts that are ran
# via subprocess.call so that each instance, robin, friar or will, all have separate processes


#friar = sherwood.Merryman('friar')