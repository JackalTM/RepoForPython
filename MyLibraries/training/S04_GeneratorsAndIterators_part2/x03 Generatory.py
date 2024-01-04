import datetime as dt

def MyGeneratorLike22(instart, inEnd):
    current = instart
    while(current < inEnd):
        yield current
        current += 1

class MilionDays():
    """
    Klasa która jest iteratorem
    posiada matody next oraz iter
    """
    def __init__(self, iYear, iMonth, iDay, iMaxdays):
        self.date   = dt.date(iYear, iMonth, iDay)
        self.maxDays= iMaxdays
        return None

    def __next__(self):
        if(self.maxDays <= 0):
            raise StopIteration

        value = self
        self.date = self.date + dt.timedelta(days= 1)
        self.maxDays = self.maxDays - 1
        return value

def MilionDays(iYear, iMonth, iDay, iMaxdays):
    """
    #Generator to funkcja
    #Metoda 'yiedl' zamraża funkcja zwrca dalej wartosci
    """
    date = dt.date(iYear, iMonth, iDay)

    for i in range(iMaxdays):
        value = date + dt.timedelta(days= i)
        yield value

def CallGenerators1():

    for day in MilionDays(2021, 3, 1, 5):
        print(day)

    return None

