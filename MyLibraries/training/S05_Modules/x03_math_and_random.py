'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
#=======================================================================================

'''*************************************************************************************
@name       CALL_Math_module
@brief      Some usage of math module
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_Math_module():
    import math

    value = 2.78

    a = math.floor(value)
    b = math.ceil(value)

    print("math.floor({}) = {}".format(value, a)) # will be lower 
    print(" math.ceil({}) = {}".format(value, b)) # will be upper 
    print('\n')

    # Number round for ever and odd is deffrent for negatin round error 
    # This is usfull with big data sets
    a = round(3.5)
    b = round(4.5)
    c = round(5.5)
    d = round(6.5)
    print("round(3.5) = {}".format(a))
    print("round(4.5) = {}".format(b))
    print("round(5.5) = {}".format(c))
    print("round(6.5) = {}".format(d))
    print('\n')

    # Methematical constants
    tPI = math.pi
    tE = math.e
    tINF = math.inf
    tLogE = math.log(math.e)
    print("math.pi = {}".format(tPI)) 
    print("math.e = {}".format(tE)) 
    print("math.inf = {}".format(tINF)) 
    print("tLogE = math.log(math.e) = {}".format(tLogE))
    print('\n')

    return None
#=======================================================================================
'''*************************************************************************************
@name       CALL_Random_module
@brief      Usage and test of a random module 
@param[in]  ...
@note       return number between range  
@return     ...
'''
def CALL_Random_module():
    import random

    for i in range(0, 8, 1):
        randomInt = random.randint(0, 0xFF)
        print("- {}".format(randomInt))
    print('\n')

    someList = list(range(0, 8, 1))
    randomElement = random.choice(someList)
    print("random.choice(someList) = {}".format(randomElement))
    randomElement = random.choice(someList)
    print("random.choice(someList) = {}".format(randomElement))
    randomElement = random.choice(someList)
    print("random.choice(someList) = {}".format(randomElement))
    print('\n')

    return None
#=======================================================================================
'''*************************************************************************************
@name       CALL_random_elements_from_list
@brief      Taking random element from list 
            With replecement 
            Widhount replecement
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_random_elements_from_list():
    import random

    someList = list(range(0, 8, 1))

    # Sample with replecement
    # Number can repeat
    els = random.choices(population= someList, k= 4)
    print("els = random.choices(population= someList, k= 4) = ")
    print(els)
    print('\n')

    # sample widhout replecement
    # None of numbers are repeated
    els = random.sample(population= someList, k= 4)
    print("els = random.sample(population= someList, k= 4)")
    print(els)
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
def CALL_random_shuffle_list():
    import random

    someList = list(range(0, 8, 1))

    # Shuffle list is done inplace
    # List is permanently affected
    random.shuffle(someList)
    print("random.shuffle(someList)")
    print(someList)
    print('\n')

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_random_unifirm_gauss
@brief      Unifirm distribution that return float
            Gauss that return nubmer with gauss distrubution
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_random_unifirm_gauss():
    import random

    # Uniform distributio from number range
    # These choise is taken with float 
    value = random.uniform(0, 7)
    print("random.uniform(0, 7) = {}".format(value))
    value = random.uniform(0, 7)
    print("random.uniform(0, 7) = {}".format(value))
    print('\n')

    # Gauss distribution 
    value = random.gauss(mu= 0, sigma= 110)
    print("random.gauss(mu= 0, sigma= 110) ={}".format(value))
    value = random.gauss(mu= 0, sigma= 110)
    print("random.gauss(mu= 0, sigma= 110) ={}".format(value))
    print('\n')

    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_random_unifirm_gauss()
else:
    pass