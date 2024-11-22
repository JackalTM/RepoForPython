import datetime as dt
'''******************************************************************************************
@name   MilionDays1
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
def CALL_MilionDays_Iterator()->None:
    myMilionDays = MilionDays_Iterator(2000, 1, 1, 10)

    print(next(myMilionDays))
    print(next(myMilionDays))
    print(next(myMilionDays))
    print(next(myMilionDays))

    myMilionDays = MilionDays_Iterator(2000, 1, 1, 4)
    # Nie może być wykożystany!
    # Błąd klasa nie jest generatorem!
    for d in myMilionDays:
        print(d)

    return None
#==============================================================================================

'''******************************************************************************************
@name   MilionDays_Iterator_Generator
@breif  Klasa stworzona jako iterator dla daty oraz dni
        Klasa została rozbudowana i teraz można wykorzystać pętlę for 
'''
class MilionDays_IteratorIterable():
    """To jest klasa która jest iterowana oraz jest iteratorem"""
    def __init__(self, year:int, month:int, day:int, maxDays:int):
        self.date:dt.date    = dt.date(year, month, day)
        self.__maxDays = maxDays
        self.__i_days = 0
        return None
    #--------------------------------------------------------
    '''
    @brief  Ta metoda pozwala pobierać kolejne elementy z tej klasy
    '''
    def __next__(self):
    # Określanie końca generowania dani
        if(self.__i_days < self.__maxDays):
            self.__i_days = self.__i_days + 1
            returnData = self.date
            self.date = self.date + dt.timedelta(days=1)
        else: # Określanie kiedy generowanie ma sie zakończyć
            raise StopIteration() # Wyjątek do zakonczenia generowania 
        
        return returnData
    #--------------------------------------------------------
    '''
    @brief  Aby działala funkcja for należy dodac ta metode
    @note   Dla klasy Iterable zwracane jest self. Klasa jest swoim własnym iteratorem
    '''
    def __iter__(self):
        return self
    #--------------------------------------------------------
    def __str__(self) -> str:
        return ">> {}-{}-{} <<".format(self.date.year, self.date.month, self.date.day)
    #--------------------------------------------------------
#==============================================================================================
def CALL_MilionDays_IteratorIterable()->None:
    myMilionDays = MilionDays_IteratorIterable(2024, 1, 1, 4)
    for d in myMilionDays:
        print(d)

    return None
#==============================================================================================

if(__name__ == ("__main__")):
    CALL_MilionDays_IteratorIterable()
else:
    pass