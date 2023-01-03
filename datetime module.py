import datetime


# Datetime module :-> import a module name dateime to work with dates as date objects.



x= datetime.datetime.now() # it is use to show the current date and time.
print(x)

# the date contains year, month, day, hour, minute, second, and microsecond.
# Creating Date objects.
x= datetime.datetime(2021,1,24) # it show the sequence of given format.
print(x)

# He method is called strftime(), and takes one parameter, format to specify the format of the returned string:
# %b => Month name, short version             - Dec
# %B => Month name, full version              - December
# %m => Month as a number 01-12               - 12
# %y => year, short version, without century  - 18
# %Y => year, full version                    - 2018
# %H => Hour 00-23                            - 17
# %I => Hour 00-12                            - 05
# %p => AM/PM                                 - PM
# %M => minute 00-59                           - 32
# %s => second 00-59                          - 34

y=datetime.datetime.now()
n=y.strftime("%M")
print(y)
print(n)
print(datetime.datetime(2022,3,22))
