#Covers Chapter 6
#splicing string
word = 'Monte Carlo'
print(word[0:6])
print(word[:6])

#string library or string methods
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print('Hi There'.lower())
type(greet)
dir(greet) #,methods in class greet.

#str.captitalize()

#str.find()
pos = greet.find('Bob')
#-->6
'Bob' in pos
print(pos)

#search and replace
nstr = greet.replace('there', 'Bob')
print(nstr)

#stripping whitespaces

greet = ' Hello Bob '
print(greet.lstrip())
#--> 'Hello Bob '
print(greet.rstrip())
#--> ' Hello Bob'
print(greet.strip())
#--> 'Hello Bob'

#line.stratswith('Please') --> True/false


#From stephhen.marquard@duct.act.za Sat Jan 5

data = 'From stephhen.marquard@duct.act.za Sat Jan 5'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos) #start searching ' ' from atpos
print(sppos)

host = data[atpos+1 : sppos] # data[21:31] --> splicing
print(host)

#Parsing Strings
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
num = text.find(':')
print(num)
piece = text[num+1 : num+10]
print(float(piece.strip()))


#Chapter 7 #secondary storage
#File processing
#handle = open(filename, mode) : filehandle is like a connection
#default print() adds new line
fname = input('Enter the file name: ')
try:
    fname = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

xfile = open('mbox.txt')
inp = fhand.read()
print(len(inp))
count =0
for line in xfile: #cheese is the iterative variable.
    print(line)
    line = line.rstrip()
    count = count +1
    if line.startswith('From: ') : #searching through a file
        print(line)
    if not line.startswith('From: ') : #searching through a file
        continue
    if not '@uct.ac.za' in line :
        continue
    print(line)
print('Line count', count)


#7.1 Write a program that prompts for a file name, then opens that file and
# reads through the file, and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.upper()
    line = line.rstrip() #print automatically adds new line. so use line.rstrip() to remove new line
    print(line)


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    lineName = line
    #print(lineName)
    count = count+1
    pos = lineName.find(":")
    #print(pos)
    value = lineName[pos+1 : ]
    value = float(value.strip())
    #print(value)
    s = s + value
average = s/count
print("Average spam confidence:", average)


#Data structures #Chapter 8-10
#Lists
lists = [1, 2, 3, [5, 6], 'red']
lits = [] #empty lists

#lists are mutable; changaeble
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
print(len(lotto))

#range function returns a list of numbers that ranges from zero to one less than the parameter
#makes it easier to iterate lists through a for loop

print(range(4)) # 0, 1, 2, 3

#counted loops
for i in range(len(lists)) :
    l = lists[i]
    print('Happy new year', l)

#adding lists together
addList = lotto + lists
print(addList)

#slicing lists
t = lists[1:3] #the second number is up to but not including
print(t)

#MAKE A BRAND NEW LIST
stuff = list()
stuff.append("book")
stuff.append(99)
stuff.append("Glen")
#in #True or false
99 in stuff
20 not in stuff

#sort in alfabetical order
friends = ["a", "f", "b"]
friends.sort()
#making a list can take large memory if working with big data sets.
#len(), max(), min(), sum()

#split breaks a string into parts and produces a list of strings.
# #Think of these as words, we can access a particular word or loop through all the words
abc = 'With three words'
stuff = abc.split()
print(stuff)

#split assumes multiple spaces as one space/delimiter by default

line= 'A lot of         spaces'
etc = line.split()
print(etc)

#specifying delimiter
line = 'first;second;third'
thing= line.split(';')
print(thing)

#Double split pattern
#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and
# if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown
# in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter the filename: ") #romeo.txt
fh = open(fname)
wordList = list()
for line in fh:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print("words within loop: ",words)
    for w in words:
        if w in wordList :
          continue
        wordList.append(w)
        #print("WORDLIST within loop: ",wordList)
wordList.sort()
print(wordList)

#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ") #mbox-short.txt
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    ##############guardian pattern###################
    #if len(line) < 3: #this skips the blank lines that could give errors as the line[0] will be blank
        #print('Skip line')
        #continue
    #if line == '':
        #print('Skip line')
    # if line[0] != 'From' :
       #continue
    #if len(line) < 3 or line[0] != 'FROM':
        #continue
    ######################################################
    if not line.startswith("From "):
    words = line.split() #put the words in the line in a list
    email = words[1] #select the word you want from the list
    print(email)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")

#######################################################################################################
#Dictionaries #Chapter 9
#Associative arrays - Perl/PHP
# a "bag" of values each with its own labels

purse = dict()
purse['monkey'] = 12 #variable['key'] = value
purse['candy'] = 3
purse['tissue'] = 15
print(purse)
print(purse['candy'])
#is mutable
purse['tissue'] = purse['candy'] + 2

jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
ooo = { } #empty dictionary

######
#Making a dictionary of names and how many times they repeat as values

counts ={} #making counts dictionary which is empty
names = ["Holly", "Fred", "shim", "Holly", "hans", "shim", "Holly"]

for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

#checking to see if a key is already in the dictionary and assumes a default value if key does not exist (0) therfore doesn't give traceback.
if name in counts:
    x = counts[name]
else :
    x = 0
#or,

counts = dict()
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

for key in counts:
    print(key, counts(key))
    #to print list of keys
    print(list(counts))
    print(counts.keys())
    #to print values
    print(counts.values())
    #items gives tupples
    print(counts.items())

#to go through both the key value pairs
for a_key, b_vaue in counts.items() :
    print(a_key, b_vaue)
####################################
#Read a file and make a list of words and count them. Search for the most frequent word.
name = input('Enter file: ') #romeo.txt
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


#Tuples
# strings and tuples are immutable

x= (2, 3, 4, 5)
(x, y) = (4, 'fred')
#for (k,v) in count.items():
(0, 1, 2) < (5, 1, 2)
#True
("James", "salley") < ("ZAOR", "DJI")
sorted(counts.items()) #sorting by keys

#sort by values instead of keys.
#First convert dict into tupples and sort them

c= {'c': 10, 'b': 1, 'a': 22}
tmp = list() #making an empty list
for k, v in c.items():
    tmp.append((v, k)) #making list of tuples with value first
print(tmp)
tmp = sorted(tmp, reverse=True) #sort it reverse i.e. high to low
print(tmp)

#open and read through a file. Count the number of each words. Return top ten common words.

fhand= open('mbox-short.txt') #romeo.txt
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True) #sort based on max counts

#print out top ten
for v, k in lst[:10] :
    print(k, v)

############# Shorter version of above code ##########################
#List Comprehension --> dynamic list

print(sorted([ (v,k) for k,v in counts.items() ], reverse=True))

################
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)

count = dict()
#reading through the lines and creating dictionary:
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    #print(time)
    t = time.split(':')
    hour = t[0]
    #print(hour)
    count[hour] = count.get(hour, 0) + 1
#print(count.items())

#sort it by hour
for k, v in sorted(count.items()):
    print(k, v)

