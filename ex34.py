from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"
    
    next = raw_input(">  ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        
    if how_much <50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
        
        
def bear_room():
    print " There's a bear here."
    print " The bear has a bunch of honey."
    print " The fat bear is in front of another door."
    print " How are you going to move the bear?"
    bear_moved = False     # What dose this mean?
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then pimp slaps your face off.")
        elif next == "taunt bear" and not bear_moved:   # If I delete "not", the program cannot recognize the string of "Taunt bear"/ "Open door" ???
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True     #? No conflicting with line 24?   # If I skip this line, the program cannot recognize " Open door" in the next step.
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your crotch off.")   # So far, I cannot find the way to launch this branch.
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
            
def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:    # if "xxx" in xxx, does it means I can input everything in the raw_input
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()
        
        
def dead(why):
    print why, "Good job!"
    exit(0)
    
def start():
    print "You're in a dark room."
    print "There's a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()
