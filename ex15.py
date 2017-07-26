# Import argv from the sys function
from sys import argv
# giving argv the range
script, filename = argv
# first to open the sample txt file.
txt = open(filename)
# to guide the user to input filename
print "Here's your file %r:" % filename
# after opening the txt, we need to read it out.
print txt.read()
# stimulate user to input again
print "I'll also ask you to type it agian:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt. close()
txt_again. close()
