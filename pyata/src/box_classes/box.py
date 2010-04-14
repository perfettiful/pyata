
##########################################################
##########################################################
# description: abstract class that represents any Pd box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################



#box class itself
class Box:
    #class variables (not instance variables
    #memory = [] #stores all objetcs that are inserted to pd
    canvas = "pd-new " #stores the name of the canvas
    snd = "" #used to communicate to pd

    #constructor of the class
    def __init__(self, x, y, id):
        self.x=x
        self.y=y
        self.id=id
        self.inlet= self.get_number_inlets()
        self.outlet=self.get_number_outlets()
        self.create()
        #Box.memory.append(self) 
    
    #method that sets the canvas
    @staticmethod
    def set_canvas(nc):
        Box.canvas = nc
        
    #method that sets the sender
    @staticmethod
    def set_sender(s):
        Box.snd = s
    
    #clicks inside this obj
    def click(self):
        #command  = []
        command  = Box.canvas + "mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        command += Box.canvas + "mouseup " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        Box.snd.send_pd(command)
        
    # method that moves this box   
    def move (self, new_x, new_y):
        command  = Box.canvas + "mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        command += Box.canvas + "motion " + str(new_x) + " " + str(new_y) + " 0 ; "
        command += Box.canvas + "mouseup " + str(new_x) + " " + str(new_y) + " 1 0 ; "
        self.x=new_x
        self.y=new_y
        print (command )
        Box.snd.send_pd(command)
    
    #method that selects this box
    def select (self):
        command  = Box.canvas + "mouse " + str(self.x-2) + " " + str(self.y-2) + " 1 0 ; "
        command += Box.canvas + "motion " + str(self.x+1) + " " + str(self.y+1) + " 0 ; "
        command += Box.canvas + "mouseup " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        Box.snd.send_pd(command)
    
    #method that unselects this box
    def unselect(self):
        command  = Box.canvas + "mouse " + str(self.x-2) + " " + str(self.y-2) + " 1 0 ; "
        command += Box.canvas + "mouseup " + str(self.x-2) + " " + str(self.y-2) + " 1 0 ; "
        Box.snd.send_pd(command)
    
    def create(self):
        print "all subclass must implement this"
    
    def delete(self):
        self.select()
        command = Box.canvas + "cut ; "
        Box.snd.send_pd(command)
    
    #deprecated!
    #method that selects this box with key shift pressed
    def shift_select (self):
        Box.snd.send_pd( Box.canvas + "key 1 Shift_R 0 ; " )
        self.select()
        Box.snd.send_pd( Box.canvas + "key 0 Shift_R 0 ; " )
        
    #deprecated!
    #method that unselects this box with key shift pressed
    def shift_unselect(self):
        Box.snd.send_pd( Box.canvas + "key 1 Shift_R 0 ; " )
        self.click()
        Box.snd.send_pd( Box.canvas + "key 0 Shift_R 0 ; " )
        
    
    # @TODO gets the number of inlet of the object
    def get_number_inlets (self):
        return 0
    
    # @TODO gets the number of inlet of the object
    def get_number_outlets (self):
        return 0
        
    #aux static function to debug this class
    @staticmethod
    def debug():
        box = Box(20, 20, 0)
        print box.move(10, 10)
        print box.select()
        print box.unselect()
        print box.shift_select()
        print box.shift_unselect()
    


