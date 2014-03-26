__author__ = 'morrolan'

import sherwood


robin = sherwood.Merryman('robin')
print robin.name
antidote_present = robin.check_for_antidote('mead.txt', 'STOP')

# Marion needs to be expanded so that instead of creating objects, she creates complete python scripts that are ran
# via subprocess.call so that each instance, robin, friar or will, all have separate processes


#friar = sherwood.Merryman('friar')