'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
#=======================================================================================

'''*************************************************************************************
@name       CALL_AdvancesStringsTest
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_AdvancesStringsTest():
    tStr = "some string"

    tResouldStr = tStr.capitalize()
    print("tStr.capitalize() = {}".format(tResouldStr))

    tResouldStr = tStr.upper()
    print("tStr.upper() = {}".format(tResouldStr))

    print("tStr.find('e') = {}".format(tStr.find('e')))

    tResouldStr = tStr.center(21, '-')
    print("tStr.center(21, '-') = {}".format(tResouldStr))

    tStr.isalnum()
    tStr.islower()
    tStr.isspace()
    tStr.istitle()
    tStr.isupper()
    tStr.endswith('\n')
    tStr.split(' ')
    tStr.partition(' ')

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_AdvanceSetLection
@brief      Set is a objecte with only unique items
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_AdvanceSetLection():

    tSET = set()

    # Add item to set 
    tSET.add(0)
    tSET.add(9)

    # Clear all elements in set
    tSET.clear()

    tSET_A = {1,2,3}
    tSET_B = {1,2,4}
    tSET_A.difference(tSET_B)

    print("tSET_A.difference(tSET_B) = {}".format(tSET_A.difference(tSET_B)))

    # Intersection
    print("tSET_A.intersection(tSET_B) = {}".format(tSET_A.intersection(tSET_B)))

    # Sub set of other set 
    tSET_A.issubset(tSET_B)

    # Contail other set
    tSET_B.issubset(tSET_A)

    # simetric differences
    tSET_A.symmetric_difference(tSET_B)

    # union of sets
    tSET_B.union(tSET_A)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_AdvanceDictionaries
@brief      Some more methods for dictionaries
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_AdvanceDictionaries():
    dic1 = {0x00 : "No errors!", 0x01 : "Parameter error!"}

    # Dictionares comperason
    # most usseful when dictionaries are based only on values
    tDict = {x : x**2 for x in range(0, 0xF, 0x01)}


    for key in tDict.iterkeys():
        print("tDict.key= {}".format(key))


    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_AdvancesLists
@brief      Some more methods for dictionaries
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_AdvancesLists():
    # Append item to list 
    tList = [0,1,2,3,4,5]
    tList.append(6)

    # Count how many times object is in list 
    tList.count(0)

    # Extend list by list argument
    # List is still one dimensional
    tList.extend([6,7,8,9])

    # Index of element put as argument
    # Index value is returned
    # Not present elemenst will  error occure
    tList.index(4)

    # Insert elemenet at index
    tList.insert(0, 9)

    # Pop last item from list 
    # Its inplace
    tList.pop()

    # Remove first occurence of a value
    tList.remove(9)

    # Reverse a list 
    # Its inplace 
    tList.reverse()

    return None
#=======================================================================================

if (__name__ == "__main__"):
    CALL_AdvanceDictionaries()
else:
    pass