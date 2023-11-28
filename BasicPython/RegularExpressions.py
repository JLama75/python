import re
fh = open("regex_sum_42.txt")
for line in fh:
    if re.search('^From:', line) : #^ first character
        print (line)
    #^X.*:
    ##Matches lines starting with X; . matches any character, *0 or more times; follwoed by colon
    #example: X-Sieve: CMU
    #^X-\S+:
    ## Matches the start of the line with X-; \S matches any non-whitespace character; + One or more times; followed by colon

re.search('^From') #returns T/F statement after matching string
re.findall() #matching strings are extracted

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
z = re.findall('[AEIOU]+', x)
print(y)
print(z)

#Greedy matching: gives as large as possible matches
y = re.findall('^F.+?:', x) #? stops greedy matching
x = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
#['stephan.marquard@uct.ac.za']

#Parentheses are not part of the match- but they tell where to start and stop what string to extract.
#Only extracts string matching within the parenthesis outside is just for matching
y = re.findall('^From (\S+@\S+)', x) #['stephan.marquard@uct.ac.za']
y= re.findall('@([^ ]*)', x) # [^] indicates not. [^ ] indicates not-blank character, * 0 or more times
#['uct.ac.za']

y = re.findall('^From .*@([^ ]*)')
x= 'We just recieved $10.00 for our party'
#if you want to extract $10.00 use '\' for special characters such as $
y = re.findall('\$[0-9]+',x)

x ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
#####################################################################################
#Exercise:
import re

filename = input("Name of the file: ")
if len(filename) < 1:
    filename = "regex_sum_42.txt"

fh = open(filename)
num = list()
sum = 0
count = 0

for line in fh:
    line = line.rstrip()
    count = count + 1
    y = re.findall('[0-9]+', line)
    if not len(y) >= 1:
        continue
    #print("result of findall: ", y)
    for i in y:
        i = int(i)
        sum = sum + i
        print('For count', count, "num is:", i)
        num.append(i)
print('Sum is:', sum)



