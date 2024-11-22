import itertools as it
import operator as op

'''
Funkcje przydatne jesli chcemy przeprowadzac analize danych czy podobne
'''
def Itertools_operator_mul():
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    res = it.accumulate(data, op.mul)
    for i in res:
        print(i)

    return None

def Itertools_write_all_methods():
    File = open("Metody_modulu_operator.txt", 'w')
    File.write("Empty")
    File.close()

    File = open("Metody_modulu_operator.txt", 'a')

    File.write("wszystkie metody dla modułu operator")
    File.write('\n')
    for i in dir(op):
        if(i[:2] == '__'):
            File.write('- {} {}'.format(i,'\n'))

    File.close()

    return None

def Itertools_count():
    '''
    Co ile powiększac kolejne wartosci zaczynając od
    '''
    for i in it.count(10,3):
        if(i > 20):
            break
        else:
            print(i)
    return None

def Itertoold_cycle():
    '''
    Nieskonczona petla miedzy elemantami z obiektu iterable
    '''
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in months:
        print(i)

def Itertools_chain():
    '''
    Zwraca kolejne elemanty z listy1 oraz nastepnie z listy2
    '''
    color1 = ['red','yellow','blue']
    color2 = ['green','orange','violet']
    resoult = it.chain(color1, color2)
    for i in resoult:
        print(i)

    return None

def Itertools_compress():
    '''
    Wybiera elemanty z list1 gdzie na list2 jest wartośc True
    '''
    cars = ['Ford','Opel','Toyota','Skoda']
    sel = [True,False,True,False]
    resoult = it.compress(cars, sel)
    for i in resoult:
        print(i)

    return None

def Itertools_dropwhile():
    '''
    Zwraca elemanty jesli został spełniony pierwszy argument
    Jednak robi to potem nawet jesli juz argumenty nie spełniaja
    '''
    F = (lambda x: x < 5)
    data = (0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x00)
    # resoult = F1(F,data) -> F1(F(data))
    resoult = it.dropwhile(F, data)
    for i in resoult:
        print(i)

    return None

def Itertools_filterfalse():
    '''
    Filtruje jesi element nie spełnia wymagania
    '''
    F       = (lambda x: x < 5)
    data    = (0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x00)
    resoult = it.filterfalse(F, data)
    for i in resoult:
        print(i)

    return None

def Itertools_islice():
    '''
    Robi wycinek dla elemantu iterrable dla pomiedzy
    '''
    months  = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    resoult = it.islice(months, 6, 8)
    for i in resoult:
        print(i)

    return None

def Itertools_products():
    '''
    Jest to iloczyn kartezianski
    Parowanie elematów
    '''
    spades  = ['Hearts','Tiles','Clovers','Pikes']
    figures = ['Ace','King','Queen','Jack','10','09']
    resoult = it.product(spades, figures)
    for i in resoult:
        print(i)

    return None

def Itertools_repeat():
    '''
    Funkcja ta powtarza w nieskonczonosc kolejne elemanty
    Powtarzanie wywoływanie fukcji czy klasy
    '''
    for i in it.repeat("Infinity", 5):
        print(i)

    return None

def Itertools_starmap():
    '''
    Robi cos na specyficznym obiekcie powiedzmy dodaje
    '''
    data    = [(1,2), (3,4), (5,6)]
    resoult = it.starmap(op.add, data)
    for i in resoult:
        print(i)

    return None

def Itertools_takwwwhile():
    '''
    Opozycja do fukkcji dropwhile
    Zostawia te akdumenty które spełniają warunek
    '''
    F       = (lambda x: x < 5)
    data    = (0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x00)
    resoult = it.takewhile(F, data)
    for i in resoult:
        print(i)

    return None

def Itertools_tee():
    '''
    Funkcka tworzy iteratory z podanej listy lub iteratora
    Sa to niezalezne iteratory
    Podajamy w argumencje ilosc tych iteratorów
    '''
    cars = ['Ford','Opel','Toyota','Skoda']
    cars1, cars2 = it.tee(cars, 2)

    for i in cars1:
        print(i)

    for j in cars2:
        print(j)

    return None

def Itertools_zip_longest():
    '''
    Doposowuje elemanty jesli nie odpowiada to daje wartosc fillvalue
    Jesli listy nie maja takich samych długosci
    '''
    months  = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plan    = ['busy','busy','busy','busy','busy','busy','free','free']
    resoult = it.zip_longest(months, plan, fillvalue = 'unknown')
    for i in resoult:
        print(i)

    return None

def PerfectNumbers(F, x):
    pass

def GetFactor(x):
    retList = []
    for i in range(1, x):
        if (x % i == 0):
            retList.append(i)
    return retList

def main():

    #Itertools_count()
    #Itertoold_cycle()
    #Itertools_chain()
    #Itertools_compress()
    #Itertools_dropwhile()
    #Itertools_filterfalse()
    #Itertools_islice()
    #Itertools_products()
    #Itertools_repeat()
    #Itertools_starmap()
    #Itertools_takwwwhile()
    #Itertools_tee()
    #Itertools_zip_longest()

    temp = GetFactor(20)
    print(temp)

    return None

main()
