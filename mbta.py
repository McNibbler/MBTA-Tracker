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

# Abstract world class for methods involving rendering world states
class World(abc):
    
    pass


# Class for the world state of gathering the T data for a station
class Station(World):
    
    # Constructor method
    def __init__(self, station)
        
        self.station = station 


# Class for choosing all the different stations of a line
class Stations(World):
    
    # Constructor method
    def __init__(self, stations):
        
        self.stations = stations


# Class for choosing between the different lines
class Lines(World):
    
    # Constructor method
    def __init__(self, lines):

        self.lines = lines




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

