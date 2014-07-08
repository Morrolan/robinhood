__author__ = 'morrolan'

import sherwood
from time import sleep

# as this is a third party module lets have some amount of error-checking involved

robin = sherwood.Merryman('Robin')
robin.check_for_antidote('marion.txt', 'HELP')

# Marion needs to be expanded so that instead of creating objects, she creates complete python scripts that are ran
# via subprocess.call so that each instance, robin, friar or will, all have separate processes