# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == "red":
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise Exception("Undefined instruction for color: {}".format(light))

car_at_light("blue")

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 


def safe_subtract(a, b):
    try:
        return b-a
    except TypeError:
        print("None")

June=(10,90)
safe_subtract(June,231)

# 


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

John= {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
Janet= {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}

import datetime
year = datetime.datetime.today().year

def retrieve_age_eafp(person):
    if 'birth' in person:
        return year - person['birth']
    else: 
        print("There is something wrong with your input.")


def retrieve_age_lbyl(person):
    try:
        return year - person['birth']
    except KeyError:
        print("Looks like the key 'birth' is not in your dictionary.")

retrieve_age_eafp(John)
retrieve_age_eafp(Janet)

retrieve_age_lbyl(John)
retrieve_age_lbyl(Janet)

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#


def read_data():
    try:
        with open("data.csv", "r") as f:
            return f.read()
    except FileNotFoundError:
        print("The file does not exist.")

read_data("asdasd:)


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

print(total_double_sum)

'''Rui's comment: In order to print the total_double_sum, in the last line of code, you need to refer to the object double after the +=, not elem. If the code,
doesn't change it only prints the sum of the elements (17) not its double (34).
Thus our suggestion for the code would be:'''

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

print(total_double_sum)


### (b)

strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings+"_"+string

print(strings)

    
'''Rui's comment: There is a problem with the code if the goal is to put a underscore between each word. This code would only put the underscore between the last two words. Furthermore, it would also put an underscore at the beginning of the string.
 There are two ways of solving it.
First it would be to change the code by saying that if the list is empty, just add the word, and if it is not, add the underscore and the word.
# strings = '''
for string in ['I', 'am', 'Groot']:
    if strings == '':
        strings += string
    else:
        strings += "_"+ string
''' Second it would be to go through the list and add the underscore after the word except the last one.'''
strings = ''
for string in ['I', 'am', 'Groot']:
    if string != string[-1]:
        strings = strings+"_"+string
    else:
        strings += string

print(strings)

### (c) Careful!
j=10
while j > 0:
   j += 1

'''Rui's comment:
 This code is going to run forever because j is always going to be greater than 0, if you are just adding 1 to it.
 If you want to run the code until it is above 0, you could put j-=1 inside the while loop, and it would finish when it hits 0.
 If you want to run the code until it is 10, you change j to 0 and put j+=1 inside the while loop.
Our suggestion would be to change the code to:'''
j=10
while j > 0:
   j -= 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

'''Rui's comment: # If you want to use productory and multiply it by the elements in the list, you should start with productory = 1, not 0. 
Otherwise, the result will always be 0 as the product of any number times 0 is 0.
You could also create a list named productory and append the productory of the elements in the list, but that would be a different approach and would take a more code.
One way to do it would be: '''
productory = 1
for elem in [1, 5, 25]:
    productory *= elem

