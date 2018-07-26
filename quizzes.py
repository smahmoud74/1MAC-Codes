# This is a Python comment. Lines that begin with a '#' are ignored by the
# Python interpreter. Comments are useful for documenting code or explaining
# quiz questions!
# 
# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result
#
# Click the "Test Run" button below to try running your code and see the output,
# and click "Submit" to submit your answer.
#print 7 * 7 * 24 * 60


# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second
#print 299792458 * 100 * (1.0/1000000000)


# What do you think the programmer who wrote the following code WANTED it to do?
#
# Do you think this code will work? Why or why not?

#print 1
#print 2
#print 3
#print 4
#print 5
#print 6
#print 7
#print 8
#print 9

# Once you have a guess, press the "Test Run" button below.
#
# Tip: Read the LAST line of the error message first.



# What do you think the programmer who wrote the following code WANTED it to do?
#
# Do you think this code will work? Why or why not?

#print 1
#print  2
#print   3
#print     4
#print        5
#print              6
#print                       7
#print                                     8
#print                                                          9

# Once you have a guess, press the "Test Run" button below.


# What do you think the programmer who wrote the following code WANTED it to do?
#
# Do you think this code will work? Why or why not?

#print 1
#print 2
#print 3
#print 4
#print 5
#print 6
#print 7
#print 8
#print 9

# Once you have a guess, press the "Test Run" button below.
#
# Tip: Read the LAST line of the error message first.


# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

#speed_of_light = 299792458.0 
#cycles_per_second = 2700000000.0
#print speed_of_light / cycles_per_second


# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.
#age = 44
#print age * 365


# Define a variable, name, and assign to it a string that is your name.
#name = "Sinan"
#print "Hello " + name + '!' * 3


# This code shows some basic variable assignment and string printing. 
#name = "Andy"
#print "Hello " + name
#print name * 4

# This code shows the difference between the string "4" and the number 4.
# Remove the four comment characters (#) on the lines below to see what happens.
#print 4
#print "4"
#print 4 + 4
#print "4" + "4"

# This code shows some of the different mistakes that are easy to make while 
# working with strings. Remove one comment at a time and press Test Run to 
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.
#print 'hello'
#print 'hello'
#print "hello"

# This code will give you a peek at what you are about to learn! Uncomment 
# all of the lines below to get a glimpse of "string indexing"
#name = "Andy"
#print name[0]
#print name[1]
#print name[2]
#print name[3]


# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

#s = 'audacity'
#capital = 'U'
#print capital + s[2:8]


# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

#print "Example 1: Finding substrings in a string"
#print "test".find("te")
#print "test".find("st")
#print "test"[2:]

#print "Example 2: Finding substrings in a string which is stored as a variable"
#my_string = "test"
#print my_string.find("te")
#print my_string.find("st")

#print my_string[2:]

#print "Example 3: Printing out everything after a certain substring"
#my_string = "My favorite color: blue"
#color_start_location = my_string.find("color:")
#favorite_color = my_string[color_start_location:]
#print favorite_color # oops, this line prints out 'color: ' as well...
#print favorite_color[7:] # this fixes it!

#print "Example 4: Other interesting things about string.find()..."
#print "text".find("text") # prints 0
#print "text".find("Text") # prints -1
#print "text".find("")     # prints 0
#print "text".find(" ")    # prints -1 


# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

#print "Example 1: using find to print the second occurrence of a sub-string"
#print "test".find("t")
#print "test".find("t", 1)

#print "Example 2: using a variable to store first location"
#first_location = "test".find("t") # here we store the first location of "t"
#print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

#print "Example 3: using find to get rid of exclamation marks!!"
#example = "Wow! Python is great! Don't you think?"
#first = example.find('!')
#second = example.find('!', first + 1)
#new_string = example[:first] + example[first+1:second] + example[second+1:]
#print new_string # oops, I should probably replace the !s with periods
#new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
#print new_string 


# Write Python code that prints out the number of hours in 7 weeks.
#print 7 * 7 * 24


# Given the variables s and t defined as:
#s = 'udacity'
#t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
#print s[0] + t[2:]


# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].

#sentence = "A NOUN went on a walk."
#substring = sentence[6:]
#print sentence[6:]


# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

#sentence = "A NOUN went on a walk. It can VERB really fast."
#substring1 = sentence[0:2]
#substring2 = sentence[6:30]
#substring3 = sentence[34:]
#print substring1
#print substring2
#print substring3


# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

#sentence = "A NOUN went on a walk. It can VERB really fast."
#substring1 = sentence[0:2]
#substring2 = sentence[6:30]
#substring3 = sentence[34:]

#noun_replacement = "dog" # your noun here
#verb_replacement = "be" # your verb here
#new_sentence = ''
#new_sentence += substring1
#new_sentence += noun_replacement
#new_sentence += substring2
#new_sentence += verb_replacement
#new_sentence += substring3
#print new_sentence

# your code here


# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

#mary = "Mary"
# Your code goes here
#randa = mary
#katie = randa
#salwa = katie
#kathleen = salwa
#gabriel = kathleen


# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
#gabriel = kathleen

# Test to see if all of these variables will print out the string "Mary"
#print gabriel
#print kathleen
#print salwa
#print katie
#print randa
#print mary


# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find, or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

#text = """Wow this is a fairly long body of text. Quite a few characters too.
#I wonder if the string.find method could help find where NOUN is located.
#That way, I could go out and VERB with my friends rather than counting characters
#all day long!"""
#print text.find("NOUN")
#print text.find("VERB")
#noun_position = 125
#verb_position = 171


# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

#text = "all zip files are zipped" 

# ENTER CODE BELOW HERE

#first_zip = text.find('zip')
#print text.find('zip', first_zip + 1)

#Anothe way to do it without introducing a viarble

#print text.find('zip', text.find('zip') + 1)

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function


# Read through the code below. Even if you don't understand it, try to make 
# a guess about what it does. What do you think will happen when you press 
# "Test Run"? Once you have a prediction, press "Test Run" and compare what 
# happens to what you predicted.

#def say_hello():
#    return "Hello!"

#print say_hello()

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing. 

# Continue to the next example to see a more interesting version of say_hello.


# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time. 
#
# Read through the code and try to predict what the output will be when 
# you press "Test Run"

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

#print say_hello("Miriam")
#print say_hello("Andy")


def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

#print add_two_numbers(4, 3)
#print add_two_numbers(2, 6)
#print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the 
# code below and then make ONE modification so that the function does 
# what the name says it should do.

def subtract_two_numbers(number_1, number_2):
    return number_1 + number_2

#print subtract_two_numbers(4, 3)


# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c




# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.
def square(a):
    c = a * a
    return c
#print square(5)
#>>> 25

#or we can do evrything with one statement

def square(a):
    return a * a
#print square(5)

#we can use a variable

#def square(a):
    #return a * a
#x = 37
#print square(x)

#or

#print square(square(x))


# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

#def sum(a,b):
    return a + b




#def sum3(a,b,c):
    return a + b + c

#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216


# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.



#def abbaize(s_1 , s_2):
    name = s_1 + s_2 + s_2 + s_1
    return name
#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'


# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter
#def udacify(s):
    return 'U'  + s
#print udacify('dacians')

# the output should be the string 'Udacians'







# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat


#print "Example 1: Greater-than and less-than comparisons"
#print 2 > 1
#print 1 > 2
#print 5 < 20
#print 100 < 19


#print "Example 2: Equality and non-equality comparisons"
#print 5 == 5
#print "hello" == "hello"
#print 5 == 10
#print 5 == '5' # what do you think will happen here?
#print 7 != 10
#print 7 != 7


#print "Example 3: A demo of what you are about to learn"
#if 3 < 5:
    #print "Three is definitely smaller than 5!"

#if 10 > 20: 
    #print "Did you know that 10 is greater than 20!?"
#else:
    #print "20 is greater than 10"


#def absolute(g):
	#if g < 0:
		#g = -g
	#return g #this will be executed whether the test is true or false
#print absolute(-3)


# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.
#def bigger(a,b):
    #if a > b:
        #return a
    #else:
        #return b
        
#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3

#or

#def bigger(a,b):
	#if a > b:
		#return a
	#return b
#print bigger(3,2)

#or

#def bigger(a,b):
	#if a > b:
		#r = a #assign to the variable "r" the result "a"
	#else:
		#r = b
	#return r
#print bigger(2,3)


# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'



#def is_friend(name):
    #if name[0] == 'D':
        #return True
    #else:
        #return False
#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False

#or

#def is_friend(name):
	#return name[0] == 'D'
#print is_friend('Dian')
#print is_friend('Fred')


# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

#def is_friend(name):
    #if name[0] == "D" or name[0] == "N": #or just: "D" or "N"
        #return True
    #else:
        #return False
        

#print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

#print is_friend('Moe')
#>>> False


#or

#def is_friend(name):
	#if name[0] == "D":
		#return True
	#if name[0] == "N":
		#return True
	#return False

#or

#def is_friend(name):
	#if name[0] == "D":
		#return True
	#else:
	    #if name[0] == "N":
		    #return True
		#else:
	         #return False


# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#def biggest(a,b,c):
    #return max([a,b,c])
    
#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9

#def biggest(a,b,c):
	#if b > c:
		#r = b
	#if b < c:
		#r = c
	#return r 
	#if a > r:
		#return a 
	#else:
		#return r
#print biggest(8, 9, 3)


#or

#def biggest(a,b,c):
    #if a > b:
        #if a > c:
            #return a
        #else:
            #return c
    #else:
        #if b > c:
            #return b
        #else:
            #return c

#or

#def bigger(a,b):
	#if a > b:
		#return a
	#else:
		#return b

#def biggest(a,b,c):
	#return bigger (bigger(a,b), c)
#print biggest(4,8,2)


#while loops

#i = 0
#while i != 10:
	#print i
	#i += 1

#i = 1
#while i != 10:
	#print i
	#i += 2


# This code demonstrates a while loop with a "counting variable"
#i = 0
#while i < 10:
    #print i
    #i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
#def remove_spaces(text):
    #text_without_spaces = '' #empty string for now
    #while text != '':
        #next_character = text[0]
        #if next_character != ' ':    #that's a single space
            #text_without_spaces = text_without_spaces + next_character
        #text = text[1:]
    #return text_without_spaces
#print remove_spaces("hello my name is andy how are you?")


# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

#def print_numbers(s):
    #n = 1
    #while n <= s:
        #print n
        #n += 1

#print print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

#or

#def print_numbers(n):
	#i = 0
	#while 1 < n:
		#i += 1
		#print i #we moved it here to get the correct number 
#print print_numbers(3)


#deep debugging


# A small change will fix the crashing bug in printInches.

#def printExample(a, b):
    #print a + b
    
#def printInches(n):
    #print str(n) + " inches"

# Don't change the function calls on lines 10 - 12.
#printExample(17, 23)
#printExample('long', 'word')
#printInches(42)


# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

#def bracket(text):
#    return '[' + text + ']'

#def boldwrap(text):
#    return '<b>' + text + '</b>'

#print boldwrap('This is an important message.')


# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

#def remove(somestring, sub):
    """Return somestring with sub removed."""
#    location = somestring.find(sub)
#    if location == -1:
#        return somestring
#    length = len(sub)
#    part_before = somestring[:location]
#    part_after = somestring[location + length:]
#    return part_before + part_after

# 
# Don't change these test cases!
#print remove('audacity', 'a')
#print remove('pythonic', 'ic')
#print remove('substring institution', 'string in')
#print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
#print remove('doomy', 'dooming')  # and this should print "doomy"



# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

#def weekend(day):
#    if day[0] == 'S':
#        return True
#    else:
#        return False
            
    # your code here
    
#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False


# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

#def countdown(n):
#    while n > 0:
#        print n
#        n = n - 1
#    print 'Blastoff!'
    
#countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


#Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#def bigger(a,b):
#    if a > b:
#        return a
#    else:
#        return b

#def biggest(a,b,c):
#    return bigger(a,bigger(b,c))

#def median(a,b,c):
#    big=biggest(a,b,c)
#    if big==a:
#        return bigger(b,c)
#    if big==b:
#        return bigger(a,c)
#    else:
#        return bigger(a,b)
            


#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7


# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

#from random import randint

#def random_noun():
    # your code here
#    random_num = randint(0,1)
#    if random_num == 0:
#        return 'sofa'
#    else:
#        return 'llama'

#print random_noun() #note no colon when call it

# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

#from random import randint

#def random_verb():
#    # your code here
#    random_num = randint(0,1)
#    if random_num == 0:
#        return 'run'
#    else:
#        return 'kayak'
#print random_verb() #note no colon when call it


# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

#from random import randint

#def random_verb():
#    random_num = randint(0, 1)
#    if random_num == 0:
#        return "run"
#    else:
#        return "kayak"
        
#def random_noun():
#    random_num = randint(0,1)
#    if random_num == 0:
#        return "sofa"
#    else:
#        return "llama"

#def word_transformer(word):
    # your code here
#    if word == 'NOUN':
#        return random_noun()
#    if word == 'VERB':
#        return random_verb()
#    else:
#        return word[0]
#print word_transformer('NOUN')
#print word_transformer('VERB')
#print word_transformer('SINAN')


# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

#from random import randint

#def random_verb():
#    random_num = randint(0, 1)
#    if random_num == 0:
#        return "run"
#    else:
#        return "kayak"
        
#def random_noun():
#    random_num = randint(0,1)
#    if random_num == 0:
#        return "sofa"
#    else:
#        return "llama"

#def word_transformer(word):
#    if word == "NOUN":
#        return random_noun()
#    elif word == "VERB":
#        return random_verb()
#    else:
#        return word[0]
        
#def process_madlib(mad_lib):
#    processed = ""
#    i=0
#    b=4
#    while i < len(mad_lib):
#        f = mad_lib[i:i+b]
#        a = word_transformer(f)
#        processed += a
#        if len(a) == 1:
#            i += 1
#        else:
#            i += 4
#    return processed
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
#test_string_1 = "This is a good NOUN to use when you VERB your food"
#test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
#print process_madlib(test_string_1)
#print process_madlib(test_string_2)


# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

#print "EXAMPLE 1: Lists can contain strings"
#string_list = ['HTML', 'CSS', 'Python']
#print string_list

#print "EXAMPLE 2: Lists can contain numbers"
#number_list = [3.14159, 2.71828, 1.61803]
#print number_list

#print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
#pi = number_list[0]
#not_pi = number_list[1:]
#print pi
#print not_pi


# Given the variable,

#days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

#def how_many_days(month_number):
#    return days_in_month[month_number - 1]

#print how_many_days(1)
#>>> 31

#print how_many_days(9)
#>>> 30
#print "EXAMPLE 4: Lists can contain strings AND numbers"
#mixed_list = ['Hello!', 42, "Goodbye!"]
#print mixed_list

#print "Example 5: Lists can even contain other lists"
#list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
#print list_with_lists


# Every entry in the following list is itself a list
#nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
#               ['CSS' , 'Cascading Style Sheets give pages style'],
#               ['Python', 'Python is a programming language'],
#               ['Lists', 'Lists are a data structure that let you organize information']]

#first_concept = nested_list[0]

#print "What do you think this will print?"
#print first_concept 

#print "Since first_concept was itself a list, we can access its elements"
#first_title = first_concept[0]
#first_description = first_concept[1]


#print "What will this print?"
#print first_title
#print first_description


# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
#countries = [['China','Beijing',1350],
#             ['India','Delhi',1210],
#             ['Romania','Bucharest',21],
#             ['United States','Washington',307]]
#print countries[1][1]

# Write code to print out the capital of India
# by accessing the list


# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
#countries = [['China','Beijing',1350],
#             ['India','Delhi',1210],
#             ['Romania','Bucharest',21],
#             ['United States','Washington',307]]
#china_population = countries[0][2]
#romania_population = countries[2][2]

#print china_population / romania_population

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.


# We defined:

#stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

#['Moe','Larry','Shemp']

# but does not create a new List
# object.

#stooges[2] = 'Shemp'
#print stooges


# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

#spy = [0,0,7]


#def replace_spy(p):
#    p[2] = p[2] + 1



# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.
#replace_spy(spy)
#print spy
#>>> [0,0,8]


# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

#print "EXAMPLE 1: We can use for loops to go through a list of strings"
#example_list_1 = ['a', 'b', 'c', 'd']
#for thing in example_list_1:
#    print thing
    

#print "EXAMPLE 2: We can use for loops on nested lists too!"
#example_list_2 = [['China', 'Beijing'],
#                  ['USA'  , 'Washington D.C.'],
#                  ['India', 'Delhi']]
#for country_with_capital in example_list_2:
#    country = country_with_capital[0]
#    capital = country_with_capital[1]
#    print capital + ' is the capital of ' + country


# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

#def sum_list(list):
#    sum = 0
#    for element in list:
#        sum += element
#    return sum



#print sum_list([1, 7, 4])
#>>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134

#or

#def sum_list(p):
#	result = 0
#	for e in p:
#		result = result + e
#	return result 
#print sum_list([1,2,3])


# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

#def measure_udacity(s):
#    count = 0
#    for e in s:
#        if e[0] == 'U':
#            count += 1
#    return count


#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2


# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.



#def find_element(li,el):
#    for i in range(0,len(li)):
#        if li[i] == el:
#            return i
#    return -1

#def find_element(li,el):
#    if el in li:
#        return li.index(el)
#    return -1
    
#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1

#or
#def find_element(p,t):
#    i = 0
#    for e in p:
#        if e == t:
#            return i
#        i = i + 1
#    return -1

#or

#def find_element(p,t):
#    i = 0
#    while i < len(p):
#        if p[i] == t:
#            return i
#        i = i + 1
#    return -1


#applyin index method

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

#def find_element(p,t):
#	for e in p:
#		if e == t:
#			return p.index(e)
#	else:
#		return -1


# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

#daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

#def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
#    return days


###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

#def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
#    if day < 30:
#        return year, month, day + 1
#    else:
#        if month < 12:
#            return year, month + 1, 1
#        else:
#            return year + 1, 1, 1

#print nextDay(1999, 12, 30)
#print nextDay(2013, 1, 30)
#print nextDay(2012, 12, 30)
#print nextDay(2012, 1, 1)


# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

#def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
#    if day < 30:
#        return year, month, day + 1
#    else:
#        if month == 12:
#            return year + 1, 1, 1
#        else:
#            return year, month + 1, 1
        
#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
#    days = 0
#    while (year1, month1, day1) < (year2, month2, day2):
#        year1, month1, day1 = nextDay(year1, month1, day1)
#        days += 1
#    return days  

#def test():
#    test_cases = [((2012,9,30,2012,10,30),30), 
#                  ((2012,1,1,2013,1,1),360),
#                  ((2012,9,1,2012,9,4),3)]
    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"

#test()


# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#  

#def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
#    if day < 30:
#        return year, month, day + 1
#    else:
#        if month == 12:
#            return year + 1, 1, 1
#        else:
#            return year, month + 1, 1
        
#def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
#    if year1 < year2:
#        return True
#    if year1 == year2:
#        if month1 < month2:
#            return True
#        if month1 == month2:
#            return day1 < day2
#    return False        

#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
#    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
#    days = 0
#    while dateIsBefore(year1, month1, day1, year2, month2, day2):
#        year1, month1, day1 = nextDay(year1, month1, day1)
#        days += 1
#    return days

#    days = 0
#    while dateIsBefore(year1, month1, day1, year2, month2, day2):
#        year1, month1, day1 = nextDay(year1, month1, day1)
#        days += 1
#    return days

#def test():
#    test_cases = [((2012,9,30,2012,10,30),30), 
#                  ((2012,1,1,2013,1,1),360),
#                  ((2012,9,1,2012,9,4),3),
#                  ((2013,1,1,1999,12,31), "AssertionError")]
    
#    for (args, answer) in test_cases:
#        try:
#            result = daysBetweenDates(*args)
#            if result != answer:
#                print "Test with data:", args, "failed"
#            else:
#                print "Test case passed!"
#        except AssertionError:
#            if answer == "AssertionError":
#                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
#            else:
#                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)            
#test()


# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

#months = [31,28,31,30,31,30,31,31,30,31,30,31]

#def leapyr(n):
#    if n % 400 == 0:
#        return True
#    if n % 100 == 0:
#        return False
#    if n % 4 == 0:
#        return True
#    else:
#        return False

#def daysInMonth(month,year):
#    if month == 2 and leapyr(year):
#        return 29
#    return months[month-1]


#def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
#    if day < daysInMonth(month,year):
#        return year, month, day + 1
#    else:
#        if month == 12:
#            return year + 1, 1, 1
#        else:
#            return year, month + 1, 1
        
#def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
#    if year1 < year2:
#        return True
#    if year1 == year2:
#        if month1 < month2:
#            return True
#        if month1 == month2:
#            return day1 < day2
#    return False        

#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
#    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
#    days = 0
#    while dateIsBefore(year1, month1, day1, year2, month2, day2):
#        year1, month1, day1 = nextDay(year1, month1, day1)
#        days += 1
#    return days

#def test():
#    test_cases = [((2012,1,1,2012,2,28), 58), 
#                  ((2012,1,1,2012,3,1), 60),
#                  ((2011,6,30,2012,6,30), 366),
#                  ((2011,1,1,2012,8,8), 585 ),
#                  ((1900,1,1,1999,12,31), 36523)]
    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"
#test()


# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

#list1 = [1,2,3,4]
#list2 = [1,2,3,4]

#list1 = list1 + [5, 6]
#list2.append([5, 6])

# to check, you can print them out using the print statements below.

#print "showing list1 and list2:"
#print list1
#print list2


# What is the difference between these two pieces of code?
#list1 = [1,2,3,4,5]
#list2 = [1,2,3,4,5]

#def proc(mylist):
#    mylist = mylist + [6, 7]

#def proc2(mylist):
#    mylist.append(6)
#    mylist.append(7)

# Can you explain the results given by the print statements below?

#print "demonstrating proc"
#print list1
#proc(list1)
#print list1
#print
#print "demonstrating proc2"
#print list2
#proc2(list2)
#print list2

# Python has a special assignment syntax: +=.  Here is an example:

#list3 = [1,2,3,4,5]

#def proc3(mylist):
#	mylist += [6,7]

#print "demonstrating proc3"
#print list3
#proc3(list3)
#print list3

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 


# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

#import random

# We then print a random integer using the random.randint(start, end) function
#print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be 
# of length 20

#random_list = []
#list_length = 20

# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.

#import random
#random_list = []
#while len(random_list) < 20:
#    random_list.append(random.randint(0, 10))



# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
#print random_list


# Now, we want to ask ourselves the question: How many occurrences of 
# the number 9 appear in our randomly made list?
# 
# For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to loop through the list and count the number of occurrences of the
# number 9. In the example list above, the number 9 occurs three times.

#import random

# 1. Create random list of integers using while loop
#random_list = []
#list_length = 20

#while len(random_list) < list_length:
#  random_list.append(random.randint(0,10))
    
# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.

#count = 0
#index = 0
#while index < len(random_list):
#    if random_list[index] == 9:
#        count += 1
#    index += 1

# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
#print random_list
#print count


# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11 
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.
#count_list = [0] * 11

# Check that we have a list of length 11 with all 0 elements
#print count_list

# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:

#count_list = [1,2,3,2,2,1,1,2,3,1,2]

# Let's print out the occurrences for the numbers 0, 4, 5, and 6
#print count_list[0]
#print count_list[4]
#print count_list[5]
#print count_list[6]

# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]

# Here's our code that we coded before

#import random

# Create random list of integers using while loop --------------------
#random_list = []
#list_length = 20

#while len(random_list) < list_length:
#  random_list.append(random.randint(0,10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

#count_list = [0] * 11
#index = 0

# Write code here to loop through every number in random_list and
# update count_list appropriately

#while index < len(random_list):
#  number = random_list[index]
#  count_list[number] = count_list[number] + 1
#  index = index + 1


# Check the list we created
#print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
#print sum(count_list)


# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

#import random

# Create random list of integers using while loop --------------------
#random_list = []
#list_length = 20

#while len(random_list) < list_length:
#    random_list.append(random.randint(0,10))

# Aggregate the data -------------------------------------------------
#count_list = [0] * 11
#index = 0

#while index < len(random_list):
#    number = random_list[index]
#    count_list[number] = count_list[number] + 1
#    index = index + 1
    
# Write code here to summarize count_list and print a neatly formatted table that looks
# like this:


#print "number | occurrence"
#index = 0
#num_len = len("number")

#while index < len(count_list):
#  num_spaces = num_len - len(str(index))
#  print " " * num_spaces + str(index) + " | " + str(count_list[index])
#  index = index + 1

"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

# Hint: To print 10 blank spaces in a row, we can multiply a string by a number "n"
# to print this string n number of times:
#print "Udacity! "*10

# BONUS!
# From your summarize code you just wrote, can you make the table even more visual by 
# replacing the count with a string of asterisks that represent the count of a number?
# The table should look like

"""
number | occurrence
     0 | *
     1 | **
     2 | ***
     3 | **
     4 | **
     5 | *
     6 | *
     7 | **
     8 | ***
     9 | *
    10 | **
"""

# Congratulations! You just created a distribution table of a list of numbers! 
# This is also known as a histogram


# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

#def product_list(list_of_numbers):
#    total = 1
#    for i in list_of_numbers:
#        total = total * i
#    return total


# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

#def greatest(list_of_numbers):
#    big = 0 
#    for i in list_of_numbers:
#        if i > big:
#            big = i
#    return big




#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0



#print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1


# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list. 
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

#string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
#string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
#list_of_words1 = string1.split() #fill this in
#list_of_words2 = string2.split() #fill this in
#print list_of_words1
#print list_of_words2


#Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.


#def word_in_pos(word, parts_of_speech):
    # your code here
    
#    if word in parts_of_speech:
#        return word
#    else:
#        for n in parts_of_speech:
#            if n in word:
#                return n
#            return None    
#    return None 
    


#test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
#parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

#print word_in_pos(test_cases[0], parts_of_speech)
#print word_in_pos(test_cases[1], parts_of_speech)
#print word_in_pos(test_cases[2], parts_of_speech)
#print word_in_pos(test_cases[3], parts_of_speech)


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

#parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

#test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

#def word_in_pos(word, parts_of_speech):
#    for pos in parts_of_speech:
#        if pos in word:
#            return pos
#    return None
        
#def play_game(ml_string, parts_of_speech):    
#    replaced = []
#    ml_string = ml_string.split()
#    for word in ml_string:
#        replacement = word_in_pos(word, parts_of_speech)
#        if replacement != None:
#            word = word.replace(replacement, "corgi")
#            replaced.append(word)
#        else:
#            replaced.append(word)
    
#    repalced=" ".join(replaced)
    
#    return replaced
    # your code here
    
#print play_game(test_string, parts_of_speech) 


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

#parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

#test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

#def word_in_pos(word, parts_of_speech):
#    for pos in parts_of_speech:
#        if pos in word:
#            return pos
#    return None
        
#def play_game(ml_string, parts_of_speech):    
#    replaced = []
#    ml_string = ml_string.split()
#    for word in ml_string:
#        replacement = word_in_pos(word, parts_of_speech)
#        if replacement != None:
#            word = word.replace(replacement, "corgi")
#            replaced.append(word)
#        else:
#            replaced.append(word)
#    replaced=" ".join(replaced)
#    return replaced
    # your code here
    
#print play_game(test_string, parts_of_speech)  


#with raw_input function line


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

#parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

#test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

#def word_in_pos(word, parts_of_speech):
#    for pos in parts_of_speech:
#        if pos in word:
#            return pos
#    return None
        
#def play_game(ml_string, parts_of_speech):    
#    replaced = []
#    ml_string = ml_string.split()
#    for word in ml_string:
#        replacement = word_in_pos(word, parts_of_speech)
#        if replacement != None:
#            word = word.replace(replacement, "corgi")
#            replaced.append(word)
#        else:
#            replaced.append(word)
    
#    repalced=" ".join(replaced)
    
#    return replaced
    # your code here
    
#print play_game(test_string, parts_of_speech) 


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

#parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

#test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

#def word_in_pos(word, parts_of_speech):
#    for pos in parts_of_speech:
#        if pos in word:
#            return pos
#    return None
        
#def play_game(ml_string, parts_of_speech):    
#    replaced = []
#    ml_string = ml_string.split()
#    for word in ml_string:
#        replacement = word_in_pos(word, parts_of_speech)
#        if replacement != None:
            #user_input = raw_input("Type in a: " + replacement)

#            word = word.replace(replacement, user_input)
#            replaced.append(word)
#        else:
#            replaced.append(word)
#    replaced=" ".join(replaced)
#    return replaced
    # your code here
    
#print play_game(test_string, parts_of_speech)  
