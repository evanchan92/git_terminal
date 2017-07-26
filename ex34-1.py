
# coding: utf-8

# In[ ]:


from sys import exit

def first_choice():
    print (" Now you enter the shop, you see 2 kinds of food, Babaozhou and Shourouzhou, which one do you prefer?")
    bbbbb = raw_input("babaozhou or shourouzhou    >")
    if bbbbb == "babaozhou":
        print (" Good choice, man!")
        babaozhou()
        
    elif bbbbb == "shourouzhou":
        print (" Ehh, not bad, man.")
        shourouzhou()

    else:
        print ("U silly bastart, I ask u to choose from those 2, you just choose from it!")
        first_choice()
        
##############################################################

def start():
    print (" U passes through a small shop, there seems to be some discount.")
    print (" Do you want to buy something?")
    buy = raw_input (" Y/N   >")
    
    if buy == "Y":
        print ("Yeah, Good choice!")
        first_choice()
        
    elif buy == "N":
        print ("Ehh, you're doomed, you'll starve to die!!! You silly bastard.")
        exit(0)
    else:
        print ("Say something that human can understand! \n")
        start()
        
##############################################################

def babaozhou():
    print ("now you have got a bottle of Babaozhou, it's very precious.")
    print ("Be careful, you'd better keep it in your underpant!")
    
    bala = raw_input("Will u put the babaozhou in your underpant?     Y / N     >")
    if bala == "Y":
        print (" Aha, you shameless thief! I finally catch you! Let's go to the police station!")
        exit()
        
    elif bala == "N":
        print ( "Yes, you honest young man! Now you let's move.")
        second_choice()
        
    else:
        Print ("Hey, what are you thinking? Make the choice!")
        babaozhou()
        
##############################################################

def second_choice():
    print(" Now you coming to the central aisle.")
    print(" Where do you want to go? Left or Right?")
    
    aaaaa = raw_input(" L/ R    >")
    
    if aaaaa == "L":
        print ("Now you come to the sports area.")
        print ("What do you want? They have badminton/ football/ basketball. ")
        sport_choice()
        
    elif aaaaa == "R":
        print ("Now you come to the Electrical applicance area.")
        print ("Do you want to buy something?")
        appliance()
        
    else:
        print ("That's not what I ask u.")
        second_choice()
##############################################################
    
    
def shourouzhou():
    print ("Ohh, What a good choice!!! It's delicious!!!")
    print ("How much do you want?")
    porridge = raw_input("How many bowls do you want to take?     >")
    
    if porridge >= 3:
        print(" That's great, I'm totally full, let's go home.")
        gohome()
        
    elif  porridge < 3:
        print ("Let's go to the central aisle to buy something more.")
        second_choice()
    else:
        shourouzhou()

##############################################################

def sport_choice():     #badminton/ football/ basketball
    print("Now, we've arrived at the sport area, what do u want?")
    choose_sport = raw_input("Badminton/ football/ basketball?    >")
    if choose_sport == "Badminton":
        print ("Good!")
        gohome()
        
    elif choose_sport == "football":
        print ("Yeah")
        gohome()
        
    elif choose_sport == "basketball":
        print ("not bad")
        gohome()
        
    else:
        print ("Put it back, you silly boy!")
        sport_choice()
#############################################################        
    
    
##############################################################
 

def gohome() :
    print ("Do you want to take bus or taxi to go home?")
    
    transportation = raw_input("Taxi or Bus   >")
    if transportation =="taxi":
        print (" You silly bastard, you'll be bankrupted soon!!!")
        exit()
        
    elif transportation == "Bus":
        print(" Good boy!")
        exit()
        
    else:
        gohome()

##############################################################
    
start()

