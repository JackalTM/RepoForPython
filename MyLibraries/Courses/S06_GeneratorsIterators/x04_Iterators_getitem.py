import datetime as myDateTime

'''****************************************************************************************
@Name   MilionDays
@brief  Klasa przykładowa dla metody __getitem__()
'''
class MilionDays_getitems:

    def __init__(self, year:int= 0, month:int= 0, day:int= 0, maxDays:int= 0)->None:
        self.date = myDateTime.datetime(year, month, day)
        self.maxDays = maxDays
        return None
    
    #------------------------------------------------------------------
    # @brief    Mozna urzywac instacji jako instMiliondays[i:int]
    def __getitem__(self, item:int)->int:
        if(item < self.maxDays):
            return (self.date + myDateTime.timedelta(days= item))
        else:
            raise StopIteration()
    #------------------------------------------------------------------

#==========================================================================================
def CALL_MilionDays_getitem()->None:
    myDays = MilionDays_getitems(2024, 8, 1, 7)

    # Należy zdefinionwć: __getitem__()
    for i in range(0, 4):
        print(myDays[i])
    print("****************")

    # Zdfiniowany zewnętrzny iterator
    myIter = iter(myDays)
    print("next( ):= ", next(myIter))
    print("next( ):= ", next(myIter))
    print("next( ):= ", next(myIter))
    print("****************")

    # Metoda __getitem__() działa rownież dla przejscia pętlą for
    for i in myDays:
        print("i:= ", i)

    return None
#==========================================================================================

if(__name__ == ("__main__")):
    CALL_MilionDays_getitem()
else:
    pass