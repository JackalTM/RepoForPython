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
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def ListAndRange():
    for i in range(0x00, 0xF):
        print("i= {}".format(i), end= '\n')

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

    listAB = []
    dictAB = {}

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
@name       FunctionEvaluation
@brief      Przetwarzanie kodu jaki jest wprowadzany zewnętrznie
@param[in]  ...
@note       ...
@return     ...
'''
def FunctionEvaluation1():
    value_x = 0xA
    str_password = "password"

    dict_globals = globals().copy()

    str_source_code = "value_x + value_x"
    resoult_eval = eval(str_source_code)

    print("Source code evaluation: ", resoult_eval, '\n', '\n')
    for i in dict_globals.values():
        print("- ", i)

    # Kasowanie zmiennej "str_password"
    del globals["str_password"]
    for i in dict_globals.values():
        print("- ", i)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       FunctionEvaluation
@brief      Przetwarzanie kodu jaki jest wprowadzany zewnętrznie
@param[in]  ...
@note       ...
@return     ...
'''
def FunctionEvaluation2():
    value_x = 0xA
    str_password = "password"
    
    #  Kasowanie wszystkich wartości aby dodać je ręcznie
    globals = {}
    str_source_code = "value_x + value_x"
    resoult_eval = eval(str_source_code)

    print("Source code evaluation: ", resoult_eval, '\n', '\n')

    for i in globals.values():
        print("- ", i)

    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       Function_expr
@brief      Umożliwnie wykonywanie calych wyrażeń programistycznych zewnętrznie napisanych
            Jest to dośc niebiespiecznie rozwiązanie.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_expr()->None:
    var_x = 15
    src_code = "var_x + var_x"
    code_resoult = eval(src_code)
    print("eval() = ", code_resoult)

    var_x = 15
    src_code = "var_x = var_x * 2"
    code_resoult = exec(src_code)
    print("var_x = ", var_x)

    # Możliwośc wykonawania zewnętrznego kodu
    src_code = '''
for i in range(0,10):
    print("i= ", i)
    '''
    code_resoult = exec(src_code)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_compile
@brief      Zewnętrzny kod który ma duzy opszar. Prkompilacja zewnętrznego kodu
@param[in]  ...
@note       ...
@return     ...
'''
def Function_compile()->None:
    num = 0
    source = "num = num + 1"
    scr_compiled = compile(source, 'Internal variabale source', "exec")

    for i in range(0,16):
        exec(scr_compiled)
        print("reportLine= ", num)
    else:
        print("Finish value= ", num)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_args
@brief      Wztawienie wiele argumnetów jako tuplet. Można dac wiele.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_args(*args)->None:
    for i in args:
        print("- ", i)
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_kwargs
@brief      Wztawienie wiele argumnetów jako słonik. Można dac wiele.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_kwargs(**kwargs)->None:
    for i in kwargs:
        print("key= ", i, " value= ", kwargs[i])
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_args_kwargs
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def Function_args_kwargs(*args, **kwargs)->None:
    #Wyświetlanie dla *args
    for i in args:
        print("i= ", i)

    #Wyswietlanie dla **kwargs
    for j in kwargs:
        print("key= ", j, " value= ", kwargs[j])
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_args_kwargs
@brief      Wywoływanie funkcji dla *args oraz **kwargs
@param[in]  ...
@note       ...
@return     ...
'''
def Call_Function_args_kwargs()->None:
    programNum = 1
    '''
    Required python version >= 3.10
    current version 3.9.13
    match programNum:
        case 1:
            Function_args(1,2,3,4,5,6,7,8,9)
        case 2:
            Function_kwargs(color= "red", size= "XL")
        case 3:
            my_args = (1,2,3,4)
            my_kwargs = {"A":1, "B":2, "C":3, "D":4}
            Function_args_kwargs(*my_args, **my_kwargs)
        case _:
            pass
    '''

    if(programNum == 1):
        Function_args(1,2,3,4,5,6,7,8,9)
    elif(programNum == 2):
        Function_kwargs(color= "red", size= "XL")
    elif(programNum == 3):
        my_args = (1,2,3,4)
        my_kwargs = {"A":1, "B":2, "C":3, "D":4}
        Function_args_kwargs(*my_args, **my_kwargs)
    else:
        pass
    
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_FunctionsAsAgrs
@brief      Testing Functions as argument to another function
@param[in]  ...
@note       ...
@return     ...
'''
def Call_FunctionsAsAgrs()->None:

    def AddNums(numA:int, numB:int)->int:
        return numA + numB
    
    def SubNums(numA:int, numB:int)->int:
        return numA - numB
    
    def MulNums(numA:int, numB:int)->int:
        return numA * numB
    

    def FunctionWraper(Funct:object, arg1:int, arg2:int)->None:
        print("Wrapper start: ", end='\t')
        res = Funct(arg1, arg2)
        print("{} {} = {}".format(arg1, arg2, res), end= ' ')
        print(" end", end= '\n')
        return None
    
    listFinctions = (AddNums, SubNums, MulNums)
    listArgs = ((1,2), (3,4), (5,6))
    
    for f in listFinctions:
        for i,j in listArgs:
            FunctionWraper(f, i,j)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_return1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def Call_Function_return1()->None:

    def AddNums(numA:int, numB:int)->int:
        return numA + numB
    
    def SubNums(numA:int, numB:int)->int:
        return numA - numB
    
    def MulNums(numA:int, numB:int)->int:
        return numA * numB

    def Calculate(Funct:object, *args)->int:
        res = 0
        for i in args:
            if(type(i) == int):
                res = Funct(res, i)
            else:
                pass

        return res
    
    listFinctions = (AddNums, SubNums, MulNums)
    listArgs = (1,2,3,4,5,6,7,8,9)

    for f in listFinctions:
        res = Calculate(f, *listArgs)
        print("res = ", res)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_return2
@brief      Creating function depend on functionality
@param[in]  ...
@note       Usefull depend whn some function need to done many times
@return     ...
'''
def Call_Function_return2()->None:

    def CreateFunction(kind:str)->object:
        startVal0 = ('+', '-')
        startVal1 = ('*', '/')

#************************************************
# Genaration function if else statment
        if(kind in startVal0):
            surceStrFunction = '''
def Function(*args):
    res = 0
    for i in args:
        res = res {} i
    return res
'''.format(kind)
        elif(kind in startVal1):
            surceStrFunction = '''
def Function(*args):
    res = 1
    for i in args:
        res = res {} i
    return res
'''.format(kind)
        else:
            surceStrFunction = '''
def Function(*args):
    res = 0
    for i in args:
        res = res {} i
    return res
'''.format(kind)

        exec(surceStrFunction, globals())
        return Function
#====================================================
        
    MyFunction1 = CreateFunction('+')
    MyFunction2 = CreateFunction("-")
    MyFunction3 = CreateFunction("*")
    listArgs = (1,2,3,4,5,6,7,8,9)

    print("Function add: ")
    res = MyFunction1(*listArgs)
    print("res= ", res)

    print("Function sub: ")
    res = MyFunction2(*listArgs)
    print("res= ", res)

    print("Function mull: ")
    res = MyFunction3(*listArgs)
    print("res= ", res)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrappersFunctions
@brief      Creating function that wrap input function by some other functionality
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrappersFunctions1()->None:

    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    def CreateFunWithWrapper(SomeFunction:object)->object:
        def FunWithWrapper(*args, **kwargs)->object:
            print("--"*0x10, end= '\n')

            print("Function name: ", SomeFunction.__name__, end= '\n')

            print("*args: ", end= '\t')
            for i in args:
                print(i, end= ', ')
            else:
                print(end= '\n')

            print("**kwargs: ", end= '\t')
            for i in kwargs:
                print("key: ", i, "arg: ", kwargs[i], end= ', ')
            else:
                print(end= '\n')

            ResFunction = SomeFunction(*args, **kwargs)
            print("=="*0x10, end='\n')
            return ResFunction
        return FunWithWrapper

    NewFunction = CreateFunWithWrapper(ChangeSalary1)
    NewFunction("Jack O lantern", 9.99, True)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrappersFunctions
@brief      Creating function that wrap input function by some other functionality
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrappersFunctions2()->None:
    #import functools
    
    def CreateFunWithWrapper(SomeFunction:object)->object:
        def FunWithWrapper(*args, **kwargs)->object:
            print("--"*0x10, end= '\n')

            print("Function name: ", SomeFunction.__name__, end= '\n')

            print("*args: ", end= '\t')
            for i in args:
                print(i, end= ', ')
            else:
                print(end= '\n')

            print("**kwargs: ", end= '\t')
            for i in kwargs:
                print("key: ", i, "arg: ", kwargs[i], end= ', ')
            else:
                print(end= '\n')

            ResFunction = SomeFunction(*args, **kwargs)

            print("=="*0x10, end='\n')
            return ResFunction
        return FunWithWrapper
    
    @CreateFunWithWrapper
    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    ChangeSalary1("Jack O Lantern Panik", 9.99, True)


    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrapperFunWithParameter
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrapperFunWithParameter()->None:
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
    Call_WrapperFunWithParameter()
else:
    pass
#=======================================================================================================================================