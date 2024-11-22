import os

"""
/****************************************************************************************************************************************
*   What is PEP 8and why it is important
*/

PEP stands for Python Enhancement Proposal. It is an official design document providing information to the python community,
or describing a new feature for python or its processes. 
PEP is especialy important since it docuent the style guidlines for python code.
"""

#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*   Python is an interpretes language.
*/

Interpreter language si any programing language that executes its statements line by line. 
This means that source code of a Python is converted
into bytecode that is then executed by Python virtual machine
Python code is not required to be build and linked like C and C++.
Python code is faster to develope and slower that C or C++.
Dynamic typed languages need to have engine to run its code.
"""
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*   What is dynamic typed languages 
*/

Type referes to type  checking in programing language. IN a strongly types languages as Python "1" + 2 will resoult error coz type error 
these languages dont allow for type correction.

Static data types are checked beforer the execution.
Dynamic data types are check during execution.
"""
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*   How to print widhout newline in Python
*/
    print("Something") will and new line on the end

    print("Something", end = " ") add space on end of the line
"""
def CallPrintWidhoutNewLine( ):
    print("Something")
    print("Something")

    print("Something", end = " ")
    print("Something", end = " ")
    return None
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*   What are keywords in Python
*/
Special word reserved thaty have specyfic meaning. There eare 35 keywords
"""
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*   List all the build in data types in Python
*/
Text types      : str
Numerin types   : int, float, complex
Sequence types  : list, tuple, range
Mapping types   : dict
Set types       : set, frozenset
Boolean types   : bool
Binary types    : bytes, bytearray, memmryview
None types      : non types

it can be check by using type()
"""
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*  What are the differences between Pyhon arrays and list
*/

list 
    someList = [1, 2.2, "3", "456"]
    - Brackets, mutable, dont to be unique, diffrent data types
    - List are dynamic aclocated memory
    - can be nested list

arrays
    ned to be imported numpy packages or array module
    import array as arr
    someArray = arr.array('i', [1,2,3,4,5,6]) it means that integer 'i' data types are stored

    They are more eficient for numerical operations
"""
def CallListAndArrayDifference():
    import array as arr

    someArray = arr.array('i', [1,2,3,4,5,6])
    print(someArray)
    print(type(someArray))

    someList = [1, 2.2, "3", "456"]
    print(someList)
    print(type(someList))
    return None
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*  What is dictioary data types in Python
*/
It is unordered colaction of items. each of a dictionary has a key and value.
Dicationary elements are eccesed by key. Using indicators like index is not posible.
Types can by mixed
"""
def CallDictionaryTest():
    someDict = {
        'A' : 10,
        'B' : 20,
        'C' : 30 }
    res = someDict["A"] + someDict["B"] + someDict["C"]
    return None
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*  Consept of indexing in Python. Negative indexing

It a a special types of object on Python that it can be iterated over.
It can be easly achieved using for lops.
Object like list, tuples, sets dictionaries, strings, arrays are called inerables.

Indexing can acces individual withing iterable by their position
Negative indexing mean that -1 is last element

Consept of slicing:
"""
def CallSlicingExample():
    someList = [1,2,3,4,5,6,7,8,9]
    print(someList[0:2], end = " ")
    print(someList[3:6], end = " ") # From 3 to 6
    print(someList[7:], end = " ")  # From 7 to end 
    print(someList[:5], end = " ")  # Up to 5 
    print(someList[:], end = " ")   # Whole list 
    return None
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*  Diferences between list and tuples

    List are mutable
    Tuple are immutable

    Both are iterable
    List iteration is more time consuming
    Tuple iteration is much faster

    List is can perform operation like add emement and remvoe 
    Tuple is apropriate for accesing elements fast

    List consume more memory 
    Tuple are more memory eficient
"""
def CallListVsTuplets():
    someList    = [1,2,3,4,5,6,7,8,9]
    someTuple   = (1,2,3,4,5,6,7,8,9)

    print(" list:", end = '\n')
    for i in someList:
        print(i, end = " - ")

    print("\n tuple:", end = '\n')
    for i in someTuple:
        print(i, end = " - ")
    return None
#=======================================================================================================================================

"""
/****************************************************************************************************************************************
*  Functions in Python

"""
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_ShortConditionalInstructions
@brief      Some more methods for dictionaries
@param[in]  ...
@note       ... 
@return     ...
'''
def Call_ShortConditionalInstructions():

    bonusGranted = True

    price = 0xFF
    bonus = 0x20
    if(bonusGranted):
        price = price - bonus

    print("Normal if method, print = {}".format(price))

    price = 0xFF
    bonus = 0x20
    price -= bonus if bonusGranted else 0

    print("Short method if method, print = {}".format(price))

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_ElseInLoops
@brief      Else dla pętli jest wykonane tylko wtedy gdy break nie zostało wykonane
@param[in]  ...
@note       Zama nazwa jestmyląca gdyż tylko gdy pętla nie zostałą przerwana to instrukcja sie wykona
@return     ...
'''
def Call_ElseInLoops():

    instructions = ["Mukade Choro", "Centichor", "Elder Celipendre", "Hero Blast", "Serious punch", True]
    instructionsApproved = []

    for instr in instructions:
        if(instr == True):
            break

        print("Add instr: {}".format(instr))
        instructionsApproved.append(instr)

    else:#
        print("For break: ")

    print("Instr taken: ", instructionsApproved)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       ListAndRange
@brief      rane, list, slice
@param[in]  ...
@note       ...
@return     ...
'''
def ListAndRange():
    for i in range(0x00, 0xF):
        print("i= {}".format(i), end= '\n')

    # Tworzenie listy od 0 do 15
    list1 = list(range(0x0, 0x10))

    # Krojenie elementów
    print(list1[0x3:0x8])

    # Odwracanie listy bez początkowego
    print(list1[-1:0:-1])

    # Odwracanie listy całkowite
    print(list1[-1::-1])

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       EnumerateAndZip1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def EnumerateAndZip1():
    listofnumbers = [7,8,9,4,5,6,1,2,3]
    #Tworzone są tuplety z podanej listy gdzie każdy tuplet zawiera index
    enumnumbers = enumerate(listofnumbers)

    tList = list(enumnumbers)
    print("Enumerate: ", tList)
    for i,j in tList:
        print("idx= {}, value= {}".format(i,j))


    tList1 = [19,21,22,21,20,22]
    tList2 = [1,2,3,4,5,6]

    # zip spina dwie listy gdzie wynikiem można przekonwertować do listy.
    # Kolejnosc elementów to kolejnośc elementó w docelowym tuplecie
    zipmonthsDays = zip(tList1, tList2)
    listMonthsDays = list(zipmonthsDays)
    print(listMonthsDays)
    for i,j in listMonthsDays:
        print("Days= {}, Month= {}".format(i,j))


    #enumerate oraz zip dla elementów z dwóch list
    # Daltego enumerate and zip sa bardzo często urzywane dla pętli for
    for idx,(m,d) in enumerate(zip(tList1, tList2)):
        print("idx= ", idx, "month= ", m, "day= ", d, end='\n')

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       EnumerateAndZip2
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def EnumerateAndZip2():
    days = [19,21,22,21,20,22]
    months = [1,2,3,4,5,6]

    print("zip(): Method 1:")
    zipDaysMonths = zip(days, months)
    for i,j in zipDaysMonths:
        print("F1 - day= ", i, "month= ", j)
    else: # When loop end widhout break
        print(end='\n')

    print("zip(): Method 2:")
    for i,j in zip(days, months):
        print("F2 - day= ", i, "month= ", j)
    else: # When loop end widhout break
        print(end='\n')

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       EnumerateAndZip3
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def EnumerateAndZip3():
    days = [19,21,22,21,20,22]

    print("enumerate(): Method 1:")
    enumerateDays = enumerate(days)
    for i,j in enumerateDays:
        print("F1 - day= ", i, "month= ", j)
    else: # When loop end widhout break
        print(end='\n')

    print("enumerate(): Method 2:")
    for i,j in enumerate(days):
        print("F2 - day= ", i, "month= ", j)
    else: # When loop end widhout break
        print(end='\n')

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       IterationsDictionaries
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def IterationsDictionaries():
    listWorkDays = [19,21,22,21,20,22]
    listMonths = ["01","02","03","04","05","06"]

    #dict(key, value)
    # Iterowanie przed słownik dla kluczy
    dictMonthsDays = dict(zip(listMonths, listWorkDays))
    print("Method1: for key in dictMonthsDays:")
    for key in dictMonthsDays:
        print("key= ", key, "dict[key]= ", dictMonthsDays[key], end='\n')
    else:
        print(end= '\n')

    # Przebudowanie for aby dostac tylko vartości
    # KOlejność wartości nie jest gwarantowana dla słownika
    print("Method2: for val in dictMonthsDays.values:")
    for val in dictMonthsDays.values():
        print("val= ", val)
    else:
        print(end= '\n')

    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       ForLoopNesting
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def ForLoopNesting():
    listA = list(range(0x00, 0x04, 0x01))
    listB = list(range(0x00, 0x04, 0x01))

    listAB:list
    dictAB:dict

    # Standardowa notacja dla tworzenia takiej listy
    for a in listA:
        for b in listB:
            listAB.append((a,b))
    print(listAB)
    listAB.clear()

    # Jednolonijkowe tworzenie nowej listy
    # Bardzo często tworzona notacja
    listAB = [(a,b) for a in listA for b in listB]
    print(listAB)
    listAB.clear()

    # Jednolinijkowe tworznie wraz z warunkami to dodawania elementów
    listAB = [(a,b) for a in listA for b in listB if a%2==1 and b%2==1]
    print(listAB)

    # Aby dować słownik jedynie nalezy zmienic notacje na {}
    # Słownik zawiera tylko unikalne elementy
    # Klucz jest unikalny i wartości są nadpisywane jeśli dla tego samego klucza dodajemy wartośc
    dictAB = {a:b for a in listA for b in listB if a%2==1 and b%2==1}
    print(dictAB)
    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       GeneratorsPart1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def GeneratorsPart1():
    listA = list(range(0x00, 0x04, 0x01))
    listB = list(range(0x00, 0x04, 0x01))

    # Generator jest opeketem króry generuje następny element wegług jakiegos wzoru
    # Generator jest opbeiktem który oszczędza pamięć RAM

    # Generator stworzony z innych list
    genAB = ((a,b) for a in listA for b in listB if a%2==1 and b%2==1)
    for a,b in genAB:
        print("a= ", a, "b= ", b)
    else:
        print(end='\n')

    # Generator całkowiecie stworzony z inych generatorów
    genAB = ((a,b) for a in range(0x00, 0x04, 0x01) for b in range(0x00, 0x04, 0x01) if a%2==1 and b%2==1)
    for a,b in genAB:
        print("a= ", a, "b= ", b)
    else:
        print(end='\n')

    # Aby na nowo wywołać generator należy do od nowa zdefiniować
    # Nie zawiera on polecenia resetowania
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       GeneratorsPart2
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def GeneratorsPart2():
    # Aby na nowo wywołać generator należy do od nowa zdefiniować
    # Nie zawiera on polecenia resetowania
    genAB = ((a,b) for a in range(0x00, 0x04, 0x01) for b in range(0x00, 0x04, 0x01) if a%2==1 and b%2==1)
    while(1):
        try:
            (a,b) = next(genAB) # (a,b) = genAB.__next__()
        except StopIteration:
            print("except StopIteration")
            break
        print("a= ", a, "b= ", b)

    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
#=======================================================================================================================================

#=======================================================================================================================================
if (__name__ == "__main__"):
    pass
else:
    pass
#=======================================================================================================================================