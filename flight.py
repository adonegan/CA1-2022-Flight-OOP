# to time the menu display
import time

class Flight():

    # class variables
    __flightCode = 0
    __pilotName = ""
    __destination = ""
    __category = ""
    __possibleCategories = ["Commercial", "Freight"]
    __capacity = False
    __rating = ""
    __possibleRatings = [0,1,2,3,4,5]

    # for counter class method
    count_inst = 0

    # to initialise instances
    def __init__(self,flightCode=0,pilotName="",destination="",category="",capacity=False,rating=0):
        try:
            self.setFlightCode(flightCode)
            self.setPilotName(pilotName)
            self.setDestination(destination)
            self.setCategory(category)
            self.setCapacity(capacity)
            self.setRating(rating)
        except Exception as e:
            raise Exception("The object has not been created.")
        Flight.count_inst += 1

    # to count how many instances the class produces
    @classmethod
    def count_instances(cls):
        return cls.count_inst
    
    # getters
    # methods to return private instance variables
    def getFlightCode(self):
        return self.__flightCode

    def getPilotName(self):
        return self.__pilotName

    def getDestination(self):
        return self.__destination

    def getCategory(self):
        return self.__category

    def getCapacity(self):
        return self.__capacity

    def getRating(self):
        return self.__rating

    # setters
    # methods to set / update private variables
    # for use with exception handling
    def setFlightCode(self,flightCode):
        self.__flightCode = flightCode

    def setPilotName(self,pilotName):
        self.__pilotName = pilotName

    def setDestination(self,destination):
        self.__destination = destination

    def setCategory(self,category):
        if category not in self.__possibleCategories:
            raise Exception("{0} is not a valid category. Commercial or Freight only.".format(category))
        else:
            self.__category = category

    def setCapacity(self,capacity):
        if capacity == True:
            self.__capacity = capacity
        elif capacity == False:
            self.__capacity = capacity
        else:
            raise Exception("{0} is not a valid capacity status. True or False only.".format(capacity))
        
    def setRating(self,rating):
        if rating not in self.__possibleRatings:
            raise Exception("{0} is not a valid rating. 0-5 only.".format(rating))
        else:
            self.__rating = rating

    def flightAtCapacity(self):
        self.__capacity = True

    # method to print details
    def print_flight_details(self):
        print("-"*45)
        print("\t\tFlight Details")
        print("-"*45)
        print("Flight code:\t\t\t", self.__flightCode)
        print("Pilot's name:\t\t\t", self.__pilotName)
        print("Destination:\t\t\t", self.__destination)
        print("Flight category:\t\t", self.__category)
        print("Flight's capacity status:\t", self.__capacity)
        print("Comfort rating:\t\t\t", self.__rating)


# main program
menuOption = 0
flightList = []

while menuOption >= 0 and menuOption < 5:

    # display main menu
    print()
    print(" -------------------------- ")
    print("|           Menu           |")
    print("|--------------------------|")
    print("|  1) Create Flight        |")
    print("|  2) Set Flight Capacity  |")
    print("|  3) View Flight Details  |")
    print("|  4) Summary of Ratings   |")
    print("|  5) Exit                 |")
    print(" -------------------------- ")

    # take user input
    menuOption = int(input("\nPlease enter menu option: "))

    if menuOption == 1:
        # store user input in variables
        flight_code = int(input("Enter flight code: "))
        destination = input("Enter destination: ")
        pilot_name = input("Enter pilot name: ")
        flight_category = input("Commercial or Freight category? ")
        comfort_rating = int(input("Enter comfort rating: "))

        # check for pre-existing object based on flight code
        for item in flightList:
            # if item's code is equal to user code input
            if item.getFlightCode() == flight_code:
                # output message and break out of program
                print("\n-> Flight code already exists. Entry cancelled.\n")
                break
        else:
            # otherwise, append flight object to list of objects
            flightList.append(Flight(flightCode=flight_code,destination=destination,pilotName=pilot_name,category=flight_category,capacity=False,rating=comfort_rating))
            print()

            # display items in flightList
            for item in flightList:
                item.print_flight_details()
                print()
        # wait 3 seconds before showing main menu
        time.sleep(3)


    elif menuOption == 2:
        
        # ask user for input
        code = int(input("Enter flight code: "))

        # check all flight objects to see if user code matches flight code
        for item in flightList:
            if item.getFlightCode() == code: 
                if item.getCapacity() == False:
                    # use method to set new capacity boolean value
                    item.flightAtCapacity()
                    print("-> Capacity status updated.\n-> Flight {0} is now at capacity.".format(item.getFlightCode()))
                    break
                elif item.getCapacity == True:
                    print("-> Flight {0} already at capacity.\n-> No status to update.".format(item.getFlightCode()))
                    break
        else:
            # if there's no object that matches user's input code, output message
            print("-> Flight code does not exist.")
        
        print()
        # wait 3 seconds before showing main menu
        time.sleep(3)
     
    elif menuOption == 3:

        # set flight capacity counters
        flights_not_at_capacity = 0
        flights_at_capacity = 0

        # loop through all flight objects
        for item in flightList:
            if item.getCapacity() == False:
                # increment not-at-capacity by 1 if flight's capacity is false
                flights_not_at_capacity += 1
            else:
                # otherwise increment at-capacity
                flights_at_capacity += 1

        # output results
        print("-"*30)
        print("\tCapacity Stats")
        print("-"*30)
        print("Flights not at capacity: ", flights_not_at_capacity)
        print("Flights at capacity: ", flights_at_capacity)
        print()

        time.sleep(2)
        # display items in flightList
        for item in flightList:
            item.print_flight_details()
            print()

        # wait 3 seconds before showing main menu
        time.sleep(3)

    elif menuOption == 4:

        # set category and rating counter variables
        commercial_flights = 0
        freight_flights = 0
        comfort_rating_commercial = 0
        comfort_rating_freight = 0

        # loop through all flight objects
        for item in flightList:
            # if category is Commercial, increment variable by 1
            if item.getCategory() == "Commercial":
                commercial_flights += 1
            # if category is Freight, increment variable by 1
            elif item.getCategory() == "Freight":
                freight_flights += 1

        # loop through again to update sum up all ratings per category
        # get average by dividing by number of flights per category
        for item in flightList:
            if item.getCategory() == "Commercial":
                comfort_rating_commercial += item.getRating()
                comfort_rating_commercial = comfort_rating_commercial / commercial_flights
            elif item.getCategory() == "Freight":
                comfort_rating_freight += item.getRating()
                comfort_rating_freight = comfort_rating_freight / freight_flights

        # output results
        print("-"*35)
        print("Category and Comfort Rating Stats")
        print("-"*35)
        print("Commercial flights: ", commercial_flights)
        print("Average comfort rating: ", round(comfort_rating_commercial,2))   
        print("Freight flights: ", freight_flights)
        print("Average comfort rating: ",round(comfort_rating_freight,2))
        print()

        # wait 3 seconds before showing main menu
        time.sleep(3)

    elif menuOption == 5:
        # if user selects 5, exit program
        print("-> Exiting...")
        break
    else:
        # if user inputs any number except 1-5, break out of the loop with output message
        print("Not a valid option. Main menu accepts 1-5.")
        break

# When exiting, print how many instances were created.
if Flight.count_instances() <= 1:
    print("->",Flight.count_instances(), "instance created")
else:
    print("->", Flight.count_instances(), "instances created")