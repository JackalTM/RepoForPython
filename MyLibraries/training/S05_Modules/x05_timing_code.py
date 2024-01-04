import time
import timeit
'''*************************************************************************************
@name       NumList_type1
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def NumList_type1(n) -> list:
    return [str(numb) for numb in range(n)]
#=======================================================================================

'''*************************************************************************************
@name       NumList_type2
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def NumList_type2(n) -> list:
    return list(map(str, range(n)))
#=======================================================================================

#=======================================================================================
def CALL_TestFunctionsTime() -> None:
    
    # Grab time before execute
    # Grab time after execute

    ''' 
    n = 0xFFFFFF
    NumList_type1 execute = 6.575702667236328
    NumList_type2 execute = 4.326554775238037
    '''

    startTime = time.time()
    NumList_type1(0xFFFFFF)
    executeTime = time.time() - startTime
    print("NumList_type1 execute = {}".format(executeTime))
    
    startTime = time.time()
    NumList_type2(0xFFFFFF)
    executeTime = time.time() - startTime
    print("NumList_type2 execute = {}".format(executeTime))

    return None
#=======================================================================================
    
'''*************************************************************************************
Test 1:
    n = 0xFFFF
    m = 0xFF
    m x NumList_type1(n)= 6.2659645
    m x NumList_type2(n)= 3.7879029000000006

Test 2:
    n = 0xFF
    m = 0xFFFF
    m x NumList_type1(n)= 5.3322384000000005
    m x NumList_type2(n)= 3.404481200000001

Test 3:
    n = 100
    m = 1000000
    m x NumList_type1()= 34.0170444
    m x NumList_type2()= 21.9343929

Method NumList_type2() is faster .
'''  
def CALL_Test_timeit() -> None:

    stmtF1 = ''' 
NumList_type1(100)
    '''
    setupF1 = '''
def NumList_type1(n) -> list:
    return [str(numb) for numb in range(n)]
    '''

    stmtF2 = ''' 
NumList_type2(100)
    '''
    setupF2 = '''
def NumList_type2(n) -> list:
    return list(map(str, range(n)))
    '''
    timeF1 = timeit.timeit(stmt= stmtF1, setup= setupF1, number= 1000000)
    timeF2 = timeit.timeit(stmt= stmtF2, setup= setupF2, number= 1000000)

    print("Test time for NumList_type1()= {}".format(timeF1))
    print("Test time for NumList_type2()= {}".format(timeF2))

    return None

if(__name__) == ("__main__"):
    CALL_Test_timeit()
else:
    pass