name = 'Evan.CHEN'
age = 25 # yeah
height = 173 #cms
weight = 82 #kgs
eyes = 'black'
teeth = 'white'
hair = 'black'

print "Let's talk about %s." % name
print "He's %d feet tall." % (height/100* 3.2808)
print "He's %d pounds heavy." % (weight *2.20462)
print "Actually that's too heavy."
print "he's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)
