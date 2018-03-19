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

import sys                              # system class
from abc import ABC, abstractmethod     # abstract classes


####################

####################
# DATA DEFINITIONS #
####################

# A Lines is an object containing a (list-of String) and a current_selected
# A Stations is an object containing a (list-of String) and a current_selected
# A Station is an object containing a String designating a real MBTA station

# A current_selected is a string designating the current world item selected


####################

##################
# ABSTRACT CLASS #
##################

# Abstract world class for methods involving rendering world states
class World(ABC):

    def render_world(self):
        
        print(self.selection())

    
    # Produces a list to work with for rendering based on the Worldstate
    def selection(self):
        
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

        # I don't know what im doing for this yet lol        
        elif type(self) is Station:

            current_station = self.station

            list_appended = []
            list_appended.append(current_station)
            list_appended.append()
            list_appended.append(get_times(current_station))
            
            return list_appended


    # I don't really know how events work 
    def event_handler(self, event):

        if event == 'up':
           self.up_handler()

        elif event == 'down':
           self.down_handler() 

        elif event == 'left':
            pass

        elif event == 'right':
            pass

        elif event == 'quit':
            sys.exit()
        
        else:
            pass

    
    # Changes the world state based on when "up" is selected
    def up_handler(self):
        
        if type(self) is Lines:

            current_index = self.lines.index(self.current_selected)

            if current_index == 0:
                pass

            else:
                self.current_selected = self.lines(current_index - 1)


        if type(self) is Stations:

            current_index = self.stations.index(self.current_selected)

            if current_index == 0:
                pass

            else:
                self.current_selected = self.stations(current_index - 1) 

        else:
            pass


    # Changes the world state based on when "down" is selected
    def down_handler(self):
        
        if type(self) is Lines:

            current_index = self.lines.index(self.current_selected)

            if current_index == len(self.lines - 1):
                pass

            else:
                self.current_selected = self.lines(current_index + 1)


        if type(self) is Stations:

            current_index = self.stations.index(self.current_selected)

            if current_index == len(self.lines - 1):
                pass

            else:
                self.current_selected = self.stations(current_index + 1) 

        else:
            pass


    # Changes back to the previous world state when left is selected    
    def left_handler(self):

        if type(self) is Stations:

            self = self.came_from_lines

        if type(self) is Station:

            self = self.came_from_stations

        else:
 
            pass

    
    # Gets the current event for the event handler
    def get_current_event():
        
        return None


####################

################
# WORLD STATES #
################

# class for the world state of gathering the T data for a station
class Station(World):
    
    # Constructor method
    def __init__(self, station, came_from_stations):
        
        self.station = station 
        self.came_from_stations = came_from_stations


# Class for choosing all the different stations of a line
class Stations(World):
    
    # Constructor method
    def __init__(self, stations, current_selected, came_from_lines):
        
        self.stations = stations
        self.current_selected = current_selected
        self.came_from_lines = came_from_lines


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
        
        event = World.get_current_event()

        current_world.render_world()
        current_world.event_handler(event)


####################

#############
# EXECUTION #
#############

# Executes the main method
if __name__ == '__main__':
    main()

