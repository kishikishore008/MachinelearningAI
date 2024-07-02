import datetime
import pytz

utc_now = datetime.datetime.utcnow()
utc_offset=datetime.timedelta(hours=5,minutes=30)
current_time=utc_now+utc_offset

current_date=current_time.date()
print(current_time)