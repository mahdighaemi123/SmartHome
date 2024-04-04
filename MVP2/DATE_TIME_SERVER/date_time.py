from persiantools.jdatetime import JalaliDateTime
import pytz
import time


class DateTime():
    def __init__(self, timezone="Asia/Tehran"):
        self.timezone = timezone

    def get_date_time(self):
        timestamp = time.time()
        jdate = JalaliDateTime.fromtimestamp(
            timestamp, pytz.timezone(self.timezone))
        date = jdate.to_gregorian()

        date_time = {
            "timestamp": timestamp,
            "hour": jdate.hour,
            "minute": jdate.minute,
            "second": jdate.second,
            "jyear": jdate.year,
            "jmonth": jdate.month,
            "jday": jdate.day,
            "year": date.year,
            "month": date.month,
            "day": date.day,

            "jweek_day": jdate.strftime("%w"),
            "jweek_day_en_short": jdate.strftime("%a"),
            "jweek_day_en": jdate.strftime("%A"),
            "jmonth_en": jdate.strftime("%b"),
            "jmonth_en_short": jdate.strftime("%B"),
            "jweek_day_fa_short": jdate.strftime("%a", locale="fa"),
            "jweek_day_fa": jdate.strftime("%A", locale="fa"),
            "jmonth_fa": jdate.strftime("%b", locale="fa"),
            "jmonth_fa_short": jdate.strftime("%B", locale="fa"),

            "week_day": date.strftime("%w"),
            "week_day_en_short": date.strftime("%a"),
            "week_day_en": date.strftime("%A"),
            "month_en": date.strftime("%b"),
            "month_en_short": date.strftime("%B"),
        }

        return date_time


if __name__ == "__main__":
    dateTime = DateTime()
    print(dateTime.get_date_time())
