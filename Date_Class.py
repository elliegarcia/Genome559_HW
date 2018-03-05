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

    def addDays(self, n=1): # This function adds n days to the current date by adding
        # n to the current day and subtracting each subsequent month from the total
        new_day = self.day + n # add the current date + n

        while new_day > 0:
            if self.month > 12:
                self.year += self.month / 12
                self.month = (self.month-1) % 12 + 1
            else:
                self.month = self.month

            if self.month==1 or self.month==3 or self.month==5 or self.month==7\
                    or self.month==8 or self.month==10 or self.month == 12:
                new_day = new_day - 31
                if new_day <= 0:
                    new_day += 31
                    break
                else:
                    self.month += 1
            elif self.month == 2:
                new_day = new_day - 28
                if new_day <= 0:
                    new_day += 28
                    break
                else:
                    self.month += 1
            else:
                new_day = new_day - 30
                if new_day <= 0:
                    new_day += 30
                    break
                else:
                    self.month += 1
        self.day = new_day


elmersbday = Date(9, 5, 1994)
elmersbday.addDays(8694)
print elmersbday