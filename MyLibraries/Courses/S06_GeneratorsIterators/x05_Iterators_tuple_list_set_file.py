'''******************************************************************************
@Brief  
'''
def CALL_Iterable_NotIterator_part1()->None:
    myTuple:tuple = (0,1,2,3,4,5,6,7)

    # 1. Iterable: OK
    for i in myTuple:
        print("i= ", i)

    # 2. Iterator: NOT
    # Błąd!
    print("next()= ", next(myTuple))
    print("next()= ", next(myTuple))
    print("next()= ", next(myTuple))
#================================================================================

'''******************************************************************************
@Brief  Aby dla tuple wywołac metode next naleźy utworzyć iterator
'''
def CALL_Iterable_NotIterator_part2()->None:
    myTuple:tuple = (0,1,2,3,4,5,6,7)

    # 1. Iterable: OK
    for i in myTuple:
        print("i= ", i)

    # 2. Iterator: OK po nowej instancji
    myIter = iter(myTuple)
    print("next()= ", next(myIter))
    print("next()= ", next(myIter))
    print("next()= ", next(myIter))
#================================================================================

'''******************************************************************************
@Brief  Set tak samo jak tuple, list nie nie są iteratorem
'''
def CALL_Iterable_NotIterator_part3()->None:
    mySet:set = {0,1,2,3,4,5,6,7}

    # 1. Set Iterable: OK
    for i in mySet:
        print("i= ", i)

    # 2. Set Iterator: NOT
    print("next()= ", next(mySet))
    print("next()= ", next(mySet))
    print("next()= ", next(mySet))
#================================================================================

'''
'''

if(__name__ == "__main__"):
    CALL_Iterable_NotIterator_part3()
else:
    pass