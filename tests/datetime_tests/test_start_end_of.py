from itertools import product, tee
from pendulum import DateTime

from .. import AbstractTestCase


class StartEndOfTest(AbstractTestCase):

    def test_start_of_second(self):
        d = DateTime.now()
        new = d.start_of('second')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, d.minute, d.second, 0)

    def test_end_of_second(self):
        d = DateTime.now()
        new = d.end_of('second')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, d.minute, d.second, 999999)

    def test_start_of_minute(self):
        d = DateTime.now()
        new = d.start_of('minute')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, d.minute, 0, 0)

    def test_end_of_minute(self):
        d = DateTime.now()
        new = d.end_of('minute')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, d.minute, 59, 999999)

    def test_start_of_hour(self):
        d = DateTime.now()
        new = d.start_of('hour')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, 0, 0, 0)

    def test_end_of_hour(self):
        d = DateTime.now()
        new = d.end_of('hour')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, d.hour, 59, 59, 999999)

    def test_start_of_day(self):
        d = DateTime.now()
        new = d.start_of('day')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, 0, 0, 0)

    def test_end_of_day(self):
        d = DateTime.now()
        new = d.end_of('day')
        self.assertIsInstanceOfDateTime(new)
        self.assertDateTime(new, d.year, d.month, d.day, 23, 59, 59, 999999)

    def test_start_of_month_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.start_of('month'))

    def test_start_of_month_from_now(self):
        d = DateTime.now()
        new = d.start_of('month')
        self.assertDateTime(new, d.year, d.month, 1, 0, 0, 0)

    def test_start_of_month_from_last_day(self):
        d = DateTime(2000, 1, 31, 2, 3, 4)
        new = d.start_of('month')
        self.assertDateTime(new, 2000, 1, 1, 0, 0, 0)

    def test_start_of_year_is_fluid(self):
        d = DateTime.now()
        new = d.start_of('year')
        self.assertIsInstanceOfDateTime(new)

    def test_start_of_year_from_now(self):
        d = DateTime.now()
        new = d.start_of('year')
        self.assertDateTime(new, d.year, 1, 1, 0, 0, 0)

    def test_start_of_year_from_first_day(self):
        d = DateTime(2000, 1, 1, 1, 1, 1)
        new = d.start_of('year')
        self.assertDateTime(new, 2000, 1, 1, 0, 0, 0)

    def test_start_of_year_from_last_day(self):
        d = DateTime(2000, 12, 31, 23, 59, 59)
        new = d.start_of('year')
        self.assertDateTime(new, 2000, 1, 1, 0, 0, 0)

    def test_end_of_month_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.end_of('month'))

    def test_end_of_month_from_now(self):
        d = DateTime.now().start_of('month')
        new = d.start_of('month')
        self.assertDateTime(new, d.year, d.month, 1, 0, 0, 0)

    def test_end_of_month(self):
        d = DateTime(2000, 1, 1, 2, 3, 4).end_of('month')
        new = d.end_of('month')
        self.assertDateTime(new, 2000, 1, 31, 23, 59, 59)

    def test_end_of_month_from_last_day(self):
        d = DateTime(2000, 1, 31, 2, 3, 4)
        new = d.end_of('month')
        self.assertDateTime(new, 2000, 1, 31, 23, 59, 59)

    def test_end_of_year_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.end_of('year'))

    def test_end_of_year_from_now(self):
        d = DateTime.now().end_of('year')
        new = d.end_of('year')
        self.assertDateTime(new, d.year, 12, 31, 23, 59, 59, 999999)

    def test_end_of_year_from_first_day(self):
        d = DateTime(2000, 1, 1, 1, 1, 1)
        new = d.end_of('year')
        self.assertDateTime(new, 2000, 12, 31, 23, 59, 59, 999999)

    def test_end_of_year_from_last_day(self):
        d = DateTime(2000, 12, 31, 23, 59, 59, 999999)
        new = d.end_of('year')
        self.assertDateTime(new, 2000, 12, 31, 23, 59, 59, 999999)

    def test_start_of_decade_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.start_of('decade'))

    def test_start_of_decade_from_now(self):
        d = DateTime.now()
        new = d.start_of('decade')
        self.assertDateTime(new, d.year - d.year % 10, 1, 1, 0, 0, 0)

    def test_start_of_decade_from_first_day(self):
        d = DateTime(2000, 1, 1, 1, 1, 1)
        new = d.start_of('decade')
        self.assertDateTime(new, 2000, 1, 1, 0, 0, 0)

    def test_start_of_decade_from_last_day(self):
        d = DateTime(2009, 12, 31, 23, 59, 59)
        new = d.start_of('decade')
        self.assertDateTime(new, 2000, 1, 1, 0, 0, 0)

    def test_end_of_decade_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.end_of('decade'))

    def test_end_of_decade_from_now(self):
        d = DateTime.now()
        new  = d.end_of('decade')
        self.assertDateTime(new, d.year - d.year % 10 + 9, 12, 31, 23, 59, 59, 999999)

    def test_end_of_decade_from_first_day(self):
        d = DateTime(2000, 1, 1, 1, 1, 1)
        new = d.end_of('decade')
        self.assertDateTime(new, 2009, 12, 31, 23, 59, 59, 999999)

    def test_end_of_decade_from_last_day(self):
        d = DateTime(2009, 12, 31, 23, 59, 59, 999999)
        new = d.end_of('decade')
        self.assertDateTime(new, 2009, 12, 31, 23, 59, 59, 999999)

    def test_start_of_century_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.start_of('century'))

    def test_start_of_century_from_now(self):
        d = DateTime.now()
        new = d.start_of('century')
        self.assertDateTime(new, d.year - d.year % 100 + 1, 1, 1, 0, 0, 0)

    def test_start_of_century_from_first_day(self):
        d = DateTime(2001, 1, 1, 1, 1, 1)
        new = d.start_of('century')
        self.assertDateTime(new, 2001, 1, 1, 0, 0, 0)

    def test_start_of_century_from_last_day(self):
        d = DateTime(2100, 12, 31, 23, 59, 59)
        new = d.start_of('century')
        self.assertDateTime(new, 2001, 1, 1, 0, 0, 0)

    def test_end_of_century_is_fluid(self):
        d = DateTime.now()
        self.assertIsInstanceOfDateTime(d.end_of('century'))

    def test_end_of_century_from_now(self):
        now = DateTime.now()
        d = now.end_of('century')
        self.assertDateTime(d, now.year - now.year % 100 + 100, 12, 31, 23, 59, 59, 999999)

    def test_end_of_century_from_first_day(self):
        d = DateTime(2001, 1, 1, 1, 1, 1)
        new = d.end_of('century')
        self.assertDateTime(new, 2100, 12, 31, 23, 59, 59, 999999)

    def test_end_of_century_from_last_day(self):
        d = DateTime(2100, 12, 31, 23, 59, 59, 999999)
        new = d.end_of('century')
        self.assertDateTime(new, 2100, 12, 31, 23, 59, 59, 999999)

    def test_average_is_fluid(self):
        d = DateTime.now().average()
        self.assertIsInstanceOfDateTime(d)

    def test_average_from_same(self):
        d1 = DateTime.create(2000, 1, 31, 2, 3, 4, 5)
        d2 = DateTime.create(2000, 1, 31, 2, 3, 4, 5).average(d1)
        self.assertDateTime(d2, 2000, 1, 31, 2, 3, 4, 5)

    def test_average_from_greater(self):
        d1 = DateTime.create(2000, 1, 1, 1, 1, 1, 1, tz='local')
        d2 = DateTime.create(2009, 12, 31, 23, 59, 59, 999999, tz='local').average(d1)
        self.assertDateTime(d2, 2004, 12, 31, 12, 30, 30, 500000)

    def test_average_from_lower(self):
        d1 = DateTime.create(2009, 12, 31, 23, 59, 59, 999999, tz='local')
        d2 = DateTime.create(2000, 1, 1, 1, 1, 1, 1, tz='local').average(d1)
        self.assertDateTime(d2, 2004, 12, 31, 12, 30, 30, 500000)

    def test_average_with_microseconds(self):
        for d1, d2, expected_average in [
            # 3ms and 5ms should average to 4
            ((1982, 12, 4, 1, 2, 3, 3), (1982, 12, 4, 1, 2, 3, 5), (1982, 12, 4, 1, 2, 3, 4)),
            # 999999ms and subsequent 1ms should average to 0
            ((1982, 12, 4, 0, 0, 0, 999999), (1982, 12, 4, 0, 0, 1, 1), (1982, 12, 4, 0, 0, 1, 0)),
            # 1.000002 should average to 0.500001
            ((2000, 1, 1, 0, 0, 0, 0), (2000, 1, 1, 0, 0, 1, 2), (2000, 1, 1, 0, 0, 0, 500001)),
        ]:
            d1 = DateTime.create(*d1)
            d2 = DateTime.create(*d2)
            a1 = d1.average(d2)
            a2 = d2.average(d1)
            self.assertDateTime(a1, *expected_average)
            self.assertDateTime(a2, *expected_average)

    def test_average_commutative(self):
        for d1, d2 in product(*tee([
            DateTime.create(1981, 10,  9,  1,  2,  3,  4),
            DateTime.create(1982, 12,  4,  5,  6,  7,  8),
            DateTime.create(2013,  4, 13,  9, 10, 11, 12),
            DateTime.create(1982,  9, 24, 13, 14, 15, 16),
        ])):
            a1 = d1.average(d2)
            a2 = d2.average(d1)
            self.assertEqual(a1, a2)

    def start_of_with_invalid_unit(self):
        self.assertRaises(ValueError, DateTime.now().start_of('invalid'))

    def end_of_with_invalid_unit(self):
        self.assertRaises(ValueError, DateTime.now().end_of('invalid'))

    def test_start_of_with_transition(self):
        d = DateTime(2013, 10, 27, 23, 59, 59, tzinfo='Europe/Paris')
        self.assertEqual(3600, d.offset)
        self.assertEqual(7200, d.start_of('month').offset)
        self.assertEqual(7200, d.start_of('day').offset)
        self.assertEqual(3600, d.start_of('year').offset)

    def test_end_of_with_transition(self):
        d = DateTime(2013, 3, 31, tzinfo='Europe/Paris')
        self.assertEqual(3600, d.offset)
        self.assertEqual(7200, d.end_of('month').offset)
        self.assertEqual(7200, d.end_of('day').offset)
        self.assertEqual(3600, d.end_of('year').offset)

    def test_start_of_invalid_unit(self):
        d = DateTime(2013, 3, 31, tzinfo='Europe/Paris')

        self.assertRaises(ValueError, d.start_of, 'invalid')

    def test_end_of_invalid_unit(self):
        d = DateTime(2013, 3, 31, tzinfo='Europe/Paris')

        self.assertRaises(ValueError, d.end_of, 'invalid')
