'''*************************************************************************************************************************************
@name       Cartype
@brief      ...
@note       ...
'''
from typing import Any
from typing import overload

class Cartype:
    numCars = 0
    listCars = []
    def GetClassInfo()->None:
        print("-----------------", end= '\n')
        print("Number of cars: ", Cartype.numCars, end= '\n')
        print("Car list: ", Cartype.listCars, end= '\n')
        print("-----------------", end= '\n')
        return None
    
    def __init__(self, brand:str, model:str, isonsale:bool) -> None:
        print(">> Cartype.__init__(): ", self.__class__.__name__, end= '\n')
        self.brand = brand
        self.model = model
        self.__isonsale = isonsale
        Cartype.numCars = Cartype.numCars + 1
        Cartype.listCars.append(brand)
        return None
    
    def GetInfo(self)->None:
        print("-----------------", end= '\n')
        print("Brand: ", self.brand, end= '\n')
        print("Model: ", self.model, end= '\n')
        print("Is on sale:", self.__isonsale, end='\n')
        print("-----------------", end= '\n')
        return None
#----------------------------------------------------------------------
class Truck(Cartype):
    def __init__(self, brand:str, model:str, isonsale:bool, capacity:int) -> None:
        # Jesli jedno dziedziczenie:
        print(">> Truck(Cartype).__init__(): ", self.__class__.__name__, end= '\n')
        super(Truck, self).__init__(brand, model, isonsale)
        #Cartype.__init__(brand, model, isonsale)
        self.capacity:int = capacity

    def GetInfo(self) -> None:
        print("------------------------------------", end= '\n')
        super(Truck, self).GetInfo()
        print("Capacity : ", self.capacity, end= '\n')
        print("------------------------------------", end= '\n')
        #Cartype.GetInfo()

#----------------------------------------------------------------------
def Call_CarTypeCalss1()->None:
    Cartype.GetClassInfo()

    myRenault = Cartype("Renault", "Megane", False)
    myFiat = Cartype("Fiat", "500", True)

    myRenault.GetInfo()
    myFiat.GetInfo()
    myRenault.newAtribute = "New atribute"

    print(vars(myRenault))
    print(vars(myFiat))

    setattr(myRenault, "yearProduction", 2014)

    print(vars(myRenault))
    print(vars(myFiat))

    Cartype.GetClassInfo()

    return None

def Call_TruckTypeCalas()->None:
    # Testowanie dziedziczenia
    myTransit:Truck = Truck("Ford", "Transit", False, 1600)
    myTrafic:Truck = Truck("Ford", "Trafic", False, 1200)

    myTransit.GetInfo()
    myTrafic.GetInfo()

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Cartype, properties
@brief      Property is used to changed private data for class instance.
            Albo posbile to use private methods
@note       ...
'''
class CartypeProperties:
    numCars = 0
    brandOnSale = ""
    listCars = []
    def GetClassInfo()->None:
        print("=================", end= '\n')
        print("Number of cars: ", Cartype.numCars, end= '\n')
        print("Car list: ", Cartype.listCars, end= '\n')
        print("=================", end= '\n')
        return None
    
    def __init__(self, brand:str, model:str, isonsale:bool) -> None:
        self.brand = brand
        self.model = model
        self.__isonsale = isonsale
        Cartype.numCars = Cartype.numCars + 1
        Cartype.listCars.append(brand)
        return None
    
    def GetInfo(self)->None:
        print("=================", end= '\n')
        print("Brand: ", self.brand, end= '\n')
        print("Model: ", self.model, end= '\n')
        print("Is on sale:", self.__isonsale, end='\n')
        print("=================", end= '\n')
        return None
    
    def GetOnSale(self)->bool:
        return self.__isonsale
    
    def SetOnSale(self, newStatus:bool)->bool:
        if(CartypeProperties.brandOnSale == self.brand):
            self.__isonsale = newStatus
            print("{}: Status changed!".format(self.brand), end='\n')
            return True
        else:
            print("{}: Status unchanged!".format(self.brand), end='\n')
            return False
        
    #Class property
    PropertyOnSale = property(GetOnSale, SetOnSale, None, "Only actual promo posible!")
#=========================================================================================
# Dziwdziczenie 

#=========================================================================================
    
def Call_CarTypeCalssProperties()->None:

    CartypeProperties.brandOnSale = "Renault"

    myRenault = CartypeProperties("Renault", "Megane", False)
    myFiat = CartypeProperties("Fiat", "500", False)

    myRenault.GetInfo()
    myFiat.GetInfo()

    myRenault.PropertyOnSale = True
    myFiat.PropertyOnSale = True

    myRenault.GetInfo()
    myFiat.GetInfo()

    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       Sword(Weapon):
@brief      Inheritance
@note       ...
'''
class Weapon():

    def __init__(self)->None:
        print("Class Weapon created!", end= '\n')
        return None

    def WhatKind(self)->None:
        print("Weapon depend of situation", end= '\n')
        return None

    def Atack(self)->None:
        print("Atacking!", end= '\n')
        return None

class Sword(Weapon):

    def __init__(self)->None:
        Weapon.__init__(self)
        print("Sword created!")
        return None

    def WhatKind(self)->None:
        print("White metal weapon", end= '\n')    
        return None
    
    def Swing(self, nTimes:int)->None:
        print("Sword swing {} times!".format(nTimes), end= '\n')
        return None
#=======================================================================================================================================

def CALL_ClassInheritance_01()->None:
    instWeapon = Weapon()
    instWeapon.WhatKind()
    instWeapon.Atack()
    return None

def CALL_ClassINheritance_02()->None:
    instSword = Sword()
    instSword.WhatKind()
    instSword.Atack()
    instSword.Swing(0x03)
    return None

'''*************************************************************************************************************************************
@name       Pistol, Rifle
@brief      ...
@note       ...
'''
class Pistol():

    def __init__(self, name:str)->None:
        self.name = name
        return None
    
    def Shoot(self, caliber:int)->str:
        tStr = "Pistol {} of {} caliber shoot!".format(self.name ,caliber)
        return tStr

class Rifle():

    def __init__(self, name:str)->None:
        self.name = name
        return None
    
    def Shoot(self, caliber:int)->str:
        tStr = "Rifle {} of {} caliber shoot!".format(self.name, caliber)
        return tStr
#=======================================================================================================================================
def CALL_PolimorfismPistolRifle():
    instPistol = Pistol("USP")
    instRifle = Rifle("L96")

    print(instPistol.Shoot(".45 cal"))
    print(instRifle.Shoot("7,56"))
    return

def CALL_IterThroughtClass():
    instPistol = Pistol("USP")
    instRifle = Rifle("L96")

    for i in (instPistol, instRifle):
        print(i.Shoot(" .045 "))
    return
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Knife, Folder, Machete
@brief      Inheritance
@note       ...
'''
class Knife():
    #Every instance of class will have some attributes
    def __init__(self, typs)->None:
        self.typs = typs
        return None
    
    def Cut(self)->None:
        raise NotImplementedError("Base class, implementation needed!")

class Folder(Knife):

    def Cut(self, nTimes:int)->None:
        print("Folding {} knive cut {} times.".format(self.typs, nTimes), end= '\n')
        return None
    
class Machete(Knife):

    def Cut(self, nTimes:int)->None:
        print("Machete {} blade cut {} times.".format(self.typs, nTimes), end= '\n')
        return None
    


#=======================================================================================================================================

def CALL_BaseClassDerived()->None:
    instFolder = Folder("Cold Steel")
    instMachete = Machete("Condor")

    instFolder.Cut(4)
    instMachete.Cut(7)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       TestClass
@brief      Wywyoływanie instancji klasy jako dodany atrybut
@note       ...
'''
class TestClass:

    def __init__(self, *args) -> None:
        self.itemsList = []
        for i in args:
            self.itemsList.append(i)

    # instTestClass():
    def __call__(self, *args) -> None:
        for i in args:
            self.itemsList.append(i)

    # str(instTestClass):
    def __str__(self) -> str:
        tempStr = "list: "
        for i in self.itemsList:
            tempStr = "{} {},".format(tempStr, str(i))
        return tempStr

def CALL_CallClassInstance() -> None:
    instTestClass = TestClass(0.2, 0.23)
    print(instTestClass)

    instTestClass(0.25, 0.28)
    print(instTestClass)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       FunctionDecoratorClass
@brief      Dekorowanie funkcji za pomoca klasy
@note       ...
'''
class FunctionDecoratorClass:
    selectedItems = []
    def __init__(self, refFun:object) -> None:
        print(">> __init__ : FunctionDecoratorClass ", end= '\n')
        self.refFun = refFun

    def __call__(self, refList:list) -> str:
        print(">> __call__ : FunctionDecoratorClass", end= '\n')
        tListNotSelected = [i for i in refList if i not in FunctionDecoratorClass.selectedItems]
        print("List o select from: ", tListNotSelected, end= '\t')
        tstr = self.refFun(tListNotSelected)
        FunctionDecoratorClass.selectedItems.append(tstr)
        return tstr

# Rozwiązanie bez dekoratora 
def CALL_FunctionClassDecorator1()->None:
    import random
    cars:list = ["Opel", "Toyota", "Fiat", "Renault", "Peygout", "Mazda"]

    def RandomSelectFromTupl(refList:list)->str:
        tempStr = random.choice(refList)
        refList.remove(tempStr)
        return tempStr
    
    print("1: ", RandomSelectFromTupl(cars))
    print("2: ", RandomSelectFromTupl(cars))
    print("3: ", RandomSelectFromTupl(cars))
    print(cars)

    return None

#Rozwiązanie z dekoratorem jako klasa. Rozwiązanie bez dotykania funkcji
def CALL_FunctionClassDecorator2()->None:
    import random
    cars:list = ["Opel", "Toyota", "Fiat", "Renault", "Peygout", "Mazda"]

    @FunctionDecoratorClass
    def RandomSelectFromTupl1(refList:list)->str:
        tempStr:str = random.choice(refList)
        return tempStr
    
    @FunctionDecoratorClass
    def RandomSelectFromTupl2(refList:list)->str:
        tempStr:str = random.choice(refList)
        return tempStr
    
    @FunctionDecoratorClass
    def RandomSelectFromTupl3(refList:list)->str:
        tempStr:str = random.choice(refList)
        return tempStr
    
    print("--")
    
    print("1: ", RandomSelectFromTupl1(cars))
    print("2: ", RandomSelectFromTupl2(cars))
    print("3: ", RandomSelectFromTupl3(cars))

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Dziedziczenie z wielu klas
@brief      ...
@note       ...
'''
class Engine:
    
    def __init__(self, brand:str, model:str, weight:int) -> None:
        print(">> Engine.__init__() - start")
        self.brand = brand
        self.model = model
        self.weight = weight
        print(">> Engine.__init__() - end")
        return None
    
    def GetInfo(self)->None:
        print(">> Engine.GetInfo() - start")
        print("Brand: ", self.brand, end= '\n')
        print("Model: ", self.model, end= '\n')
        print("Weight:", self.weight, end='\n')
        print(">> Engine.GetInfo() - end")
        return None
    
class Carbody:
    def __init__(self, material:str, model:str, color:str) -> None:
        print(">> Carbody.__init__() - start")
        self.material = material
        self.model = model
        self.color = color
        print(">> Carbody.__init__() - end")
        return None

    def GetInfo(self)->None:
        print(">> Carbody.GetInfo() - start")
        print("Body material: ", self.material, end= '\n')
        print("Car model: ", self.model, end= '\n')
        print("Color:", self.color, end='\n')
        print(">> Carbody.GetInfo() - end")
        return None
    

import types
class WholeCar(Engine, Carbody):
    def __init__(self, brand:str, engine_model:str, weight:int, material:str, body_model:str, color:str) -> None:
        print(">> WholeCar.__init__() - start")

        Engine.__init__(self, brand, engine_model, weight)
        Carbody.__init__(self, material, body_model, color)

        print(">> WholeCar.__init__() - end")
        return None
    
    def GetInfo(self) -> None:
        Engine.GetInfo(self)
        Carbody.GetInfo(self)
        return None
    
    # Szuka az znajdzie pierwszą metode pasujące.
    def GetInfo(self) -> None:
        #Engine.GetInfo(self)
        super(WholeCar, self).GetInfo()
        return None
    
def CALL_Multiinstance()->None:
    instWholeCar = WholeCar("Ford", "1,3 liter", 200, "aluminium", "Fiesta", "Black")
    instWholeCar.GetInfo()

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
#=======================================================================================================================================


if (__name__ == "__main__"):
    CALL_Multiinstance()
else:
    pass