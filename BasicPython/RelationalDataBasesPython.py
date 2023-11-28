 #Two Roles in Large Projects:
 #Application Developer: Builds the logic for the application, the look and feel of application- monitors the application for problems

 #Database Administrator: Monitors and adjusts the database as the program runs in production

# python has built in SQL
#SQLite is a popular database , free fast and small. SQLite Browser allows us to directly manipulate SQLite files
#There is also a Firefox plugin to manipulate SQLite database
#SQLite is embedded in Python

#Do the following code in SQL:
CREATE TABLE Users (
	email VARCHAR (128),
    COUNT INTEGER (128)
)

INSERT INTO Users(name, email) VALUES ('Kristen', 'kf@umich.edu')
DELETE FROM Users WHERE email='kf@umich.edu'
UPDATE Users SET name='Charles' WHERE email='csev@umic.edu'
SELECT * FROM Users  WHERE email='csev@umic.edu'
SELECT * FROM Users ORDER BY email

import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #secure connection to the database
cur = conn.cursor() #acts as a cursor

cur.execute('DROP TABLE IF EXISTS Counts') # If already there is a table named counts then remove it
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)') #wirte SQL code

fname = input('Enter file name: ')
if (len(fname) < 1) : fname ='mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #? is a placeholder and give a tupple like (email,)
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit() #save to disk

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()



#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
 # (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

#CREATE TABLE Counts (org TEXT, count INTEGER)
#When you have run the program on mbox.txt upload the resulting database file above for grading.
#If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.
#You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
#The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
#Because the sample code is using an UPDATE statement and committing the results to the database as each record is
 # read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely
 # writing all the data to disk every time it is called.
#The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program,
 # there is a balance between the number of operations you execute between commits and the importance of not losing the results
 # of operations that have not yet been committed.

import sqlite3

conn = sqlite3.connect('emailassignment.sqlite') #secure connection to the database
cur = conn.cursor() #acts as a cursor

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#Top organizational count

fname = input('Enter filename: ')
if len(fname)<1 :
    fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("From: "): continue
    line = line.rstrip()
    line = line.split()
    email = line[1]
    mail = email.split("@")
    org = mail[1]
    #print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone() #fetchone method retrievs the next row of a querry result set and returns a single sequence or None if no more rows are available
    #print(row)
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ', (org,))
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
