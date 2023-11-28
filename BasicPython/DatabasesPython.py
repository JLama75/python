#Chapter 13-14
#Databases and object oriented programming

#ASCI
print(ord('H'))
print(ord('h'))
#UTF-8 #network data between two systems

#In python3, all strings internally are UNICODE (UTF-8).
#Working with string variables in python and reading data from files usually "just works".
#When we talk to a network resource using sockets or talk to a database we have to encode and eecode data (usually to UTF-8)

x = b'abc' #b -->byte
type(x)
#<class 'bytes'>
x = 'dkj'
type(x)
#<class 'str'>
x = u'dkj'
type(x)
#<class 'str'>



while True:
    data = mysock.recv(512)
    if(len(data) < 1) :
        break
    mystring = data.decode() #decode bytes into UNICODE
    print(mystring)

#Object oriented programming ; OOP
 #class - a template
 #method/message - a defined capability of a class
 #field/attribute - a bit of data in a class
 #object/instance- A particular instance of a class

 class PartyAnimal: #keyword is the class. PartyAnimal is the name of the class. This is the template for making PartyAnimal objects.
     x=0 #attribute#Each PartyAnimal object has a bit of data.

     def party(self): #party is a function/method
         self.x = self.x + 1
         print("So far", self.x)

    an = PartyAnimal() #Construct a PartyAnimal object and store in an variable
an.party() #Make a call to the object.method(parameter). PartyAnimal.party(an)

type(an)
dir(an)

#Object lifecycle
#The contructor and destructor are optional. Constructor is typically used to set up variables. The destructor is seldom used.

class PartyAnimal:
    x=0
    def __init__(self): # constructer: grab the variable: code that runs when an object is created
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)
an = PartyAnimal()
an.party()
an.party()
an = 42
an.party()

#Two independent instances
class PartyA:
    x = 0
    name = ""
    def __init__(self, z):  #constructer grabs the variable.
        self.name = z
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
s = PartyA("Sally")
s.party()

n = PartyA("Jim")
n.party()
s.party()

#Inheritance : extenstion: The ability to extend a class to make a new class
#Subclasses

class FootballFan(PartyA) : #extension: all the capabilities of partyA and more
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
j = FootballFan("Jim")
j.party()
j.touchdown()

dir(j)