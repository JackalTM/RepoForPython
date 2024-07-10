import random as Random
import os
from MyTimeConversion import myTimeConvert
'''*********************************************************************************************
* Class to generate file
'''
class GenerateTextFile:
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
    def Action_IncTimeByValue(self) -> None:
        self.cycle_amount += 1
        
        if((self.cycle_amount) % self.CYCLE_AMOUNT_LONG):
            secAmount = Random.choice(self.CYCLE_TIME_TUPLET_SHORT)
        else:
            secAmount = Random.choice(self.CYCLE_TIME_TUPLET_LONG)

        self.secActTime += secAmount
        self.secFromBegin += secAmount
        return          
#==============================================================================================
#**********************************************************************************************
    def Gen_BeginOfFIle(self)-> str:
        title = "Project Data: GM7159/01-1100 OP2100.01 DryRun|Auto/No Fault|Cycle Complete" + '\n'
        title = title + "Process Data 1: 27, C " + '\n'
        title = title + "Process Data 2: 27, C " + '\n'
        title = title + "Process Data 3: 0, C " + '\n'
        title = title + "Process Data 4: 0, C " + '\n'
        return title
#==============================================================================================
#**********************************************************************************************
    def Gen_CycleStarted(self)-> str:
        #(hours, minutes, seconds) = self.__Method_SecondsToTime_h_m_s(self.secActTime)
        (hours, minutes, seconds) = myTimeConvert.SecondsToTime_h_m_s(self.secActTime)
        dataStr = "{}.{}.{}".format(self.day, self.month, self.year)
        timeText = "{}:{}:{}".format(hours, minutes, seconds)

        return "{} {} Start Of Cycling".format(dataStr, timeText)
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_1(self) -> str:
        #(days, hours, minutes, seconds) = self.__Method_SecondsToTime_d_h_m_s(self.secActTime)
        (days, hours, minutes, seconds) = myTimeConvert.SecondsToTime_d_h_m_s(self.secActTime)
        
        if(days > self.dayLast):
            self.dayLast = days
            self.day += 1

        dataStr = "{}.{}.{}".format(self.day, self.month, self.year)
        timeText = "{}:{}:{}".format(hours, minutes, seconds)

        return "{} {} Error-free-Cycle finished".format(dataStr, timeText) 
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_2(self) -> str:
        return "Cycle Nr.{}".format(self.cycle_amount) 
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_3(self) -> str:
        #(hours, minutes) = self.__Method_SecondsToTime_h_m(self.secFromBegin)
        (hours, minutes) = myTimeConvert.SecondsToTime_h_m(self.secFromBegin)
        return "Processed Time: {}h{}min".format(hours, minutes) 
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_4(self) -> str:
        return "pData[1]: 26"
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_5(self) -> str:
        return "pData[2]: 26"
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_6(self) -> str:
        return "pData[3]: 0"
#==============================================================================================
#**********************************************************************************************
    def Gen_CSV_Col_7(self) -> str:
        return "pData[4]: 0"
#==============================================================================================

#**********************************************************************************************
def GenerateFullFile()->bool:
    #------------------------------------------------------------------------------------------
    # Configuration
    dataList = (2024, 7, 10)
    hour = 7
    minute = 3
    second = 14

    fromCycle = 0
    cyclesAmount = 383
    fromSecond = (0 * 60 * 60) + (0 * 60)
    #===========================================================================================
    instGenetare = GenerateTextFile(dataList, hour, minute, second, fromCycle, fromSecond)
    fileCD = "E:/05_Pracowe/"
    fileCD = fileCD + "test.txt"
    #===========================================================================================
    myFile = open(fileCD, "w")
    print("File {} created or opened".format(fileCD))
    if(fromCycle == 0):
        myFile.write(instGenetare.Gen_BeginOfFIle())
        lineStr1 = instGenetare.Gen_CycleStarted()
        lineStr2 = instGenetare.Gen_CSV_Col_2()
        lineStr3 = instGenetare.Gen_CSV_Col_3()
        lineStr4 = instGenetare.Gen_CSV_Col_4()
        lineStr5 = instGenetare.Gen_CSV_Col_5()
        lineStr6 = instGenetare.Gen_CSV_Col_6()
        lineStr7 = instGenetare.Gen_CSV_Col_7()
        fullStr = "{}, {} , {} , {} , {} , {} , {}\n".format(lineStr1, lineStr2, lineStr3, lineStr4, lineStr5, lineStr6, lineStr7)
        myFile.write(fullStr)
    else:
        pass

    for i in range(0, cyclesAmount):
        instGenetare.Action_IncTimeByValue()

        lineStr1 = instGenetare.Gen_CSV_Col_1()
        lineStr2 = instGenetare.Gen_CSV_Col_2()
        lineStr3 = instGenetare.Gen_CSV_Col_3()
        lineStr4 = instGenetare.Gen_CSV_Col_4()
        lineStr5 = instGenetare.Gen_CSV_Col_5()
        lineStr6 = instGenetare.Gen_CSV_Col_6()
        lineStr7 = instGenetare.Gen_CSV_Col_7()

        fullStr = "{}, {} , {} , {} , {} , {} , {}\n".format(lineStr1, lineStr2, lineStr3, lineStr4, lineStr5, lineStr6, lineStr7)
        #print(fullStr, end= ' \t')
        myFile.write(fullStr)

    myFile.close()
    print("File {} closed".format(fileCD))

    return True
#==============================================================================================

#===============================================================================
if(__name__ == "__main__"):
    GenerateFullFile()
else:
    pass
#===============================================================================