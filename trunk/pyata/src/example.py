
from box_classes.box import *
from box_classes.number import *
from box_classes.message import *
from box_classes.comment import *
from box_classes.symbol import *
from communication import *

#file created just for debug tests



if __name__ == '__main__':
    print "ei man"
   
   
   

def debug_symbol():  
    pd = Communication(False)
    pd.init_pd()
    
    s = Symbol(10, 10, 0)
    command = "obj " + str(s.x) + " " + str(s.y) + " sym ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = s.set("mesa")
    print command
    pd.send_pd(command)
    sleep(2)
    
    pd.finish_pd()

   
def debug_number():
    pd = Communication(False)
    pd.init_pd()
    
    n = Number(10, 10, 0)
    #command = "floatatom " + str(n.x) +  " " + str(n.y) + " 5 0 0 0 - - pyata ;"
    command = "obj " + str(n.x) + " " + str(n.y) + " " + "nmb ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = n.increment()
    print command
    pd.send_pd(command)
    sleep(2)
    
    print n.get_value()
    
    
    command = n.increment()
    print command
    pd.send_pd(command)
    sleep(2)
    
    print n.get_value()
    
    command = n.decrement()
    print command
    pd.send_pd(command)
    sleep(2)
    
    print n.get_value()
    
    command = n.set(20)
    print command
    pd.send_pd(command)
    sleep(2)
    
    print n.get_value()
    
    pd.finish_pd()   

    
    
    
def debug_comment():   
    pd = Communication(False)
    pd.init_pd()
    
    m = Message(10, 10, "alo", 0)
    command = "text " + str(m.x)  + " " + str(m.y) + " " + m.text + " ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = "editmode 1 ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = m.edit("mimimi")
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = "editmode 0 ;"
    print command
    pd.send_pd(command)
    sleep(2)
    

    pd.finish_pd()
    
    
    
def debug_message():
    pd = Communication(False)
    pd.init_pd()
    
    m = Message(10, 10, "alo", 0)
    command = "msg " + str(m.x)  + " " + str(m.y) + " " + m.text + " ; "
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = m.click()
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = "editmode 1 ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = m.edit("mimimi")
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = "editmode 0 ;"
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = m.click()
    print command
    pd.send_pd(command)
    sleep(2)

    pd.finish_pd()
    
    
  
  
    
def debug_object():
    pd = Communication(False)
    pd.init_pd()
    command = "editmode 1;"
    pd.send_pd(command);
    
    obj1 = Object(10, 10, "dac~", 0)
    command = "obj " + str(obj1.x) + " " + str(obj1.y) + " " + obj1.label + ";"
    print command
    pd.send_pd(command)
    sleep(2)
    
    #obj2 = Object(20, 20, "dac~", 0)
    #command = "obj " + str(obj2.x) + " " + str(obj2.x) + " " + obj2.label + ";"
    #print command
    #pd.send_pd(command)
    #sleep(2)
    
    command = obj1.move(100, 100)
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = obj1.unselect()
    print command
    pd.send_pd(command)
    sleep(2)

    #command = obj2.select()
    #print command
    #pd.send_pd(command)
    #sleep(2)
    
    command = obj1.edit("osc~")
    print command
    pd.send_pd(command)
    sleep(5)
    
    pd.finish_pd()