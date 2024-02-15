from data import Date;

class TestData():
    #
    # een aantal datums om mee te werken...
    #
    d = Date(2, 12, 2020)           # Vandaag?
    d2 = Date(21, 12, 2020)         # Kerstvakantie
    ny = Date(1, 1, 2021)           # Nieuwjaar
    nd = Date(1, 1, 2030)           # Nieuw decennium
    nc = Date(1, 1, 2100)           # Nieuwe eeuw
    graduation = Date(12, 7, 2024)  # Pas dit zelf aan!
    vacation = Date(19, 7, 2021)    # Dit ook ~ zomervakantie!
    sm1 = Date(28, 10, 1929)        # Krach aandelenbeurs
    sm2 = Date(19, 10, 1987)        # Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...

    def test_copy(self):
        # Tests for copy
        dcopy = self.d.copy()
        assert self.d == dcopy

    def test_isbefore(self):
        # Tests for is_before
        assert self.d.is_before(self.d2)
        assert not self.nc.is_before(self.d)
        dcopy = self.d.copy()
        assert not dcopy.is_before(self.d)
        assert self.vacation < self.graduation

    def test_isafter(self):
        # Tests for is_after
        assert self.nc.is_after(self.ny)
        assert self.sm2 > self.sm1

    def test_tomorrow(self):
        # Tests for tomorrow
        dt = Date(31, 12, 2020)
        dt.tomorrow()
        assert dt == Date(1, 1, 2021)
        dt = Date(28, 2, 2020)
        dt.tomorrow()
        assert dt == Date(29, 2, 2020)
        dt.tomorrow()
        assert dt == Date(1, 3, 2020)

    def test_yesterday(self):
        # Tests for yesterday
        dy = Date(1, 1, 2021)
        dy.yesterday()
        assert dy == Date(31, 12, 2020)
        dt = Date(1, 3, 2020)
        dt.yesterday()
        assert dt == Date(29, 2, 2020)
        dt.yesterday()
        assert dt == Date(28, 2, 2020)

    def test_add_n_days(self):
        # Tests for add_n_days
        dn = Date(10, 12, 2021)
        dn.add_n_days(14)

    def test_sub_n_days(self):
        # Tests for sub_n_days
        dn = Date(23, 12, 2021)
        dn.sub_n_days(14)

    def test_plusis(self):
        # Tests for +=
        dn = Date(10, 12, 2021)
        dn += 14
        assert dn == Date(24, 12, 2021)

    def test_diff(self):
        # Tests for diff
        dd = Date(2, 12, 2020)
        dd2 = Date(19, 7, 2021)
        assert dd2.diff(dd) == 229
        assert dd.diff(dd2) == -229
        assert dd == Date(2, 12, 2020)

    def test_dow(self):
        # Tests for dow
        assert Date(7, 12, 1941).dow() == 'Sunday'
        assert Date(28, 10, 1929).dow() == 'Monday'
        assert Date(19, 10, 1987).dow() == 'Monday'
        assert Date(19, 6, 1980).dow() == 'Thursday'