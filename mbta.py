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
import RPi.GPIO as GPIO                 # Keyboard inputs


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

    # Dummy rendering function
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
           self.left_handler()

        elif event == 'right':
            pass

        elif event == 'quit':
            sys.exit()
        
        else:
            pass


    # Handler for up event
    def up_handler(self):

        if self is Lines:

            self = self.Lines.up_handler(self)

        elif self is Stations:

            self = self.Stations.up_handler(self)

        else:

            pass


    # Handler for down event
    def down_handler(self):

        if self is Lines:

            self = self.Lines.down_handler(self)

        elif self is Stations:

            self = self.Stations.down_handler(self)

        else:

            pass


    # Handler for left event
    def left_handler(self):

        if self is Station:

            self = self.Station.left_handler(self)

        elif self is Stations:

            self = self.Stations.left_handler(self)

        else:

            pass


    # Handler for right event
    def right_handler(self):

        if self is Lines:

            self = self.Lines.right_handler(self)

        elif self is Stations:

            self = self.Stations.right_handler(self)

        else:

            pass



    # Gets the current event for the event handler
    def get_current_event():

        '''

        if keyboard.is_pressed('w'):
            
            return 'up'
        
        elif keyboard.is_pressed('a'):

            return 'left'
             
        elif keyboard.is_pressed('s'):

            return 'down'

        elif keyboard.is_pressed('d'):

            return 'right'

        elif keyboard.is_pressed('q'):

            return 'quit'
        
        else:

            pass

        '''

        pass        


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


    # Event handler for up
    def up_handler(self):

        return self

    
    # Event handler for down
    def down_handler(self):

        return self


    # Event handler for left
    def left_handler(self):

        return came_from_stations


    # Event handler for right
    def right_handler(self):

        return self


# Class for choosing all the different stations of a line
class Stations(World):


    # Constructor method
    def __init__(self, stations, current_selected, came_from_lines):
        
        self.stations = stations
        self.current_selected = current_selected
        self.came_from_lines = came_from_lines

        self.blue_line = ['Wonderland',
                        'Revere Beach',
                        'Beachmont',
                        'Suffolk Downs',
                        'Orient Heights',
                        'Wood Island',
                        'Airport',
                        'Maverick',
                        'Aquarium',
                        'State Street',
                        'Government Center',
                        'Bowdoin']
        self.green_line = ['Lechmere',
                        'Science Park',
                        'North Station',
                        'Haymarket',
                        'Government Center',
                        'Park Street',
                        'Boyleston',
                        'Arlington',
                        'Copley',
                        'Hynes',
                        'Kenmore',
                        'E:Prudential',
                        'E:Symphony',
                        'E:Northeastern',
                        'E:MFA',
                        'E:Longwood Medical',
                        'E:Brigham Circle',
                        'E:Fenwood Road',
                        'E:Mission Park',
                        'E:Riverway',
                        'E:Back of the Hill',
                        'E:Heath Street',
                        'D:Fenway',
                        'D:Longwood',
                        'D:Brookline Village',
                        'D:Brookline Hills',
                        'D:Beaconsfield',
                        'D:Reservoir',
                        'D:Chestnut Hill',
                        'D:Newton Center',
                        'D:Newton Highlands',
                        'D:Eliot',
                        'D:Waban',
                        'D:Woodland',
                        'D:Riverside',
                        'C:St Marys Street',
                        'C:Hawese Street',
                        'C:Kent Street',
                        'C:St Paul Street',
                        'C:Coolidge Corner',
                        'C:Summit Ave',
                        'C:Brandon Hall',
                        'C:Fairbanks St',
                        'C:Washington Sq',
                        'C:Tappan Street',
                        'C:Dean Road',
                        'C:Englewood Ave',
                        'C:Cleveland Circ',
                        'B:Blandford St',
                        'B:Boston Uni E',
                        'B:Boston Uni Cent',
                        'B:Boston Uni W',
                        'B:St Paul Street',
                        'B:Pleasant Street',
                        'B:Babcock Street',
                        'B:Packards Corner',
                        'B:Harvard Ave',
                        'B:Griggs Street',
                        'B:Allston Street',
                        'B:Warren Street',
                        'B:Washington St',
                        'B:Sutherland Road',
                        'B:Chiswick Road',
                        'B:Chestnut Hill',
                        'B:South Street',
                        'B:Boston College']

        self.orange_line = ['Oak Grove',
                        'Malden Center',
                        'Wellington',
                        'Assembly',
                        'Sullivan Square',
                        'Community College',
                        'North Station',
                        'Haymarket',
                        'State Street',
                        'Downtown Crossing',
                        'Chinatown',
                        'Tufts Medical',
                        'Back Bay',
                        'Mass Ave',
                        'Ruggles',
                        'Roxbury Crossing',
                        'Jackson Square',
                        'Stony Brook',
                        'Green Street',
                        'Forest Hills']

        self.red_line = ['Alewife',
                        'Davis',
                        'Porter',
                        'Harvard',
                        'Central',
                        'Kendall/MIT',
                        'Charles/MGH',
                        'Park Street',
                        'Downtown Crossing',
                        'South Station',
                        'Broadway',
                        'Andrew',
                        'JFK/U Mass',
                        'A:Savin Hill',
                        'A:Fields Corner',
                        'A:Shawmut',
                        'A:Ashmont',
                        'B:North Quincy',
                        'B:Wollaston',
                        'B:Quincy Center',
                        'B:Quincy Adams',
                        'B:Braintree']


    
    # Event handler for up
    def up_handler(self):    

        current_index = self.stations.index(self.current_selected)

        if current_index == 0:

            return self 

        else:

            self.current_selected = self.stations(current_index - 1) 
            
            return self


    # Event handler for down
    def down_handler(self):

        current_index = self.stations.index(self.current_selected)

        if current_index == len(self.stations - 1):

            return self

        else:
            self.current_selected = self.stations(current_index + 1) 
            
            return self
    

    # Event handler for left
    def left_handler(self):

        return self.came_from_lines        


    # Event handler for right
    def right_handler(self):

        return self


# Class for choosing between the different lines
class Lines(World):
    
    # Constructor method
    def __init__(self, lines, current_selected):

        self.lines = lines
        self.current_selected = current_selected

    
    # Event handler for up
    def up_handler(self):    

        current_index = self.lines.index(self.current_selected)

        if current_index == 0:

            return self

        else:

            self.current_selected = self.lines(current_index - 1) 
            
            return self


    # Event handler for down
    def down_handler(self):

        current_index = self.lines.index(self.current_selected)

        if current_index == len(self.lines- 1):

            return self 

        else:
            self.current_selected = self.lines(current_index + 1) 
            
            return self
    

    # Event handler for left
    def left_handler(self):

        return self
     

    # Event handler for right
    def right_handler(self):

        return self


####################

###############
# MAIN METHOD #
###############

# main method weow!!
def main():
    
    # grabs my api key for MBTA API v3
    with open('api-key.txt', 'r') as file:

        api_key = file.read()
    

    # Initializing a "Big Bang" type structure
    running = True 
    
    # These are the lines weow!
    line_list = ['Blue Line',
            'Green Line',
            'Orange Line',
            'Red Line']

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

