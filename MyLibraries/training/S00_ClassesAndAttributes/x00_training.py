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
@brief      Some more methods for dictionaries
@param[in]  ...
@note       ... 
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

    else:
        print("For break: ")

    print("Instr taken: ", instructionsApproved)

    return None
#=======================================================================================================================================


#=======================================================================================================================================
if (__name__ == "__main__"):
    Call_ElseInLoops()
else:
    pass
#=======================================================================================================================================