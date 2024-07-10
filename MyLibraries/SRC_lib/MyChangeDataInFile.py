import time as Time
import re as RegExp
import random as Random
from MyTimeConversion import myTimeConvert

'''*********************************************************************************************
* Class to generate file
'''
class ReplaceTextFile:

    RE_PATTERN_DATA =  RegExp.compile(r"^\d{1,2}\.\d{1,2}\.\d{2,4}\s")
    RE_PATTERN_CURRTIME =  RegExp.compile(r"(?:[1-9]|[0-9]|2[0-3]):[1-5]?[0-9]:[1-5]?[0-9]")
    #RE_PATTERN_CYCL_NUM = RegExp.compile(r"Nr.(?:[0-9]|2[0-9])")
    RE_PATTERN_CYCL_NUM = RegExp.compile(r"Nr.[0-9]*")
    RE_PATTERN_CYCLETIME = RegExp.compile(r"(?:[1-9]|[0-9]|2[0-3])h[1-5]?[0-9]min")

    CYCLE_TIME_TUPLET_SHORT = (95,96,94,100,96,93,96,93,100,97,97,92,99,91,94,84,88, 103, 101, 103, 95, 94)
    CYCLE_TIME_TUPLET_LONG = (1632, 1637, 1650, 1624, 1625, 1633, 1674, 1634, 1639, 1627, 1704)

    CYCLE_AMOUNT_LONG = 16
#***********************************************************************************************
    def __init__(self, dataList : tuple, hourStart : int, minStart : int, secStart : int, cycleNumStart : int, secondStarted : int)->None:
        self.year = dataList[0]
        self.month = dataList[1]
        self.day = dataList[2]
        self.dayLast = 0

        self.hourstart = hourStart
        self.minstart = minStart
        self.senstart = secStart

        self.secTimeStarted = secStart + (60 * minStart) + (3600 * hourStart)

        self.secActTime = self.secTimeStarted
        self.secFromBegin = secondStarted
        self.cycle_amount = cycleNumStart
        self.tuple_idx = 0
        return
#==============================================================================================
#**********************************************************************************************
    def FindPatternData(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_DATA.match(someStr)
        if(tempStr == None):
            return ""
        return tempStr
    
    def FindPatternCurrTime(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CURRTIME.search(someStr)
        if(tempStr == None):
            return ""
        return tempStr
    
    def FindPatternCyclAmount(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CYCL_NUM.search(someStr)
        if(tempStr == None):
            return ""
        return tempStr
    
    def FindPatternCyclTime(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CYCLETIME.search(someStr)
        if(tempStr == None):
            return ""
        return tempStr
#==============================================================================================
#**********************************************************************************************
    def ReplacePatternData(self, stringNew, stringLine : str)->str:
        tempStr = self.RE_PATTERN_DATA.sub(stringNew, stringLine)
        return tempStr
    
    def ReplacePatternCurrTime(self, stringNew, stringLine : str)->str:
        tempStr = self.RE_PATTERN_CURRTIME.sub(stringNew, stringLine)
        return tempStr
    
    def ReplacePatternCyclAmount(self, stringNew, stringLine : str)->str:
        tempStr = self.RE_PATTERN_CYCL_NUM.sub(stringNew, stringLine)
        return tempStr
    
    def ReplacePatternCyclTime(self, stringNew, stringLine : str)->str:
        tempStr = self.RE_PATTERN_CYCLETIME.sub(stringNew, stringLine)
        return tempStr
#==============================================================================================
#**********************************************************************************************
    def Action_IncTimeByValue(self) -> None:
        self.cycle_amount += 1

        if(self.cycle_amount % self.CYCLE_AMOUNT_LONG):
            secAmount = Random.choice(self.CYCLE_TIME_TUPLET_SHORT)
        else:
            secAmount = Random.choice(self.CYCLE_TIME_TUPLET_LONG)

        self.secActTime += secAmount
        self.secFromBegin += secAmount
        return        
#==============================================================================================
#**********************************************************************************************
    def GetData(self)->tuple:
        (day, hour, minute, second)= myTimeConvert.SecondsToTime_d_h_m_s(self.secActTime)
        if(day > self.dayLast):
            self.day += 1
            self.dayLast
        else:
            pass
        return ("{}.{}.{}".format(self.year, self.month, day), "{}:{}:{}".format(hour, minute, second))
    
    def GetCyclAmount(self)->str:
        return ("Nr.{}".format(self.cycle_amount))
    
    def GetCyclTime(self)->str:
        (hour, minute, second) = myTimeConvert.SecondsToTime_h_m_s(self.secFromBegin)
        return ("{}h{}min".format(hour, minute))
#==============================================================================================

#**********************************************************************************************
def ReplaceFileEntries()->bool:
    dataList = (2024, 6, 22)
    hour = 7
    minute = 00
    second = 00

    fromCycle = 0
    fromSecond = (0 * 60 * 60) + (32 * 60)

    instGenetare = ReplaceTextFile(dataList, hour, minute, second, fromCycle, fromSecond)

    mainDir = "C:/_Projekty_/__GM__/GM7159 Ford impregnation line 2/x07_ExportFiles/DryrunLog/"
    srcFile = "Log_File_6_20_2024_Run_1.txt"
    destFile = "_Log_File_6_20_2024_Run_1.txt"

    SourceFile = open(mainDir+srcFile, "r")
    DestinFile = open(mainDir+destFile, "w")

    for line in SourceFile:
        if(instGenetare.FindPatternData(line)):
            (el1, el2) = instGenetare.GetData()
            newLine = instGenetare.ReplacePatternData(el1, line)
            newLine = instGenetare.ReplacePatternCurrTime(el2, newLine)

            el1 = instGenetare.GetCyclAmount()
            newLine = instGenetare.ReplacePatternCyclAmount(el1, newLine)

            el2 = instGenetare.GetCyclTime()
            newLine = instGenetare.ReplacePatternCyclTime(el2, newLine)

            instGenetare.Action_IncTimeByValue()

            DestinFile.write(newLine)
        else:
            DestinFile.write(line)

    SourceFile.close()
    DestinFile.close()

    return True
#==============================================================================================

#===============================================================================
if(__name__ == "__main__"):
    ReplaceFileEntries()
else:
    pass
#===============================================================================