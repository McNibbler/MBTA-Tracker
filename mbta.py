###########################################
# MBTA LCD Train Tracker for Raspberry Pi #
# Version 0.1                             #
# March 17, 2018                          #
#                                         #
# Developed by: Thomas Kaunzinger         #
###########################################

####################

#####################
# IMPORT STATEMENTS #
#####################

from abc import abc     # abstract classes


####################

###########
# CLASSES #
###########

# World class for methods involving rendering world states
class World(abc):
    
    pass


# Class for displaying and choosing all the different stations of a line
class Line(World):
    
    # Constructor method
    def __init__(self, stations):
        
        self.stations = stations


####################

###############
# MAIN METHOD #
###############

# main method weow!!
def main():
    memes = 'bobs'
    print(memes)


####################

#############
# EXECUTION #
#############

# Executes the main method
if __name__ == '__main__':
    main()

