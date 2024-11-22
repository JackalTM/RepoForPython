
#**********************************************************************************
# @Name             MyModule_Fun01
#
# @Brief            Test Function module
#     
# @parameter[in]    void
# 
# @return           void
#
def MyModule_Fun01():
    print("call -> MyModule_Fun01()", end='\n')
    return None
#===================================================================================


#**********************************************************************************
# @Brief            Flatten a nested list
#
def ListTest1()->None:
    from collections.abc import Iterable as IT

    def Flatten(refList:list)->any:
        for i in refList:
            if (isinstance(i, IT)) and not (isinstance(i, str)):
                yield from Flatten(i)
            else:
                yield i

    listOfList:list = [1, [2,3, [4,5]], 6]
    for i in Flatten(listOfList):
        print("- ", i, end= '\n')

    return None
#===================================================================================

#**********************************************************************************
# @Brief            List of Indicates for Specyfic value 
#
def ListTest2()->None:
    myList1:list = [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15]
    myList2:list
    myList3:list

    myList2 = [i for i in myList1]
    print("New list: ",myList2)

    myList3 = [i for i, x in enumerate(myList1) if x%2==0]
    print("New list: ", myList3)

    return None
#===================================================================================

#**********************************************************************************
# @Brief            LTranspose a list of list Matrix
#
def ListTest3()->None:
    tX:tuple = (1,2,3,4)
    tY:tuple = (5,6,7,8)
    tZ:tuple = (9,10,11,12)

    matrix_1:list = [tX, tY, tZ]
    matrix_1_t:list = list(map(list, zip(*matrix_1)))

    print("--- Matrix transpose", matrix_1_t)

    return None
#===================================================================================

#**********************************************************************************
# @Brief            Shift list by amount
#
def ListTest4()->None:

    def RotList(refList:list, n:int)->list:
        return refList[-n:] + refList[:-n]

    myList1:list = [0,1,2,3,4,5,6,7]
    myList2:list = RotList(myList1, 2)

    print('\n', "New rotated list: ", myList2)

    return None
#===================================================================================

#**********************************************************************************
# @Brief            Find duplicates in a list
#
def ListTest5()->None:

    from collections import Counter as CNT

    myList:list = [0,1,2,2,2,3,4,5,5,5,6,7,8,9]
    myDuplicates:list = [i for i, c in CNT(myList).items() if c > 1]
    print('\n', "List of duplicates: ", myDuplicates)

    return None
#===================================================================================


if(__name__ == "__main__"):
    ListTest5()
else:
    pass