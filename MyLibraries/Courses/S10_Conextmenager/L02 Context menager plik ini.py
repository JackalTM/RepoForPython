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
    @brief  
    '''
    def __exit__(self, in_type:str, in_val:str, in_traceback):
        print(">> __exit__()")
        return None
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
def CALL_InitFile_test1()->None:
    myInitfile = InitFile("E:/Dokumenty/testFiles/context_manager.ini")
    myInitfile.WriteParemeter("version", "1")
    myInitfile.WriteParemeter("level","advanced")
    myInitfile.SaveOnDisc()

    del myInitfile

    myInitfile = InitFile("E:/Dokumenty/testFiles/context_manager.ini")
    print(myInitfile.parameters)
    print(myInitfile.ReadParameter("version"))
    print(myInitfile.ReadParameter("level"))
#----------------------------------------------
def CALL_InitFile_test2()->None:
    with InitFile("E:/Dokumenty/testFiles/context_manager.ini") as myFile:
        print(myFile.parameters)
        print(myFile.ReadParameter("version"))
        print(myFile.ReadParameter("level"))
#==========================================================================================

'''*****************************************************************************************
@brief  
'''
class TxtParemeters():
    '''*************************************************************************************
    @brief  Inicialzacja klasy TxtParemeters
    '''
    def __init__(self, in_path:str):
        print(">> TxtParemeters::__Init___ -  started")
        self.parameters = []
        self.path       = in_path
        print(">> TxtParemeters::__Init___ -  finished")
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Sprawdza czy scirzka istnieje oraz zamiena zamienia znaki oraz aktualizuje słownik
    '''
    def ReadFromTxt(self, in_path:str):
        print(">> TxtParemeters::ReadFromTxt - started")

        if(os.path.isfile(self.path)):

            f = open(self.path)
            for i in f:
                parts = i.replace("\n",'').split('=')
                parts = i.split('=')
                self.parameters[parts[0] - parts[1]]
            f.close()

        else:
            print(">> TxtParemeters::ReadFromTxt - File do not exist -> Exit")

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def ReadFromClass(self, key:int):
        '''
        Czy zadana nazwa klucza znajduje sie w liscie kluczy w słowniku parameters
        '''
        if(key in self.parameters.keys()):
            return self.parameters[key]
        else:
            print(">> Parameters Empty - > EXIT")
            return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def WriteToClass(self, key, value):
        '''
        Zapisywanie wartosci do klucza
        '''
        self.parameters[key] = value
        return None

    '''*************************************************************************************
    @brief  
    '''
    def WriteToTxt(self, fileName):
        '''
        Metoda ta pobiera wsztkie parametry oraz zapisuje je na dysku
        '''
        if fileName:
            fullPath = r'{}\{}'.format(self.parameters, fileName)

            f = open(fullPath,'w')
            for key, value in self.parameters:
                line = "{}={}\n".format(key, value)
                file.writelines(line)
            f.close()

        else:
            print(">> Parameters is empty")

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def __enter__(self):
        return self
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def __exit__(self, a, b, c):
        pass
        return None
    #--------------------------------------------------------------------------------------
#==========================================================================================
def CALL_TxtParameters():
    ini = TxtParemeters(path= r'C:\Users\User\Documents\Python\Course02_PythonPL\Nowy_folder')

    ini.WriteToClass(key= 'P1', value= 'V1')
    ini.WriteToClass(key= 'P2', value= 'V2')

    ini.WriteToTxt(fileName=  r'\txt1.txt')

    return None
#===========================================================================================

class FileFromweb():
    '''*************************************************************************************
    @brief  
    '''
    def __init__(self, url, tempFile):
        self.url        = url
        self.tempFile   = tempFile
        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def __enter__(self):
        # download
        response = requests.get(self.url)
        f = open(self.tempFile, 'wb')
        f.write(response.content)
        f.close()
        return self
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def __exit__(self, exc_type, exc_val, exc_tb):
        return None
    #--------------------------------------------------------------------------------------

#==========================================================================================
def CALL_FileFromweb():
    temp1 = ''
    temp2 = ''
    with FileFromweb(temp1, temp2) as f:

        with zipfile.ZipFile(f.tempFile, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            dire = ''
            os.chdir(dire)
            z.extract(a_file, '-', None)
#==========================================================================================

if(__name__ == "__main__"):
    CALL_InitFile_test2()
else:
    pass

