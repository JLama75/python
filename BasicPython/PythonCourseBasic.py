# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Covers Basic python chapters 1-5
x = 1 #Assignement statements
print(x)
x = x + 2
print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#conditional
if x < 10:
    print('smaller')
if x > 20:
    print('Bigger')
if x == 5:
    print('Equals 5')
print ('Finish')

#repeated steps: Loops: While, for

n=5
while n > 0 :
    print(n)
    n = n - 1
print('Blstoff!')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger that 2')
    else :
        print('smaller than 2')
    print('Done with i', i)
print('All done')

if x < 2:
    print('small')
elif x <10:
    print('Medium')
else :
    print('Large')
print('all done')
#Fixed numbers are constants.
#reserved words:
#variables- places where allocate a bit of memory and stick something in them/ store data on it and retrive it later
#case sensitive, bad to start with numbers and mixture of numbers and characters
#Mnemonic variables

#Expressions
xx = 1
print(xx/2)
eee = 'Hello'
type (eee)
type (xx)

#convert string to integer
stringval= '123'
type(stringval)
integerval = int(stringval)
x= 12+ integerval
print(x)

#User Input: read data from user. Input function returns a string
name = input('Type your name here?')
print('Welcome', name) #every comma puts a space.

#Convert elevators floors
inp = input('Europe floor?')
usf = int(inp) + 1
print('USA floor', usf)

# This first line is provided for you

hrs = input("Enter Hours:")
rate = input ("Enter rate:")
pay = float(hrs)* float(rate)
print('Pay:', pay)



#try/except
rawstr = input('Enter a number: ')
try:
     ival = int(rawstr)
except:
     ival = -1

if ival > 0 :
    print('Nice work')
else:
    print('Not a number')


#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    try:
        h = float(hrs)
        r = float(rate)
    except :
        print("Error, please enter numeric input")
        quit()

    if h <= 40:
        pay = h * r
        print(pay)
    elif h > 40:
        add = h - 40
        nrate = 1.5 * r
        pay = (40 * r) + (add * nrate)
        print(pay)
    else:
        print('Not a number')

#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score between 0.0 to 1.0: ")
try:
    s = float(score)
except:
    print('please enter numeric input')

if 0 <= s <= 1:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    elif s < 0.6:
        print('F')
else:
    print("Score out of range")
    quit()
#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and
# use the function to do the computation. The function should return a value. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float()
# to convert the string to a number. Do not worry about error checking the user input unless you want to -
# you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    if h > 40:
        diff = h - 40
        pay = (40 * r) + (diff * 1.5 * r)
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(float(hrs), float(rate))
print("Pay", p)

#Indefinite loop: While loop

while True:
    line = input('> ')
    if line == 'done' :
        break #stops/escapes from the loop to avoid infinite loop
    print(line)
print('Done!')


#continue: statement ends the current iteration and jumps to the top of the loop to start the next iteration

while True:
    line = input('> ')
    if line[0] == '#' : #if the input starts with the '#' sign it skips that line/input and goes to the next
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

#Definite loops: For loops

for i in [5, 4, 3, 2, 1] :
    print (i)
print('Blastoff!')

#definite loops have explicit iteration variables that change each time through a loop. The iteration variables move through a  sequence or set.

#summing in a loop

sum = 0
count = 0
print ('Before', count, sum)
for thing in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + thing
    print (count, sum, thing)
print('After', count ,sum, sum/count) # printing no. of iterations, sum and average

#boolean variable: True or False

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)

#none type variable: lack of value
#smallest number search
smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None : #first time #is used for None and True/False
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num +1
    tot = tot + fval
print('All done!')
print(tot, num, tot/num)

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None :
        largest = num
    elif num > largest:
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)
