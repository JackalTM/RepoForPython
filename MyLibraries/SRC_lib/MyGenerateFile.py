import re as RegExp
import os

'''*********************************************************************************************
* Class to generate file
'''
class GenerateTextFile:
    IDX_HOUR = 0
    IDX_MIN = 1
    IDX_SEC = 2

    CYCLE_TIME_TUPLET = (91, 92, 92, 93, 93, 94, 95)
#***********************************************************************************************
    def __init__(self, fileName : str, strData : str, hourStart : int, minStart : int, secStart : int) -> None:
        self.filename = fileName
        self.strData = strData
        self.hourstart = hourStart
        self.minstart = minStart
        self.senstart = secStart

        self.sec_started = secStart + (60 * minStart) + (3600 * hourStart)
        self.sec_left = self.sec_started
        self.cycle_amount = 0

        self.tuple_idx = 0
        return
#==============================================================================================
#**********************************************************************************************
    def __INTERN_SecondsToTime(self, secAmount : int)->list:
        hours = int(secAmount / 3600)
        minutes = int(secAmount / 60)
        minutes = minutes - int(secAmount % 3600)
        seconds = secAmount - (secAmount % 60)
        timeList = [hours, minutes, seconds]
        return timeList

#**********************************************************************************************
    def IncTime(self, incSecAmount : int) -> list:
        self.cycle_amount = self.cycle_amount + 1
        self.sec_left += incSecAmount
        return self.__INTERN_SecondsToTime(self.sec_left)
#==============================================================================================        

#**********************************************************************************************
    def CreateTimeString(self, timeList : list) -> str:
        timeString = "Processed Time: {}h{}min".format(timeList[self.IDX_HOUR], timeList[self.IDX_MIN])
        return timeString
#==============================================================================================

#**********************************************************************************************
    def CreateTimeString(self, timeList : list) -> str:
        timeString = "Processed Time: {}h{}min".format(timeList[self.IDX_HOUR], timeList[self.IDX_MIN])
        return timeString
#==============================================================================================

    def CreateCol_Number1(self) -> str:
        tempStr = "{} {} {}, ".format(self.strData, self)
        return 

#**********************************************************************************************
    def CALL_IncrementeTime(self):
        if(self.tuple_idx < len(self.CYCLE_TIME_TUPLET)):
            i = self.CYCLE_TIME_TUPLET[self.tuple_idx]
            self.tuple_idx += 1
        else:
            self.tuple_idx = 0
            i = self.CYCLE_TIME_TUPLET[self.tuple_idx]

#==============================================================================================
        
#**********************************************************************************************
def CALL_test() -> None:
    instGenetare = GenerateTextFile("someFile", 7, 00, 00)
    
    for i in range(0, 10):
        timestr = instGenetare.CreateTimeString(instGenetare.IncCycleAndTime(60))
        print(timestr)

    return
#===============================================================================

if(__name__ == "__main__"):
    CALL_test()
else:
    pass