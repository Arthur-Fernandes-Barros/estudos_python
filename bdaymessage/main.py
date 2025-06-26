import datetime 
import bday_message

today = datetime.date.today()

next_birthday = datetime.date(2025,6,26)

days_away =   next_birthday - today

if today == next_birthday:
    print(bday_message.radom_message)
else:
    print(f"My next birthday is {days_away} days away!")

