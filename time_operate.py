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
        year,month,day,hour,minute,seconds,microseconds\n
        (this is your location time)
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
    
    def getlocaltime(times:list[str],gettime:int,delaytime:int,comma:str):
        """
        it can get your location's time\n
        datetime.now()s is get how many times time\n
        and delaytime is delay between get time\n
        if comma is / it will look like 2002/1/1
        """
        i = 0
        a = 0
        returntime = ""

        while i <= gettime:
            time.sleep(delaytime)
            while a <= len(times):
                if "year" in times:
                    returntime = returntime + str(datetime.now().year()) + comma
                elif "month" in times:
                    returntime = returntime + str(datetime.now().month()) + comma
                elif "day" in times:
                    returntime = returntime + str(datetime.now().day()) + comma
                elif "hour" in times:
                    returntime = returntime + str(datetime.now().hour()) + comma
                elif "minute" in times:
                    returntime = returntime + str(datetime.now().minute()) + comma
                elif "second" in time:
                    returntime = returntime + str(datetime.now().second()) + comma
                elif "microsecond" in time:
                    returntime = returntime + str(datetime.now().microsecond()) + comma
            return returntime