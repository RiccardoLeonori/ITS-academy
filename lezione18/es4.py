'''
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa 
implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  
A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; 
it must be instantiated from a string.
'''

class Database:

    def __init__(self, date:str) -> str:
        self.date = date

    def new_date(data:str) -> str:
        pass

    def delete_date(data:str) -> str:
        pass