'''******************************************************************
@name       OpenFile
@brief      Open a certain file 
@parameter  inCD - String Cd to file
@note       void 
@return     None
'''
def OpenFile(inCD= "file.csv", openOrEdit= 'R'):
    print("File {} is opened".format(inCD), end= '\n')

    def _OpenLine(lineNUmber= 0):
        tStr = " -> Line {} in file is opened".format(lineNUmber)
        return tStr

    def _EditLine(lineNUmber= 0):
        tStr = " -> Line {} in file is edited".format(lineNUmber)
        return tStr

    if(openOrEdit == 'R'):
        return _OpenLine
    elif(openOrEdit == 'W'):
        return _EditLine
#====================================================================
def CALL_ReturnFunctionFromFunction():
    OpenLine = OpenFile()
    print("===============")
    print(OpenLine())
#====================================================================
    

'''******************************************************************
@name       CompareData
@brief      Compare input data 
@parameter  inData1 - data to compare 
@parameter  inData2 - data to compare
@note       Acording to data type special meyhod is used
@return     None
'''
def CompareData(inData1, inData2):
    if type(inData1) == int and type(inData2) == int:
        if(inData1 > inData2):
            return inData1
        else:
            return inData2
    elif type(inData1) == float and type(inData2) == float:
        if(inData1 > inData2):
            return inData1
        else:
            return inData2
    else:
        return None
#====================================================================
'''******************************************************************
@name       QuickSort
@brief      Sort input data wwith Quick sort agloritm
@parameter  inData1 - data to compare 
@parameter  inData2 - data to compare
@parameter  CompareMethod - Comparte method for object in data input
@note       void 
@return     None
'''
def QuickSort(inData1, inData2, DataCompareMethod):
    try:
        resoult = DataCompareMethod(inData1, inData2)
    except:
        print("Input method wrong")
        resoult = None

    return resoult
#====================================================================
def CALL_FunctioAsArgument():
    cmpResoult = QuickSort(0xFF, 0xFFF, CompareData)
    print("Resoult is {}".format(hex(cmpResoult)))
#====================================================================
    
'''******************************************************************
@name       OpenFileFrom
@brief      Function that will be decorated with other functionality 
@parameter  inCD - Directory to file 
@note       This is standard method 
@return     None
'''
def OpenFileFrom_v1(inCD):
    print("Function OpenFileFrom_v1() is called")
    print("File {} is opened!".format(inCD))
#====================================================================   
'''******************************************************************
@name       NewDeocrator
@brief      New functionality is created from 
@parameter  FunOriginal - Function to decorate with other functionality
@note       This is wrape funtions
@return     New wraped funtion
'''
def NewDeocrator(FunOriginal):

    def WrapFunction(inCD):
        print("File is beging procesed...")
        FunOriginal(inCD)
        print("File is read!")

    return WrapFunction
#====================================================================
'''******************************************************************
@name       OpenFileFrom_v2
@brief      Function that will be decorated with other functionality 
@parameter  inCD - Directory to file 
@note       This is syntax method
@return     None
'''
@NewDeocrator
def OpenFileFrom_v2(inCD):
    print("Function OpenFileFrom_v2() is called")
    print("File {} is opened!".format(inCD))
#==================================================================== 
def CALL_DecoratorFunction():
    someCD = "file.csv"

    #Standard call
    FullFunction = NewDeocrator(OpenFileFrom_v1)
    FullFunction(someCD)

    print('\n')
    #Syntax call
    OpenFileFrom_v2(someCD)
#====================================================================
def CALL_DecoratorFunctionSpecialSyntax():
    pass
#====================================================================