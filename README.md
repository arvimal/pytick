#
# README.md for pytick
# 
#

The original idea for this tool comes from 'bati'.

pytick is intended to be an easy-to-use tool/tracker for answering tickets in support organisations. It keeps track of various
counts/stats on the tickets worked such as the shifts and is intended to use in Linux.

Some of the features are :

a) Open new cases.
b) Open existing cases.
c) 
e) 

..add more features here, as it gets implemented..

TO-DO:
------
1) Add the time in epoch to each cases opened and updated. All the epoch times can be added one below one. From the second time onwards,
only add it if there is a change in the file. else dont.. since tickets can be opened just for viewing too.
2) Add a 'Subject' line when a new ticket is created. 
3) If 'search' is used for the first time and not tickets exists, print "No tickets exists in database".
4) 'list total <year>' should print total number of cases, 
5) 'list total <month> <year>' should list cases for that month.
6) 'list total <day> <month> <year>'

1) Searching through the cases using wildcards (TBI)
2) Getting the count of cases done on a particular date, use 'list'. (TBI)
3) Finding cases can be drilled down to the shift in which it was answered, using 'list'. (TBI)
4) Search for keywords, pytick will print the tickets which has the said keywords. (TBI) 
5) Open the file with a template if opened using 'Open'. * Not on priority * 
6) Search, searches for keywords in the cases. 
7) Implement a db for pytick which gets updated on each search, sort of a pickle or whatever.
8) Implement history for commands.
9) Search for cases updated in between dates. '>>> search 10-12-2011 10-11-2012'
10)

###########
###########

Features in alpha v1:
--------------------
1) Open new cases
2) Open existing cases.
3) If a ticket number is not mentioned with 'open', pytick will prompt for an input.
4) Only one ticket can be opened with 'open'. Once the case is opened, the control is passed back to pytick and hence the second case can be opened. 
5) If the tool is run for the first time, it creates the dir hierarchy under /home/<user-name>/pytick/ and puts the cases created under 'tickets'.
6) pytick will create the necessary dir structure to store data if its running for the first time, else will start the 'pytick >>>' prompt.

FIXED:
------
1) Returns control to 'pytickloop()' from open() subprocess.call(), using subprocess.Popen()
2) Creates sub directories if the destination dir does not exist.
3) Returns to pytickloop() if an argument is not passed to 'open()'.
4) If more than one case number is mentioned, it shows the help.
5) If only 'open' is mentioned, it will show a message "'open' needs a ticket number".
6) Tickets can be opened with any names. Restrict this to integers.
7) 'open' only accepts integers.
8) 'open' only take a single int argument. After the editor is opened, control is passed over to pytick so that further operations can be done.


