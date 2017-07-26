# testing
filename = raw_input('''We're going to edit a file via this program, first, we need to type in the name of the file ...
''')


print "We're going to erase %r." % filename
print "if you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open (filename,'w')

print "Truncating the file, goodbye!"
target. truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target. write (line1)
target. write ("\n")
target. write (line2)
target. write ("\n")
target. write (line3)

target. close
