from Speak import speak
import datetime
from num2words import num2words

def run_date(input):
    if input.find("date") != -1 or input.find("day") != -1:
        today = datetime.datetime.now()
        day = today.strftime('%A')
        month = today.strftime('%B')
        year = today.strftime('%Y')
        date_str = "today's date is " + day + ' ' + month + ' ' + year
        speak(date_str)
        return True
    if input.find("time") != -1:
        today = datetime.datetime.now()
        hour = num2words(today.strftime('%I'))
        minute = num2words(today.strftime('%M'))
        time_str = "it is " + hour + ' ' + minute
        speak(time_str)
        return True
    