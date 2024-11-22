import itertools
import operator

'''*********************************************************************************
@brief  wykonywanie obliczeen dla kolejnych elementach z listy razem
        Co należy wykonać jest przekazywane jako funkcja operator.mul ...
'''
def Itertools_Acumulate()->None:
    datalist = [1,2,3,4,5]
    acumResoult:list = itertools.accumulate(datalist, operator.mul)
    for i in acumResoult:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Generuje coraz wieksze liczby bo podany krok
'''
def Itertols_Count()->None:
    for i in itertools.count(10,3):
        if i < 20:
            print(i)
        else:
            break
#===================================================================================

'''*********************************************************************************
@brief  Przechodzi przez liste elementów kiedy lista się skonczy zaczyna od początku
        Ten cykl jest w nieskonczonośc
'''
def Itertools_Cycle()->None:
    days = ("pn","wt","sr","czw","pt","sob","nd")
    j = 0
    for i in itertools.cycle(days):
        if(j<14):
            print(i)
            j = j + 1
        else:
            break
#===================================================================================

'''*********************************************************************************
@brief  Łaczenie dwóch list w jeden obiekt chozi o obiekty Iterable[_T]
'''
def Itertools_Chain()->None:
    list1 = ["red","green", "blue"]
    list2 = ["orange", "violet", "yellow"]
    list_12 = itertools.chain(list1, list2)
    for i in list_12:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Zwracanie elementów z pierwszego argumentu gdzie w drugim argumencie jest True
@note   Każdy element w liscie który nie jest False lub zero None jest określany jako true
'''
def Itertools_Compress()->None:
    cars = ("Ford", "Opel", "Toyota", "Skoda")
    selections = (True, False, True, False)
    nums = (1,0,1,0)
    other = ("test", 0, "test", 0)

    resList = itertools.compress(cars, selections)
    for i in resList:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Tworzona jest nowa lista z listy wejsciowej.
        Elementy z listy sa pomijane do momenty kiedy warunek nie zostanie spełniony.
        Następnie reszta elemetów jest pobierana bez względu na warunek
@note   Często podawna jako funkcja lambda
'''
def Itertools_Dropwhile()->None:
    data = (0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9)
    extracted = itertools.dropwhile(lambda x: x<5, data)
    for i in extracted:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Tworzone jest nowa lista z listy wejsciowej.
        Elementy są dodawane na podstawnie argumentowej funkcji.
        W tym przypadku na podstawie warunku niespełnienia tego warunku.
        Wszystkie elementy są sprawdzanie bo jest to funkcja filter()
'''
def Itertools_filterfalse()->None:
    data = (0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9)
    extracted = itertools.filterfalse(lambda x: x<5, data)
    for i in extracted:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Tworzone jest nowa lista z listy wejsciowej.
        Elementy są dodawane na podstawnie argumentowej funkcji.
        W tym przypadku na podstawie warunku spełnienia tego warunku.
        Wszystkie elementy są sprawdzanie bo jest to funkcja filter()
'''
def Itertools_takewhile()->None:
    data = (0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9)
    extracted = itertools.takewhile(lambda x: x<5, data)
    for i in extracted:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Z listy wejsciowej sa wyseparowanie elementy na postawie przedziału.
        Numer elementu odności sie do wskaźnika wiec zaczyna sie od 0.
        Koniecjest podobnie jak w range(0,n) gdzie sprawdzaniy jest warunek i<n
'''
def Itertools_islice()->None:
    days = ("pn","wt","sr","czw","pt","sob","nd")
    extracted = itertools.islice(days, 3, 5)
    for i in extracted:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Tworzone kombinacje w tym wypadku dwu elementowe.
        Mozliwe kombinace tych wejscoiwych list lub tuple
        Obiekty wejscoiwe muszą być Iterable[_T2@__new__]
'''
def Itertools_product()->None:
    strLetters = ("AA","BB","CC","DD")
    strNumbers = ("11","22","33","44")

    combinatins = itertools.product(strLetters, strNumbers)
    for i in combinatins:
        print(i)
#===================================================================================

'''*********************************************************************************
@brief Zwracjanie podanego obiektu zadaną ilośc razy lub w nieskonczonośc
'''
def Itertools_repeat()->None:
    for i in itertools.repeat("Ale jaja!!", 9):
        print(i)
#===================================================================================

'''*********************************************************************************
@brief  Na zadanym w specyficzny sposób obiekcie jako lista z tuple
        Wykonywane sa działa nie matematyczne.
        Przykłąd [(1,2), (3,4), (5,6)] = [3, 7, 11]
'''
def Itertools_starmap()->None:
    data = [(1,2), (3,4), (5,6)]
    res = itertools.starmap(operator.add, data)
    for i in res:
        print(i)
#===================================================================================

'''*********************************************************************************
@breif  Bazyjąc na bazowym Iterator tworzone sa nowe niezależne.
        Proste przypisanie tworzny tylko nową referencje a nie nowy obiekt.
        Domyślnie tworzone sa dwa nowe iteratory jednak może byćwięcej niz dwa
'''
def Itertools_tee()->None:
    days = ("pn","wt","sr","czw","pt","sob","nd")
    (days1, days2) = itertools.tee(days)
    for i in days1:
        print(i)
    else:
        print("--------")

    for i in days2:
        print(i)
    
#===================================================================================

'''*********************************************************************************
@brief  Tworzy listę z tuple z podanych dwóch list.
        Spina dwie listy w jedna z dwoma elementami.
        Jeśli jedna lista jest krótsza to wypełnianie jest argumentem fillvalue=
'''
def Itertools_zip_longest()->None:
    months = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    plan = ("busy", "busy", "busy", "busy", "busy", "free", "free")
    ziped = itertools.zip_longest(months, plan, fillvalue= "empty")
    for i in ziped:
        print(i)
#===================================================================================

if(__name__ == ("__main__")):
    Itertools_zip_longest()
else:
    pass