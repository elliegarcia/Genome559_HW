class Date:
    def __init__(self, day, month, year = 2018):
        if int(day) < 31 and int(day) > 0:
            self.day = day
            self.month = month
            self.year = int(year)
        else:
            print "Error, please print correct date"

    def __str__(self) :
        day_str = '%s' % self.day
        mon_str = self.month
        year_str = self.year
        return mon_str + "-" + day_str + "-" + year_str

    def printUS(self):
        print self.month , "/", self.day, "/", self.year

    def printUK(self):
        print self.day, ".", self.month, ".", str(self.year)[2:]

    def addDays(self, n=1):


mydate = Date( 21, 'Feb')
mydate.printUS()