'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
#=======================================================================================

'''===============================================================================================================
These are genarators by using yield keyword
Internaly generatorts are using next() and when stop iteration wrror ocured iteration is stoped 
'''

'''*************************************************************************************
@name       ...
@brief      List is cerated upfront
@param[in]  ...
@note       With very long list lot of memory is taken
@return     ...
'''
def CreateCubesList(n):
    listResoult = []
    for i in range(0, n, 1):
        listResoult.appent(n**3)
    return listResoult
#=======================================================================================
        
'''*************************************************************************************
@name       ...
@brief      More memory efficient
@param[in]  ...
@note       With very hight number aonly one numer at time is returned. Generator can be castet to a list 
@return     yield - One value at a time is returned
'''
def CreateCubesGenerator(n):
    for i in range(0, n, 1):
        yield (n**3)
#=======================================================================================
        
'''*************************************************************************************
@name       GenFib_v1
@brief      ...
@param[in]  ...
@note       ... 
@return     yield - One value at a time is returned
'''
def GenFib_v1(n):
    a = 0
    b = 1
    for i in range(0, n, 1):
        yield a
        (a, b) = (b, a + b)
#=======================================================================================
'''*************************************************************************************
@name       GenFib_v2
@brief      ...
@param[in]  ...
@note       ... 
@return     yield - One value at a time is returned
'''
def GenFib_v2(n):
    a = 0
    b = 1
    for i in range(0, n, 1):
        (a, b) = (b, a + b)
        yield a
#=======================================================================================
def CALL_Generator():
    FIBON_MAX = 7

    print("V1: Fobinachi sequance is generated: ")
    for num in GenFib_v1(FIBON_MAX):
        print("- {}".format(num), end= '\n')
    print('\n')

    print("V2: Fobinachi sequance is generated: ")
    for num in GenFib_v2(FIBON_MAX):
        print("- {}".format(num), end= '\n')
    print('\n')

    return None
#=======================================================================================

'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def GenSimple(n):
    for i in range(0, n, 1):
        yield i
#=======================================================================================
def CALL_SimpleGen1():
    # In this case StopIterationError will occure
    n = 0
    MAX_GEN = 9
    instGen = GenSimple(8)
    while(n < MAX_GEN):
        value = next(instGen)
        print("{} next(instGen()):= {}".format(n, value))
        n += 1
    return None
#=======================================================================================
def CALL_SimpleGen2():
    # In this case StopIterationError will occure
    n = 0
    MAX_GEN = 9

    someString = "password"
    instStrIter = iter(someString)

    while(n < MAX_GEN):
        value = next(instStrIter)
        print("i:= {}, {}".format(n, value))
        n += 1
    return None
#=======================================================================================
def CALL_SimpleGen3():
    # In this case StopIterationError will occure
    someString = "password"
    instStrIter = iter(someString)

    print("{} turned into generator".format(someString))
    while(True):
        try:
            letter = next(instStrIter)
        except StopIteration:
            break

        finally:
            print(letter)

    return None
#=======================================================================================
def CALL_GeneratorComperation():
    # This a generator comperation
    # Similar topis like list comperation
    # List is turned into generator comperation
    templist = [-3, -2, -1, 0 ,1 , 2, 3]
    instGenComp = (i for i in templist if i > 0)

    print("- templist = [-3, -2, -1, 0 ,1 , 2, 3]")
    print("- instGenComp = (i for i in templist if i > 0)")

    for i in instGenComp:
        print(i)

    return None
#=======================================================================================

'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
import random
def GenRandomNum(nLow, nHigh, nAmount):
    for i in range(0, nAmount, 1):
        yield random.randint(nLow, nHigh)
#=======================================================================================