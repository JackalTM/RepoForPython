class GlobalClass():
    valueInt:int = 0
    valueStr:str = ""
    someList:list = []

    def __str__(self) -> str:
        return "valueInt= {}, valueStr= {}, someList= {}".format(GlobalClass.valueInt, GlobalClass.valueStr, GlobalClass.someList)
#--------------------------------------------------------------------
def ChangeByReferenceTest_Global(refGlobalClass:GlobalClass)->None:
    refGlobalClass.valueInt = 1
    refGlobalClass.valueStr = "TEST"
    refGlobalClass.someList.append("TEST")
    return None
#--------------------------------------------------------------------
# Globalna klasa
# Wniosek klasy oraz obiekty sa przekazywane przez referencję
# Istniene możlowośc zmiany wartości 
def CALL_Test1():
    print(GlobalClass())
    ChangeByReferenceTest_Global(GlobalClass)
    print(GlobalClass())
    return None  
#=======================================================================================================================================
class InstanceClass():
    someList:list = []
    def __init__(self, vInt:int, vStr:str, vList:list) -> None:
        self.vInt = vInt
        self.vStr = vStr
        self.vList = vList

    def __str__(self) -> str:
        return "Int= {}, str= {}, list= {}, gList= {}".format(self.vInt, self.vStr, self.vList, InstanceClass.someList)
#--------------------------------------------------------------------
def ChangeByReferenceTest_Instance(refInstanceClass:InstanceClass)->None:
    refInstanceClass.vInt = 1
    refInstanceClass.vStr = "TEST2"
    refInstanceClass.vList.append("TEST2")
    refInstanceClass.someList.append("TEST2")
    return None
#--------------------------------------------------------------------
# Instancja klasy
# Wniosek klasy oraz duze obiekty sa przekazywane przez referencję
# Istniene możlowośc zmiany wartości 
# Lista równiez jest przekazywana jako referencja 
def CALL_Test2():
    testList = [1,2,3,4]
    testList2 = [5,6,7,8]
    instInstanceClass = InstanceClass(0, "", [])

    print(instInstanceClass)
    # Reference to external list is set!
    InstanceClass.someList = testList
    instInstanceClass.vList = testList2
    ChangeByReferenceTest_Instance(instInstanceClass)
    print(instInstanceClass)

    print("testList= {}".format(testList))
    print("testList2= {}".format(testList2))
    return None
#=======================================================================================================================================
if (__name__ == "__main__"):
    CALL_Test2()
else:
    pass
#=======================================================================================================================================