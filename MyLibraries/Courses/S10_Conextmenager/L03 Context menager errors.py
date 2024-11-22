import os
import zipfile
import requests

'''*****************************************************************************************
@brief  
'''
class InitFile():
    className:str = __name__
    '''*************************************************************************************
    @brief  Inicialzacja klasy TxtParemeters
    '''
    def __init__(self, in_path:str):
        print(">> InitFile::__Init___ -  started")

        self.path = in_path
        self.parameters:dict = {}
        self.ReadFromDisc()

        print(">> InitFile::__Init___ -  finished")
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def __enter__(self):
        print(">> __enter__()")
        return self
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Metoda wykonywana przy "with:"
            Jesli zwracajne jest false to błąd nie jest zwracany przez silnik
    '''
    def __exit__(self, exc_type, exc_val, exc_traceback)->bool:
        print(">> __exit__()")

        print(">> exc_type= ", exc_type)
        print(">> exc_val= ", exc_val)
        print(">> exc_traceback= ", exc_traceback)

        if(exc_traceback == OSError):
            return False
        else:
            return True
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Czytanie parametrów z dysku oraz dodawanie ich do słownika
    '''
    def ReadFromDisc(self)->None:
        if(os.path.isfile(self.path)):
            print(">> File exist", end= '\n')
        else:
            print(">> File not exist", self.path, end= '\n')
            print(">> File will be created", self.path, end= '\n')
            return None
        
        with open(self.path) as myFile:
            for line in myFile:
                textList:list = str(line).replace('\n', '').split('=')
                self.parameters[textList[0]] = textList[1]

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Sprawdzanie czy zadany klucz istnieje
    '''
    def ReadParameter(self, key:str):
        if(key in self.parameters.keys()):
            return self.parameters[key]
        else:
            return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Dodawanie nowego parametru
    '''
    def WriteParemeter(self, key:str, value:str)->None:
        self.parameters[key] = value
        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Zapisywanie parametrów na dysku
    '''
    def SaveOnDisc(self)->None:
        with open(self.path, 'w') as myFile:
            for k, v in self.parameters.items():
                myFile.writelines("{}={}\n".format(k,v))
        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    #--------------------------------------------------------------------------------------
#==========================================================================================
def CALL_InitFile_errors_test1()->None:
    
    with InitFile("E:/Dokumenty/testFiles/*context-menger-errors.ini") as myInitFile:
        myInitFile.WriteParemeter("mode","strict")
        myInitFile.WriteParemeter("loglevel", "light")
        myInitFile.SaveOnDisc()

    return
#==========================================================================================
#==========================================================================================
def CALL_InitFile_errors_test2()->None:
    pass
#=========================================================================================

if(__name__ == "__main__"):
    CALL_InitFile_errors_test1()
else:
    pass