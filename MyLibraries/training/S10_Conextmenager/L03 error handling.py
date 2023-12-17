import os
import zipfile
import requests

class IniFiles():

    def __init__(self, path):
        '''
        Initialazing instance
        '''
        print(">> init start")
        self.path = path
        self.par = {}
        #self.ReadFromTxt()

        return None

    def ReadFromTxt(self):
        '''
        Reding from txt file
        '''
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

    def ReadParameters(self, key):
        '''
        return paremeters if it is in dictionary
        '''
        if key in self.par.keys():
            return self.par[key]

        else:
            print('>> Key does not exist')

        return None

    def WriteParametrs(self, key, val):
        '''
        Write parameters in class variable
        '''
        self.par[key] = val

        return None

    def WriteToTxt(self):
        '''
        Write all paremeters in txt file on disk
        '''
        file = open(self.path, 'a')
        #===========================
        for i in self.par:
            key = i
            val = self.par[i]
            file.write('{}={}\n'.format(key,val))
        #===========================
        file.close()

        return None

    def ShowPar(self):
        '''
        Delete all data in class instance variable
        '''
        for i in self.par:
            key = i
            val = self.par[i]
            print('{} = {}'.format(key, val))

        return None

    def __enter__(self):
        '''
        enable to work with "with" method
        '''
        print('>> Enter method')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        exit from "with" method
        '''
        if(exc_type or exc_val or exc_tb):

            print('Type error       => {}'.format(exc_type))
            print('Value error      => {}'.format(exc_val))
            print('Trace bug error  => {}'.format(exc_tb))

        else:
            print('>> Exit method no error')

        if(exc_type == OSError):
            return False
        else:
            return True

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


def Main1():

    instPar = IniFiles(path= 'C:/Users/User/Documents/Python/Course02_PythonPL/InitFiles/txt1.txt')

    #instPar.WriteParametrs('A', '0x0000_0000')
    #instPar.WriteParametrs('B', '0xFFFF_FFFF')
    #instPar.WriteToTxt()

    instPar.ReadFromTxt()
    instPar.ShowPar()

    return None


def Main2():
    with IniFiles(path= 'C:/Users/User/Documents/Python/Course02_PythonPL/InitFiles/txt1.txt') as instPar:
        instPar.ReadFromTxt()
        instPar.ShowPar()

        print(1/0)


Main2()
