from math import sqrt
'''***************************************************************************************************************
@name       FindInDictionary
@brief      ...
@param[in]  refDictionary - Dictionary object, in this case it is reference object
@param[in]  keyStr - Key for ditionary
@param[in]  bb - Weight of plactic bullet
@note       ...
@return     Velocity of a bullet
'''
def FindInDictionaryExample(refDictionary:dict, keyStr:str, bb:float)->float:
    try:# Test zadania
        energy:float = refDictionary[keyStr]
    except:# Jesli bląd
        energy:float = 0.0
        speed:float = 0.0
    else: # Jesli błędu nie ma 
        speed = (2*energy) / bb
        speed = speed * 1000
        speed = sqrt(speed)
    finally: # Zawsze wykonane
        return speed
#===================================================================================================================

'''***************************************************************************************************************
@name       FindInDictionary
@brief      ...
@param[in]  refDictionary - Dictionary object, in this case it is reference object
@param[in]  bb - Weight of plactic bullet
@note       ...
@return     Velocity of a bullet
'''
def FindInDictionaryExept(refDictionary:dict, bb:float)->float:   
    #------------------------------------------------------------- 
    try:
        keyStr = str(input("Posible choice: CQB, ASS, DMR, SNI "))
        energy:float = refDictionary[keyStr]
    except KeyError as e:
        print(">> -------------")
        print("Choice {} is not valid".format(e), end= '\n')
        print("Error: ", e)
        print("KEY ", [i for i in refDictionary.keys()])
        print(">> -------------")
        return 0.0
    #-------------------------------------------------------------
    try:
        temp = input("Hop up energy reduction in float [J]: ")
        energyReducion = float(temp)
    except (ValueError, ZeroDivisionError, FloatingPointError) as e:
        print(">> -------------")
        print("Input: > ", temp, " < in for valid float!")
        print("ValueError: ", e)
        print(">> -------------")
        return 0.0
    except Exception as e: 
        print(">> -------------")
        print("Input: > ", temp, " < in for valid float!")
        print("Exception: ", e)
        print(">> -------------")
        return 0.0
    else:
        energy = energy - energyReducion
    #-------------------------------------------------------------
    speed = (2*energy) / bb
    speed = speed * 1000
    speed = sqrt(speed)
    return speed
#===================================================================================================================

'''*****************************************************************************************************************
@name       MyErrorRaise
@brief      ...
@note       ...
'''
def MyErrorRaise(weightBB:float)->bool:
    posibleWeight:tuple = (0.2, 0.23, 0.25, 0.28, 0.30, 0.32)
    if(weightBB in posibleWeight):
        return True
    else:
        raise Exception("Niedozwolone kulki!")
#===================================================================================================================

def CALL_DictionariesFaults()->None:
    myDictionary = {"CQB":1.15, "ASS":1.9, "DMR":2.6, "SNI":3.6}
    velocity = FindInDictionaryExept(myDictionary, 0.2)
    print("Velocity = ", velocity)
    return None
#===================================================================================================================

def CALL_CustomErrorraise()->None:
    bbWeight = 0.4
    #-------------------------------------------------------------
    try:
        MyErrorRaise(bbWeight)
    except Exception as e:
        print("Error: ", e)
    #-------------------------------------------------------------
    return None
#===================================================================================================================


'''*****************************************************************************************************************
@name       CALL_AsertMethod
@brief      Testowanie warunków dla testowania 
@note       Jesli zmmienna środowiskowa "PYTHONOPTIMAZE=TRUE" to asser nie bedzie wykonywane
'''
def CALL_AsertMethod()->None:

    bbWeight = 0.12

    posibleWeight:tuple = (0.2, 0.23, 0.25, 0.28, 0.30, 0.32)

    # Działa jeśli "PYTHONOPTIMAZE="
    assert (bbWeight >= posibleWeight[0]), "BB weight less than {} !".format(posibleWeight[0])
    assert (bbWeight <= posibleWeight[-1]), "BB weight less than {} !".format(posibleWeight[-1])

    return None
#===================================================================================================================

'''*************************************************************************************************************************************
@name       MYEeption(Exception)
@brief      Tworzenie nowego wyjątku jako błedu
@note       Bład urzytkownika utworzony z Klasy Exception
            Mozna oprogramować bład natury aplikacyjnej nie związany z samym językiem programownia 
'''
class MYEeption(Exception):
    def __init__(self, text:str, area:str) -> None:
        super().__init__(text)
        self.area = area

    def __str__(self) -> str:
        return ">> MYEeption | ERROR info:= {} | AREA:= {} |".format(super().__str__(), self.area)
#-------------------------------------------------------------------------------------------------
'''
@name   MYSecurityEeption(MYEeption)
@brief  Klasa pusta aby rozrózniac typy błędów
'''
class MYSecurityEeption(MYEeption):
    pass
#-------------------------------------------------------------------------------------------------
'''
@name MYDataFormatEeption(MYEeption)
@brief  Klasa pusta aby rozrózniac typy błędów
'''
class MYDataFormatEeption(MYEeption):
    pass
#=======================================================================================================================================

def CALL_MyNewExeptionErrorClass()->None:
    try:
        raise MYEeption("My custom ERROR!", "My custom data")
    except MYEeption as e:
        print(e)
    #-------------------------------------------------------------
    try:
        raise MYEeption("My custom ERROR!", "My custom files")
    except MYEeption as e:
        print(e)
#-------------------------------------------------------------------------------------------------
def CALL_MultiExeptionError(errorNum:int)->None:
    ERROR_TYPE_1:int = 1
    ERROR_TYPE_2:int = 2
    ERROR_TYPE_3:int = 3

    try:
        if(errorNum == ERROR_TYPE_1):
            raise MYEeption("ERROR 1: ", "1")
        elif(errorNum == ERROR_TYPE_2):
            raise MYSecurityEeption("ERROR 2: ", "2")
        elif(errorNum == ERROR_TYPE_3):
            raise MYDataFormatEeption("ERROR 3: ", "3")
        else:
            raise Exception(" Other error: ", " ")
    
    except MYEeption as e:
        print(e)
    except MYSecurityEeption as e:
        print(">> MYSecurityEeption | ",e)
    except MYDataFormatEeption as e:
        print(">> MYDataFormatEeption | ",e)
    except Exception as e:
        print(">> Exception | General | ", e)
    else:
        pass
    finally:
        pass

    return None
#=======================================================================================================================================


if(__name__ == "__main__"):
    CALL_MultiExeptionError(2)
else:
    pass