import os
import zipfile
import requests

class TxtParemeters():
    '''
    '''
    def __init__(self, path):
        print(">> Init started")
        self.parameters = []
        self.path       = path
        print('>> Init finished')

    def ReadFromTxt(self, path):
        '''
        Sprawdza czy scirzka istnieje oraz zamiena zamienia znaki oraz aktualizuje słownik
        '''
        print('>> read from txt started')
        if(os.path.isfile(self.path)):

            f = open(self.path)
            for i in f:
                parts = i.replace("\n",'').split('=')
                parts = i.split('=')
                self.parameters[parts[0] - parts[1]]
            f.close()

        else:
            print(">> File do not exist -> Exit")

        return None

    def ReadFromClass(self, key):
        '''
        Czy zadana nazwa klucza znajduje sie w liscie kluczy w słowniku parameters
        '''
        if(key in self.parameters.keys()):
            return self.parameters[key]
        else:
            print(">> Parameters Empty - > EXIT")
            return None

    def WriteToClass(self, key, value):
        '''
        Zapisywanie wartosci do klucza
        '''
        self.parameters[key] = value
        return None

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

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        pass
        return None

class FileFromweb():
    '''
    '''
    def __init__(self, url, tempFile):
        self.url        = url
        self.tempFile   = tempFile
        return None

    def __enter__(self):
        # download
        response = requests.get(self.url)
        f = open(self.tempFile, 'wb')
        f.write(response.content)
        f.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

def main1():
    ini = TxtParemeters(path= r'C:\Users\User\Documents\Python\Course02_PythonPL\Nowy_folder')

    ini.WriteToClass(key= 'P1', value= 'V1')
    ini.WriteToClass(key= 'P2', value= 'V2')

    ini.WriteToTxt(fileName=  r'\txt1.txt')



    return None

def main2():
    temp1 = ''
    temp2 = ''
    with FileFromweb(temp1, temp2) as f:

        with zipfile.ZipFile(f.tempFile, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            dire = ''
            os.chdir(dire)
            z.extract(a_file, '-', None)

main2()

