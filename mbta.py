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

from abc import ABC, abstractmethod  # abstract classes


####################

####################
# DATA DEFINITIONS #
####################

# A Lines is an object containing a (list-of String) and a current_selected
# A Stations is an object containing a (list-of String) and a current_selected
# A Station is an object containing a String designating a real MBTA station

# A current_selected is a string designating the current world item selected


####################

###########
# CLASSES #
###########

# Abstract world class for methods involving rendering world states
class World(ABC):

    def render_world(self):
        
        print(self.append_selection())

    def append_selection(self):
        
        # Deals with appending the > for the current Line selection in the
        # Lines world state
        if type(self) is Lines:
            
            index_selected = self.lines.index(self.current_selected)
            
            list_appended = []
            for i in range(0, len(self.lines)):
                if i == index_selected:
                    list_appended.append(str('>' + self.lines[i]))
                else:
                    list_appended.append(str(' ' + self.lines[i]))
            
            return list_appended

        # Deals with appending the > for the current Line selection in the
        # Stations world state
        elif type(self) is Stations:
            
            index_selected = self.stations.index(self.current_selected)

            list_appended = []
            for i in range(0, len(self.stations)):
                if i == index_selected:
                    list_appended.append(str('>' + self.stations[i]))
                else:
                    list_appended.append(str(' ' + self.stations[i]))

            return list_appended
 
 
    def event_handler(self, world, key_event):

        pass
        

# Class for the world state of gathering the T data for a station
class Station(World):
    
    # Constructor method
    def __init__(self, station):
        
        self.station = station 


# Class for choosing all the different stations of a line
class Stations(World):
    
    # Constructor method
    def __init__(self, stations, current_selected):
        
        self.stations = stations
        self.current_selected = current_selected


# Class for choosing between the different lines
class Lines(World):
    
    # Constructor method
    def __init__(self, lines, current_selected):

        self.lines = lines
        self.current_selected = current_selected




####################

###############
# MAIN METHOD #
###############

# main method weow!!
def main():
    
    # Initializing a "Big Bang" type structure
    running = True 
    
    # These are the lines weow!
    line_list = ['Blue Line',
            'Green Line',
            'Orange Line',
            'Red Line',
            'Silver Line']

    current_selected = 'Blue Line'

    current_world = Lines(line_list, current_selected)

    # Big Bang for my beautiful universe
    while running:
        
       current_world.render_world()


####################

#############
# EXECUTION #
#############

# Executes the main method
if __name__ == '__main__':
    main()

