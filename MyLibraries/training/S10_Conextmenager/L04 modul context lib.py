# Biblioteka umożliwiająca umieszczenia dekoratoróa aby pracować z kontekst menagerem
from contextlib import contextmanager

'''
Biblioteki słurzace do zamytania obiektów
'''
from urllib.request import urlopen
from contextlib import closing
import os

from contextlib import suppress

class Door():
    '''
    Obsługa kontekst menagera za pomocą dekoratorów
    '''

    def __init__(self, where):
        self.where = where
        return None

    def open(self):
        print("Opening door to the {}".format(self.where))
        return None

    def close(self):
        print('Closing door to the {}'.format(self.where))
        return None

@contextmanager
def OpenAndClose(obj):
    '''
    sztuczka za pomocy generatora aby zamrozic obiekt
    Dodadkowo udekorowana dekoratorem aby korzystac z kontekst menagera bez tworzenia metod w samej klasie
    '''
    obj.open()
    yield obj
    obj.close()
    return None

@contextmanager
def OnlyClose(obj):
    '''
    Fukcja która tylko zamyka jest to odchudzona wersja poprzedniej funkcji
    '''
    yield obj
    obj.close()
    return None

def RemoveFile(path):
    with suppress(FileNotFoundError):
        os.remove(path)
        print(">> File removed")

    return None

def PrintToTxtFile():
    '''
    Funkcja ta zamiast działac jak instrukcja print()
    Zapisuje wsztkie dane do pliku log na dysku
    '''
    from contextlib import redirect_stdout
    path = r'C:\Users\User\Documents\Python\Course02_PythonPL\InitFiles\log.txt'
    file = open(path,'w')
    with redirect_stdout(file):
        print('welcome to CryNetSystem')
        d = Door('Raj')
        d.open()
        d.close()

    return None

def Excercise():
    '''
    Excercise from udemy on this
    '''
    class FileFromWeb:

        def __init__(self, url, tmp_file):
            self.url = url
            self.tmp_file = tmp_file

        def download_file(self):
            response = requests.get(self.url)
            with open(self.tmp_file, 'wb') as f:
                f.write(response.content)
            return self

        def close(self):
            if os.path.isfile(self.tmp_file):
                os.remove(self.tmp_file)

    f = FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref1.zip')
    f.download_file()

    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)

        #os.remove(f.tmp_file)

    return None


def main1():

    DoorToHell = Door('Hell')
    DoorToHell.open()
    DoorToHell.close()

    DoorToParadise = Door('Paradise')
    DoorToParadise.open()
    DoorToParadise.close()

    return None

def main2():
    with OpenAndClose(Door('Hell')) as door:
        print('we have door to the {}'.format(door.where))
    return None

def main3():
    with OnlyClose(Door('Hell')) as door:
        door.open()
        print('we have door to the {}'.format(door.where))
    return None

RemoveFile(r'C:\Users\User\Documents\Python\Course02_PythonPL\InitFiles\Plik_do_usuniecia.txt')

PrintToTxtFile()
