import time
from datetime import datetime
import pytz

class timers:
    def stopwatch():
        return time.perf_counter()
    def timer(stoptime:float):
        time.sleep(stoptime)
        return True
class world_time:
    def nowtime(get_times:int,delaytime:float):
        """
        you can get these times:\n
        year,month,day,hour,minute,seconds,microseconds

        all letter must be small type
        """

        for i in range(0,get_times):
            nowtime = datetime.now()
            timelist = []
            get_times += 1
            timelist.append(nowtime.year)
            timelist.append(nowtime.month)
            timelist.append(nowtime.day)
            timelist.append(nowtime.hour)
            timelist.append(nowtime.minute)
            timelist.append(nowtime.second)
            timelist.append(nowtime.microsecond)
            return timelist
        time.sleep(delaytime)
    def locationtime():
        """
            Because of the zones are too many, it can't print
            all zone in terminal,so use the csv to save it
        """
        open("zones.csv","x").close
        file = open("zones.csv","a")
        for i in pytz.all_timezones:
            pass