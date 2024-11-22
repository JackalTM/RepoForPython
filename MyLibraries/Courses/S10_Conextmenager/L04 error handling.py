import os
import zipfile
import requests

'''*************************************************************************************
@brief  
'''
class IniFiles():

    '''*************************************************************************************
    @brief  
    '''
    def __init__(self, path:str):
        print(">> __init__() start")

        self.path = path
        self.par = {}

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  enable to work with "with" method
    '''
    def __enter__(self):
        print('>> __enter__()')
        return self
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  exit from "with" method  
    '''
    def __exit__(self, exc_type:str, exc_val:str, exc_tb:str)->bool:
        if(exc_type or exc_val or exc_tb):

            print(">> __exit__() ERROR!")
            print('Type error       => {}'.format(exc_type))
            print('Value error      => {}'.format(exc_val))
            print('Trace bug error  => {}'.format(exc_tb))

        else:
            print('>> __exit__() no error')

        if(exc_type == OSError):
            return False
        else:
            return True
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Reding from txt file
    '''
    def ReadFromTxt(self)->None:
        if os.path.isfile(self.path):
            print('>> File exist')
            f = open(self.path)
            for l in f:
                #Remove new line mark and place empty mark
                KeyValue = l.replace('\n', '').split('=')
                key = KeyValue[0]
                val = KeyValue[1]
                self.par[ key ] = val
            f.close()
        else:
            print('>> File does not exist')

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def ReadParameters(self, key)->None:
        if key in self.par.keys():
            return self.par[key]

        else:
            print('>> Key does not exist')

        return None
    #--------------------------------------------------------------------------------------
    
    '''*************************************************************************************
    @brief  Write parameters in class variable
    '''
    def WriteParametrs(self, key:str, val:str)->None:
        self.par[key] = val
        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  Write all paremeters in txt file on disk
    '''
    def WriteToTxt(self)->None:
        file = open(self.path, 'a')
        #===========================
        for i in self.par:
            key = i
            val = self.par[i]
            file.write('{}={}\n'.format(key,val))
        #===========================
        file.close()

        return None
    #--------------------------------------------------------------------------------------

    '''*************************************************************************************
    @brief  
    '''
    def ShowPar(self)->None:
        for i in self.par:
            key = i
            val = self.par[i]
            print('{} = {}'.format(key, val))

        return None
    #--------------------------------------------------------------------------------------
#==========================================================================================
def CALL_IniFiles_Test1()->None:

    instPar = IniFiles(path= "E:/Dokumenty/testFiles/context-menager-errors.ini")

    #instPar.WriteParametrs('A', '0x0000_0000')
    #instPar.WriteParametrs('B', '0xFFFF_FFFF')
    #instPar.WriteToTxt()

    instPar.ReadFromTxt()
    instPar.ShowPar()

    return None
#==========================================================================================
def CALL_IniFiles_Test2()->None:
    with IniFiles(path= 'C:/Users/User/Documents/Python/Course02_PythonPL/InitFiles/txt1.txt') as instPar:
        instPar.ReadFromTxt()
        instPar.ShowPar()

        print(1/0)
#==========================================================================================

'''*************************************************************************************
@brief  
'''
def Exercise():
    class FileFromWeb:

        def __init__(self, url, tmp_file):
            self.url = url
            self.tmp_file = tmp_file

        def __enter__(self):
            #download
            response = requests.get(self.url)
            with open(self.tmp_file, 'wb') as f:
                f.write(response.content)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass


    with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:

            with zipfile.ZipFile(f.tmp_file, 'r') as z:
                a_file = z.namelist()[0]
                print(a_file)
                os.chdir('c:/temp')
            z.extract(a_file, '.', None)

    return None
#==========================================================================================

if(__name__ =="__main__"):
    CALL_IniFiles_Test1()
else:
    pass
