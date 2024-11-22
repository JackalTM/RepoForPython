import re 

'''**************************************************************************
@name       FilterFromFile_Generator
@brief      Generator that filter ALARM message
@param[in]  mainDir - Main direction to folder
@param[in]  fileName - Name of file to open
'''
def FilterFromFile_Generator_v1(fillDir:str,  patternStr:str)->any:
    myRe = re.compile(patternStr)

    print(">> File open: ")
    myFile = open(fillDir)

    for line in myFile:
        tList = myRe.split(line)
        if(len(tList) > 1):
            tStr:str = tList[1]
            yield tStr.replace('\n','')

    myFile.close()
    print(">> File close: ")
#============================================================================
'''**************************************************************************
@name       FilterFromFile_Generator
@brief      Generator that filter ALARM message
@param[in]  mainDir - Main direction to folder
@param[in]  fileName - Name of file to open
'''
def FilterFromFile_Generator_v2(fillDir:str, refPatternRE:re.Pattern)->any:

    print(">> File open: ")
    myFile = open(fillDir)

    for line in myFile:
        tList = refPatternRE.split(line)
        if(len(tList) > 1):
            tStr:str = tList[1]
            yield tStr.replace('\n','')

    myFile.close()
    print(">> File close: ")
#============================================================================
def CALL_OpenFilestandard_v1():
    fullDirection = "E:/Dokumenty/testFiles/Generator-Strumien.txt"
    for i in  FilterFromFile_Generator_v1(fullDirection, "ALARM: "):
        print(i)
#-----------------------------------------------------------------------------
def CALL_OpenFilestandard_v2():

    fullDirection = "E:/Dokumenty/testFiles/Generator-Strumien.txt"

    for i in  FilterFromFile_Generator_v2(fullDirection, re.compile("ALARM: ")):
        print(i)
#============================================================================

if(__name__ == ("__main__")):
    CALL_OpenFilestandard_v2()
else:
    pass