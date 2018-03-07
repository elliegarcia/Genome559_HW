## This class represents the date
class Date:
    def __init__(self, day, month, year = 2018):
        if int(day) < 31 and int(day) > 0: # make sure the day is correct
            self.day = day
            self.month = month
            self.year = year
        else:
            print "Error, please print correct date"

    def __str__(self): # print the date as such: day-month-year
        day_str = '%s' % self.day
        mon_str = '%s' % self.month
        year_str = '%s' % self.year
        return day_str + "-" + mon_str + "-" + year_str

    def printUS(self): # print the date as such: month/day/year
        print self.month , "/", self.day, "/", self.year

    def printUK(self): # print the date as such: day.month.year (last two digits)
        print self.day, ".", self.month, ".", str(self.year)[2:]

    def addmonths(self, n = 1): # This function adds n months to the current date
        new_month = self.month + n
        self.year += (new_month-1)/12
        self.month = (new_month-1) % 12 + 1

    def addDays(self, n=1): # This function adds n days to the current date by replacing the current date
        new_day = self.day + n # add the current date + n

        while new_day > 0: # this loop keeps iterating until new_day is less than the days in that month
            if self.month > 12: # starts the month back at 1 after it reaches 12
                self.year += self.month / 12
                self.month = (self.month-1) % 12 + 1
            else:
                self.month = self.month

            if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7\
                    or self.month == 8 or self.month == 10 or self.month == 12: # if the month has 31 days
                new_day = new_day - 31 # take off the days in that month from new_day
                if new_day <= 0: # if new_day < the days in that month then
                    new_day += 31 # add 31 back (to get a positive number)
                    break # and break the loop
                else:
                    self.month += 1 # if new_day was > the days in that month than add +1 to the month
            elif self.month == 2: # if the month has 28 days
                new_day = new_day - 28 # take off the days in that month from new_day
                if new_day <= 0: # if new_day < the days in that month then
                    new_day += 28 # add 31 back (to get a positive number)
                    break # and break the loop
                else:
                    self.month += 1 # if new_day was > the days in that month than add +1 to the month
            else: # if the month has 30 days
                new_day = new_day - 30 # take off the days in that month from new_day
                if new_day <= 0: # if new_day < the days in that month then
                    new_day += 30 # add 30 back (to get a positive number)
                    break # and break the loop
                else:
                    self.month += 1 # if new_day was > the days in that month than add +1 to the month
        self.day = new_day # replace self.day with new_day

#### Running the functions ####


mydate = Date(22, 11, 1976)
mydate.printUK()
mydate.addDays(5)
mydate.printUK()