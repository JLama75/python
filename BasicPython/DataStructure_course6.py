#Covers Chapter 6 and 7
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
'Bob' in greet
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
num = text.find('0')
print(num)
print(float(text[num : num+10]))

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

#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.upper()
    line = line.strip()
    print(line)

#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
fname= input("Enter file name: ") #mbox-short.txt
fh = open(fname)
count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        lineName = line
        print(lineName)
        count = count+1
        pos = lineName.find(":")
        print(pos)
        value = lineName[pos+1 : ]
        value = float(value.strip())
        print(value)
        sum = sum + value
average = sum/count
print("Average spam confidence: ", average)


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