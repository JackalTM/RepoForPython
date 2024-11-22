'''*************************************************************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Cartype, properties
@brief      Property is used to changed private data for class instance.
            Albo posbile to use private methods
@note       ...
'''
class CartypePropertiesSatic:
    numCars = 0
    brandOnSale = ""
    listCars = []
    def GetClassInfo()->None:
        print("=================", end= '\n')
        print("Number of cars: ", CartypePropertiesSatic.numCars, end= '\n')
        print("Car list: ", CartypePropertiesSatic.listCars, end= '\n')
        print("=================", end= '\n')
        return None
    
    def __init__(self, brand:str, model:str, isonsale:bool) -> None:
        self.brand = brand
        self.model = model
        self.__isonsale = isonsale
        CartypePropertiesSatic.numCars = CartypePropertiesSatic.numCars + 1
        CartypePropertiesSatic.listCars.append(brand)
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
        if(CartypePropertiesSatic.brandOnSale == self.brand):
            self.__isonsale = newStatus
            print("{}: Status changed!".format(self.brand), end='\n')
            return True
        else:
            print("{}: Status unchanged!".format(self.brand), end='\n')
            return False
        
    #Class property
    PropertyOnSale = property(GetOnSale, SetOnSale, None, "Only actual promo posible!")

    @classmethod
    def ReadFromText(cls, aText:str, splitMark:str)->list:
        if(len(splitMark) != 1):
            return []
        return cls(*aText.split(splitMark))
    
    @staticmethod
    def Convert_KM_KW(inKM:float)->float:
        return (inKM * 1.341)
    
    @staticmethod
    def Convert_KW_KM(inKM:float)->float:
        return (inKM * 0.736)
    
    def ReadFromText1(aText:str, splitMark:str)->list:
        if(len(splitMark) != 1):
            return []
        return aText.split(splitMark)
#--------------------------------------------------------------------------------------
def Call_CartypePropertiesSatic()->None:

    strObj = "Ford;Focus;True"
    myFord = CartypePropertiesSatic.ReadFromText(strObj, ';')
    myFord.GetInfo()

    kilowat = CartypePropertiesSatic.Convert_KM_KW(200)
    print("Kilowat= ", kilowat)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Cartype, decorators
@brief      Property is used to changed private data for class instance.
            Albo posbile to use private methods
@note       ...
'''
class CartypeDecorators:
    numCars = 0
    brandOnSale = ""
    listCars = []

    @classmethod
    def ReadFromText(cls, aText:str, splitMark:str)->list:
        if(len(splitMark) != 1):
            return []
        return cls(*aText.split(splitMark))

    def GetClassInfo()->None:
        print("=================",  end= '\n')
        print("Number of cars: ",   CartypeDecorators.numCars, end= '\n')
        print("Car list: ",         CartypeDecorators.listCars, end= '\n')
        print("=================",  end= '\n')
        return None
    
    def GetInfo(self)->None:
        print("=================",          end= '\n')
        print("Brand: ",        self.brand, end= '\n')
        print("Model: ",        self.model, end= '\n')
        print("Is on sale:",    self.__isonsale, end='\n')
        print("=================",  end= '\n')
        return None
    
    def __init__(self, brand:str, model:str, isonsale:bool) -> None:
        self.brand = brand
        self.model = model
        self.__isonsale = isonsale
        CartypeDecorators.numCars = CartypeDecorators.numCars + 1
        CartypeDecorators.listCars.append(brand)
        return None
    
    @property # Odwoływanie sie do właściwosci przez nazwę
    def PropertyOnSale(self)->bool:
        return self.__isonsale
    
    @PropertyOnSale.setter #Logika do ustawiania atrybutu
    def PropertyOnSale(self, newStatus:bool)->bool:
        if(CartypeDecorators.brandOnSale == self.brand):
            self.__isonsale = newStatus
            print("{}: Status changed!".format(self.brand), end='\n')
            return True
        else:
            print("{}: Status unchanged!".format(self.brand), end='\n')
            return False
        
    @PropertyOnSale.deleter
    def PropertyOnSale(self)->None:
        self.__isonsale = None
        return None
    
    @property
    def CarTitle(self)->None:
        print("Brand: {}, model: {}".format(self.brand, self.model))
        return None
#--------------------------------------------------------------------------------------
def Call_CartypeDecorators()->None:

    strObj = "Ford;Focus;True"
    myFord = CartypePropertiesSatic.ReadFromText(strObj, ';')
    myFord.GetInfo()
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       CartypeDynamicAddMethods
@brief      ...
@note       ...
'''
class CartypeDynamicAddMethods:
    numCars = 0
    brandOnSale = ""
    listCars = []
    def GetClassInfo()->None:
        print("=================", end= '\n')
        print("Number of cars: ", CartypeDynamicAddMethods.numCars, end= '\n')
        print("Car list: ", CartypeDynamicAddMethods.listCars, end= '\n')
        print("=================", end= '\n')
        return None
    
    def __init__(self, brand:str, model:str, isonsale:bool) -> None:
        self.brand = brand
        self.model = model
        self.__isonsale = isonsale
        CartypeDynamicAddMethods.numCars = CartypeDynamicAddMethods.numCars + 1
        CartypeDynamicAddMethods.listCars.append(self)
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
        if(CartypeDynamicAddMethods.brandOnSale == self.brand):
            self.__isonsale = newStatus
            print("{}: Status changed!".format(self.brand), end='\n')
            return True
        else:
            print("{}: Status unchanged!".format(self.brand), end='\n')
            return False
        
    #Class property
    PropertyOnSale = property(GetOnSale, SetOnSale, None, "Only actual promo posible!")
#--------------------------------------------------------------------------------------
import csv
def ExportFile_CSV_static(fullPath:str, heder:str, data:str)->bool:
    with open(fullPath, 'a', ) as file:
        myWriter = csv.writer(file, delimiter= ',', quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        myWriter.writerow(heder)
        myWriter.writerow(data)
    print("Data write and file closed", end= '\n')
    return True
#---------------
import types
def ExportFile_CSV_class(cls:CartypeDynamicAddMethods, fullPath:str)->bool:
    with open(fullPath, 'a', ) as file:
        myWriter = csv.writer(file, delimiter= ',', quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        myWriter.writerow(("Brand","Model","isOnSale"))
        for i in cls.listCars:
            myWriter.writerow((i.brand, i.model, str(i.PropertyOnSale)))

    print("Class method - Data write and file closed", end= '\n')
    return True
#---------------
def ExportFile_CSV_Instance(self, fullPath:str)->bool:
    with open(fullPath, 'a', ) as file:
        myWriter = csv.writer(file, delimiter= ',', quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        myWriter.writerow(("Brand","Model","isOnSale"))
        myWriter.writerow((self.brand, self.model, str(self.PropertyOnSale)))

    print("Class method - Data write and file closed", end= '\n')
    return True
#--------------------------------------------------------------------------------------
def Call_CartypeDynamicAddMethods1()->None:
    myFord = CartypeDynamicAddMethods("Ford", "Focus", False)
    myFiat = CartypeDynamicAddMethods("Fiat", "500", False)

    fullDir = "E:/Dokumenty/testFiles/Ford.csv"
    header = ("Brand","Model","isOnSale")
    data = (myFord.brand, myFord.model, str(myFord.PropertyOnSale))
    ExportFile_CSV_static(fullDir, header, data)

    fullDir = "E:/Dokumenty/testFiles/Fiat.csv"
    header = ("Brand","Model","isOnSale")
    data = (myFiat.brand, myFiat.model, str(myFiat.PropertyOnSale))
    ExportFile_CSV_static(fullDir, header, data)
    return None
#---------------
def Call_CartypeDynamicAddMethods2()->None:
    #CartypeDynamicAddMethods.ExportToFileCSV = ExportFile_CSV_class - Dont work
    CartypeDynamicAddMethods.ExportToFileCSV = types.MethodType(ExportFile_CSV_class, CartypeDynamicAddMethods)

    myFord = CartypeDynamicAddMethods("Ford", "Focus", False)
    myFiat = CartypeDynamicAddMethods("Fiat", "500", False)

    CartypeDynamicAddMethods.ExportToFileCSV("E:/Dokumenty/testFiles/Class.csv")
    return None
#---------------
def Call_CartypeDynamicAddMethods3()->None:
    myFord = CartypeDynamicAddMethods("Ford", "Focus", False)
    myFiat = CartypeDynamicAddMethods("Fiat", "500", False)

    myFord.ExportToFileCSV = types.MethodType(ExportFile_CSV_Instance, myFord)
    myFiat.ExportToFileCSV = types.MethodType(ExportFile_CSV_Instance, myFiat)

    myFord.ExportToFileCSV("E:/Dokumenty/testFiles/ClassInstFord.csv")
    myFiat.ExportToFileCSV("E:/Dokumenty/testFiles/ClassInstFiat.csv")
    return None
#=======================================================================================================================================

if (__name__ == "__main__"):
    Call_CartypeDynamicAddMethods3()
else:
    pass