import datetime as dt

'''******************************************************************************************
@name   MilionDays_Iterator
@breif  Klasa stworzona jako iterator dla daty oraz dni
        W obecnej postaci nie może byc wykorzystane w pętli for 
'''
class MilionDays_Iterator():
    """To jest klasa która jest iterowana oraz jest iteratorem"""
    def __init__(self, year:int, month:int, day:int, maxDays:int):
        self.date:dt.date    = dt.date(year, month, day)
        self.__maxDays = maxDays
        self.__i_days = 0
        return None
    #--------------------------------------------------------
    '''******************************************************
    @brief  Klasa jest iterowana mozna urzywac pętlę for
    '''
    def __next__(self):
        if(self.__i_days < self.__maxDays):
            self.__i_days = self.__i_days + 1
            returnData = self.date

            self.date = self.date + dt.timedelta(days=1)
        else:
            raise StopIteration()
        
        return returnData
    #--------------------------------------------------------
    #@brief Dla klasy 
    def __str__(self) -> str:
        return ">> {}-{}-{} <<".format(self.date.year, self.date.month, self.date.day)
    #--------------------------------------------------------
#==============================================================================================

'''******************************************************************************************
@name   MilionDays_IterableWidhoutIterator
@breif  Klasa stworzona jako iterator dla daty oraz dni
        Klasa Iterowana bez iteratora
'''
class MilionDays_IterableWidhoutIterator():
    """To jest klasa która jest iterowana oraz jest iteratorem"""
    def __init__(self, year:int, month:int, day:int, maxDays:int):
        self.date:dt.date    = dt.date(year, month, day)
        self.__maxDays = maxDays
        self.__i_days = 0
        # przypisać mozna zewnętrzny iterator
        self.Externaliterator = MilionDays_Iterator(year, month, day, maxDays)
        return None
    #--------------------------------------------------------
    '''******************************************************
    @brief  W klasie MilionDays_Iterator nie jest zawarta ta metoda
            Tutaj jets połączenie obu klas
    '''
    def __iter__(self)->MilionDays_Iterator:
        return self.Externaliterator
    #--------------------------------------------------------
    def __str__(self) -> str:
        return ">> {}-{}-{} <<".format(self.date.year, self.date.month, self.date.day)
    #--------------------------------------------------------
#==============================================================================================
def CALL_Test1()->None:
    myMD = MilionDays_IterableWidhoutIterator(2024, 1, 1, 30)
    for i in myMD:
        print(i)
    return
#------------------------------------------------------------
def CALL_Test2()->None:
    myMD = MilionDays_IterableWidhoutIterator(2024, 1, 1, 30)
    #Metoda next tutaj nie działa bo nie jest zaimplementowana
    for i in range(0,8):
        print(next(iter(myMD)))
    return
#==============================================================================================

if(__name__ == "__main__"):
    CALL_Test2()
else:
    pass