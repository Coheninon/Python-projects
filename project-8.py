''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################

class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0.0
        
    def __repr__(self):
        snacks_lst = []
        drinks_lst = []
        for key in self.snacks:
            snacks_lst.append(key)
        for key2 in self.drinks:
            drinks_lst.append(key2)
            
        return "The minibar contains the drinks:"+' '+ str(drinks_lst) +"\nAnd the snacks:"+' '+ str(snacks_lst) +"\nThe bill for the minibar is:"+' '+ str(self.bill)

    def eat_a_snack(self, snack):

        if snack in self.snacks:
            self.bill += self.snacks.pop(snack)
        else:
            raise ValueError ("The snack is not in the minibar")
        
    def drink_a_drink(self, drink):
        
        if drink in self.drinks:
            self.bill += self.drinks.pop(drink)
        else:
            raise ValueError ("The drink is not in the minibar")
        
#########################################
# Question 2 - do not delete this comment
#########################################

class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        
        if type(clean_level) != int:
            raise TypeError ("Invalid Clean level")
        if type(rank) != int:
            raise TypeError ("Invalid rank")
        if type(satisfaction) != int and type(satisfaction) != float:
            raise TypeError ("Invalid satisfaction")

        if clean_level > 10 or clean_level < 1:   
            raise ValueError ("Clean level not in range")
        if rank > 3 or rank < 1:
            raise ValueError ("rank not in range")
        if satisfaction > 5 or satisfaction < 1:
            raise ValueError ("satisfaction not in range")
        
        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = guests
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = 1.0

    def __repr__(self):
        floor_num = int(self.floor)
        num = int(self.number)
        if len(self.guests) == 0:
            guests_lst = "empty"
        else:
            guests_lst = ""
            for name in self.guests:
                guests_lst += name.lower() + ", "
            guests_lst = guests_lst.rstrip(' ,')
        clean_level_num = int(self.clean_level)
        rank_num = int(self.rank)
        satisfaction_num = float(round(self.satisfaction))

        return str(self.minibar)+"\nfloor: "+str(floor_num)+"\nnumber: "+str(num)+"\nguests:"+' '+ str(guests_lst) +"\nclean_level: "+str(clean_level_num)+"\nrank: "+str(rank_num)+"\nsatisfaction: "+str(satisfaction_num)               
        
    def is_occupied(self):
        if len(self.guests) == 0:
            return False
        else:
            return True

    def clean(self):
        self.clean_level = min(10,self.clean_level + self.rank) 

    def better_than(self, other):   
        if type(other) != Room:
            raise TypeError ("Other must be an instance of Room")
        elif (self.rank,self.floor,self.clean_level) > (other.rank,other.floor,other.clean_level):
            return True
        else:
            return False

    def check_in(self, guests):
        if self.is_occupied() == True:
            raise RoomError ("Cannot check-in new guests to an occupied room")
        else:
            guests_names = []
            for name in guests:
                guests_names.append(name.lower())
            self.guests = guests_names 
            self.satisfaction = 1.0
            
    def check_out(self):
        if self.is_occupied() == False:
            raise RoomError ("Cannot check-out an empty room")
        else:
            self.guests = []
    
    def move_to(self, other):
        if self.is_occupied() == False:
            raise RoomError ("Cannot move guests from an empty room")
        if other.is_occupied() == True:
            raise RoomError ("Cannot move guests into an occupied room")
        else:
            other.guests = self.guests
            
            if self.better_than(other) == False:
                other.satisfaction = min(5.0, self.satisfaction + 1.0)
            else:
                other.satisfaction = self.satisfaction 
            self.guests = []
       
#########################################
# Question 3 - do not delete this comment
#########################################

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
            
    def __repr__(self):
        num_of_rooms = len(self.rooms)
        occupied_rooms = 0
        for elem in self.rooms:
            if elem.is_occupied() == True:
                occupied_rooms += 1
        return str(self.name) + " hotel has:" + "\n" + str(num_of_rooms) + " rooms" + "\n" + str(occupied_rooms) + " occupied rooms"
                      
    def check_in(self, guests, rank):        
        for elem in self.rooms:
            if elem.rank == rank:
                try:  
                    elem.check_in(guests)
                    return elem   
                except RoomError:
                    pass
                
    def check_out(self, guest):  
        for elem in self.rooms:
            if guest in elem.guests:
                try:
                    elem.check_out()
                    return elem  
                except RoomError:
                    pass

    def upgrade(self, guest):       
        for val in self.rooms:
            if guest in val.guests:
                room1 = val
                break
        for elem in self.rooms:
            try:
                if elem.is_occupied() == False and elem.better_than(room1) == True:
                    room1.move_to(elem)
                    return elem            
            except RoomError:
                pass
    
#########################################
# Question 3 supplement - do not delete this comment
#########################################

def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print(m)
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel() ## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the 
    
