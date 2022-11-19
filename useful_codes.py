import time
from os.path import isfile
from csv import DictReader
from threading import Thread

class basic_operate:
    def loop(loop_times:int,target:object):
        if loop_times != 0 and loop_times > 1:
            for i in loop_times:
                target
        elif loop_times == 0:
            i = 2
            while i > 1:
                target
    def UseMutiTread(target:object):
        s = Thread(target=target)
        s.start
        s.join

        
class file_operate:
    def check_file_exist(path:str):
        return isfile(path=path)
    
    def add_file(path:str):
        open(path,mode="x").close
    
    def read_file_by_line(filepath:str):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = [_.rstrip('\n') for _ in f]
            return content
        
class readcsv:
    def ReadcsvToList(CsvPath:str,WantToReadLine:str):
        file = open(file=CsvPath,mode="r")
        raw_data = DictReader(file)
        data = []
        for readdata in raw_data:
            data.append(readdata[WantToReadLine])
        return data