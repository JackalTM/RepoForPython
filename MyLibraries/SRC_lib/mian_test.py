import re as RegExp

text1 = "20.6.2024 7:4:12 Error-free-Cycle finished, Cycle Nr.0 , Processed Time: 0h0min , pData[1]: 26 , pData[2]: 26 , pData[3]: 0 , pData[4]: 0"
text2 = "20.6.2024 7:22:55 Error-free-Cycle finished, Cycle Nr.12 , Processed Time: 0h18min , pData[1]: 26 , pData[2]: 26 , pData[3]: 0 , pData[4]: 0"

class FindFromPattern:

    RE_PATTERN_DATA =  RegExp.compile(r"^\d{1,2}\.\d{1,2}\.\d{2,4}")
    RE_PATTERN_CURRTIME =  RegExp.compile(r"(?:[1-9]|[0-9]|2[0-3]):[1-5]?[0-9]:[1-5]?[0-9]")
    RE_PATTERN_CYCL_NUM = RegExp.compile(r"Nr.(?:[0-9]|2[0-9])")
    RE_PATTERN_CYCLETIME = RegExp.compile(r"(?:[1-9]|[0-9]|2[0-3])h[1-5]?[0-9]min")


    def __init__(self) -> None:
        self.patternDataFound = False
        self.patternTimeFound = False
        self.patternCycleFound = False
        self.patternDataFound = False
        return None
#**********************************************************************************************
    def FindPatternData(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_DATA.match(someStr)
        return tempStr
    
    def FindPatternCurrTime(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CURRTIME.search(someStr)
        return tempStr
    
    def FindPatternCyclAmount(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CYCL_NUM.search(someStr)
        return tempStr
    
    def FindPatternCyclTime(self, someStr : str)->str:
        tempStr = self.RE_PATTERN_CYCLETIME.search(someStr)
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

if __name__ == "__main__":
    instFind = FindFromPattern()

    print("Text before {}".format(text1))
    text1 = instFind.ReplacePatternData( "d.m.yyyy",text1)
    text1 = instFind.ReplacePatternCurrTime( "h.m.ss",text1)
    text1 = instFind.ReplacePatternCyclAmount( "Nr.69",text1)
    text1 = instFind.ReplacePatternCyclTime("20h50min",text1)
    print("Text after  {}".format(text1))

else:
    print("ERROR INDIRECT CALL!!!")
    # Do nothing beacuse run indirectly





