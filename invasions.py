from datetime import datetime, timedelta
import pytz


class InvasionTimer:
    invasion_delta = timedelta(hours=18, minutes=30)
    invasion_duration = timedelta(hours=6)

    def __init__(self, now=None):
        if now is None:
            now = datetime.now(tz=pytz.utc)

        self.now = now

    @property
    def next_invasion_date(self):
        """Return the next invasion date.
        Invasions start every 18.5 hours and last 6 hours."""
        # This is our base date. We now an invasion happened at that point (UTC).
        invasion_date = datetime(2017, 5, 2, 6, 30, 0, tzinfo=pytz.utc)

        while True:
            # Add 18.5h hours to the first know date
            # as long as it's smaller than the current date.
            if invasion_date >= self.now:
                return invasion_date

            invasion_date += InvasionTimer.invasion_delta

    @property
    def last_invasion_date(self):
        """Return the date of the last invasion."""
        return self.next_invasion_date - InvasionTimer.invasion_delta

    @property
    def invasion_running(self):
        """Return True or False if an invasion is currently going on."""
        invasion_date = self.last_invasion_date
        return invasion_date <= self.now <= invasion_date + InvasionTimer.invasion_duration

    @property
    def invasion_time_left(self):
        """Return the time left on an invasion if there's one going on."""
        if self.invasion_running:
            return (self.last_invasion_date + InvasionTimer.invasion_duration) - self.now
