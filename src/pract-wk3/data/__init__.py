#
# wk10ex1.py
#
# naam: Erik Roos
#

class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same day, month, year
        as the calling object (self).
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew
 
    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        return self.equals(d2)

    def is_before(self, d2):
        """ Checks if self is before d2
        """
        if d2.year != self.year:
            return self.year < d2.year
        else:
            # Same year
            if d2.month != self.month:
                return self.month < d2.month
            else:
                # Same month
                return self.day < d2.day

    def __lt__(self, d2):
        return self.is_before(d2)

    def is_after(self, d2):
        """ Checks if self is after d2
        """
        if d2.year != self.year:
            return self.year > d2.year
        else:
            # Same year
            if d2.month != self.month:
                return self.month > d2.month
            else:
                # Same month
                return self.day > d2.day

    def __gt__(self, d2):
        return self.is_after(d2)

    def tomorrow(self):
        fdays = 28
        if self.is_leap_year():
            fdays = 29

        month_lengths = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day + 1 > month_lengths[self.month]:
            # Last day of month
            self.day = 1
            if self.month == 12:
                # Last day of year
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        fdays = 28
        if self.is_leap_year():
            fdays = 29

        month_lengths = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.day - 1 < 1:
            # First day of month
            if self.month == 1:
                # First day of year
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                self.day = month_lengths[self.month - 1]
                self.month -= 1
        else:
            self.day -= 1

    def add_n_days(self, n):
        #print(self)
        for _ in range(n):
            self.tomorrow()
            #print(self)

    def __iadd__(self, n):
        self.add_n_days(n)
        return self

    def sub_n_days(self, n):
        #print(self)
        for _ in range(n):
            self.yesterday()
            #print(self)

    def __isub__(self, n):
        self.sub_n_days(n)
        return self

    def diff(self, d2):
        """ Returns the number of days between self and d2.
        """
        self_copy = self.copy()
        d2_copy = d2.copy()
        if self_copy == d2_copy:
            return 0
        else:
            ndays = 0
            if d2_copy < self_copy:
                while d2_copy < self_copy:
                    d2_copy += 1
                    ndays += 1
            else:
                while d2_copy > self_copy:
                    d2_copy -= 1
                    ndays -= 1
            return ndays

    def dow(self):
        weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        ref_date = Date(10, 10, 2010) # a known Sunday
        ndays = self.diff(ref_date)
        day_index = ndays % 7
        return weekdays[day_index]

    def dow2(self, ref_date):
        weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        ndays = self.diff(ref_date)
        day_index = ndays % 7
        return weekdays[day_index]