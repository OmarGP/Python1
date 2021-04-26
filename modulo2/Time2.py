from datetime import datetime, timedelta
from pytz import timezone
import pytz

#print(pytz.all_timezones)
print(datetime.now(pytz.timezone('Asia/Tokio')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
print(datetime.now(pytz.timezone('UTC')))