import datetime as dt

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
#==================================================================================
def MilionDays(iYear, iMonth, iDay, iMaxdays):
    """
    #Generator to funkcja
    #Metoda 'yiedl' zamraża funkcja zwrca dalej wartosci
    """
    date = dt.date(iYear, iMonth, iDay)

    for i in range(iMaxdays):
        value = date + dt.timedelta(days= i)
        yield value
#==================================================================================
def Combinations(listA, listB, listC):
    """
    Funkcja która jest generatorem.
    Kolejno zwracane są elemanty
    """
    if(type(listA) == list)and(type(listB) == list)and(type(listC) == list):
        pass
    else:
        return None

    for a in listA:
        for b in listB:
            for c in listC:
                t = ("{} - {} - {}".format(a, b, c))
                yield t
#==================================================================================
def main():

    for day in MilionDays(2021, 3, 1, 5):
        print(day)

    print("================================")

    products = ["Product {}".format(i) for i in range(1, 4)]
    promotions = ["Promotion {}".format(i) for i in range(1, 3)]
    customers = ['Customer {}'.format(i) for i in range(1, 5)]

    for c in Combinations(products, promotions, customers):
        print(c)

    return None
#==================================================================================
main()
