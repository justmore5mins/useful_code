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
    
    def getallzones(returnornot:bool):
        for i in pytz.all_timezones:
            if returnornot == True:
                return i
            elif returnornot == False:
                print(i)
    
    def locationtime(location:str):
        """
        because the zones are too much,so if you want to see all zones,
        please you use the funtion getallzones
        """