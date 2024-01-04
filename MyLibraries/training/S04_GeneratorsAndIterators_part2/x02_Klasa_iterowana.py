import datetime as dt

class MilionDays1():
    """To jest klasa która jest iterowana oraz jest iteratorem"""
    def __init__(self, year, month, day, maxDays):
        self.date    = dt.date(year, month, day)
        self.maxDays = maxDays
        return None

    def __next__(self):
        if(self.maxDays <= 0):
            raise StopIteration()
        returnData      = self.date
        self.date       = self.date + dt.timedelta(days=1)
        self.maxDays    = self.maxDays - 1
        return returnData

    def __iter__(self):
        return self

class MilionDays2Iterator():
    """ To jest kalsa która jest iteratorem dla klasy ponizej"""
    def __init__(self, date, maxDays):
        self.date       = date
        self.maxDays    = maxDays
        return None

    def __next__(self):
        if(self.maxDays <= 0):
            raise StopIteration()
        returnData = self.date
        self.maxDays = self.maxDays - 1
        self.date = self.date + dt.timedelta(days= 1)
        return returnData

class MilionDays2():
    """To jest klasa która z zewnętrznym iteratorem"""
    def __init__(self, year, month, day, maxDays):
        self.date    = dt.date(year, month, day)
        self.maxDays = maxDays
        self.i       = MilionDays2Iterator(self.date, self.maxDays)
        return None

    def __iter__(self):
        return self.i

# Cwiczenia z kursu
class Combinations():
    def __init__(self, listProducts, listPromotions, listCustomers):
        self.listCustomers  = listCustomers
        self.listPromotions = listPromotions
        self.listProducts   = listProducts
        self.i   = 0
        self.j   = 0
        self.k   = 0
        return None

    def __next__(self):
        if(self.i >= len(self.listCustomers)):
            self.i = 0
            self.j = self.j + 1

        if(self.j >= len(self.listPromotions)):
            self.j = 0
            self.k = self.k + 1

        if(self.k >= len(self.listProducts)):
            self.k = 0
            raise StopIteration()

        itemToReturn    = "{} - {} - {}".format(self.listProducts[self.k], self.listPromotions[self.j], self.listCustomers[self.i])
        self.i = self.i + 1
        return itemToReturn

    def __iter__(self):
        return self

def main():
    # Tworzenie listwy przy urzyciu petli for tak zwane 'List comprehention'
    products    = ["Product {}".format(i) for i in range(1,4)]
    promotions  = ["Promotion {}".format(i) for  i in range(1,3)]
    customers   = ["Customer {}".format(i) for i in range(1,5)]

    instCombinations = Combinations(products, promotions, customers)

    for c in instCombinations:
        print(c)

    return None
main()
