'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
#=======================================================================================

'''*************************************************************************************
@name       ...
@brief      Counter object count amount of same objects in list
            Amount of objects ar asigned into this object in dictionary
@param[in]  ...
@note       Resoult is Counter dictionary with other posibility similar to standard dictionary object
@return     ...
'''
from collections import Counter
def CALL_CollectionsCounter_1():
    someList = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
    someDict = Counter(someList)
    print("someList = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]")
    print(someDict)

    someString ="password"
    print("someString = password")
    someDict = Counter(someString)

    someList = [[1,2,3], [4,5,6], [1,2,3], [4,5,6]]
    try:
        # Not working
        someDict = Counter(someList)
    except:
        someDict = {}

    print("[[1,2,3], [4,5,6], [1,2,3], [4,5,6]]")
    print(someDict)

    listOfWords = "Password as password is wrong password".lower().split()
    someDict = Counter(listOfWords)
    print("listOfWords = Passwrods as passwors is wrong password.split()")
    print(someDict)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_Collections_defaultdict_1
@brief      Functionality of normal dictionary
@param[in]  void 
@note       when key is missing error will occure
@return     void
'''
from collections import defaultdict
def CALL_Collections_defaultdict_1():

    normalDictionary = { 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15 }
    try:
        # In normal distionary this will resould error 
        val = normalDictionary['g']
    except KeyError:
        print("Dictionary ERROR!")
        val = 0x00
    print(val)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_Collections_defaultdict_2
@brief      Functinality of defaultdict from collection module
@param[in]  void
@note       defaultdict when key is missind can be assigned default value
@return     void 
'''
from collections import defaultdict
def CALL_Collections_defaultdict_2():

    defaultDictionary = defaultdict(lambda: 0x00)
    defaultDictionary['a'] = 10
    defaultDictionary['b'] = 11
    defaultDictionary['c'] = 12
    defaultDictionary['d'] = 13
    defaultDictionary['e'] = 14
    defaultDictionary['f'] = 15

    print("collection.defaultdick call :")
    print(defaultDictionary['a'])
    print(defaultDictionary['g'])

    normalDictionary = { 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15 }
    defaultDictionary = defaultdict(lambda: 0x00, normalDictionary)
    print("collection.defaultdick call :")
    print(defaultDictionary['a'])
    print(defaultDictionary['g'])

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_namedtuple
@brief      Functionality of a namedtuple
@param[in]  void
@note       namedtuple is similar to class / structure object. Object need to created 
            TupleTEmplate = namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
@return     void
'''
from collections import namedtuple
def CALL_namedtuple():
    # Named tubplet is more like calss object
    # Arguments from a list is converted to imput argument
    # Its like dictionary and with real arguments
    # It can be function like structure silimar to other languages with constant values

    normalTuplet = (10,20,30)

    SwordnamedTuplet = namedtuple("Sword", ["mass", "lenght", "angle"])
    longSword = SwordnamedTuplet(mass= 2, lenght= 1.3, angle= 0.0)

    # Value assignatation is not posible to namedtuple() object!!!
    #longSword.mass = 5
    print("{} | {} | {}".format(longSword.mass, longSword.lenght, longSword.angle))

    return None
#=======================================================================================
    

if(__name__) == ("__main__"):
    CALL_namedtuple()