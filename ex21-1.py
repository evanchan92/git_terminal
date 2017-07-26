def multiply (a, b):
     print "%r * %r " % (a, b)
     return (a, b)
     
def minus (a, b):
    print " %r - %r " % (a, b)
    return (a, b)
    
def xxx(a, b):
    print " %r* 8 - %r/ 2 + 3" % (a,b )
    return (a, b)
    
a = raw_input( "What do u want A be ? ...   => ")
b = raw_input( "What do u want B be ? ...   => ")

merci = xxx( 18, minus (xxx(a, b) ,b))
print " Merci is ... " , merci

print xxx (a,b)
