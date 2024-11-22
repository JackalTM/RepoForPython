# Biblioteka umożliwiająca umieszczenia dekoratoróa aby pracować z kontekst menagerem
from contextlib import contextmanager

'''************************************************************************************
Biblioteki słurzace do zamytania obiektów
'''
from urllib.request import urlopen
from contextlib import closing
import os

from contextlib import suppress

'''*************************************************************************************
@brief  Obsługa kontekst menagera za pomocą dekoratorów
'''
class Door():

    def __init__(self, where:str):
        self.where = where
        return None

    def open(self):
        print("Opening door to the {}".format(self.where))
        return None

    def close(self):
        print('Closing door to the {}'.format(self.where))
        return None
#=======================================================
# Otwieranie poprzez metode open oraz close
def CALL_Door_test1()->None:
    hevenDoor = Door("Heven")
    hellDoor = Door("Hell")

    hevenDoor.open()
    hevenDoor.close()

    hellDoor.open()
    hellDoor.close()

    return
#======================================================================================

'''*************************************************************************************
@brief  Metoda "With" za pomocy generatora aby zamrozic obiekt
        Dodadkowo udekorowana dekoratorem aby korzystac z kontekst menagera bez tworzenia metod w samej klasie

@note   Otwieranie poprzez contekst manager
'''
@contextmanager
def OpenAndClose(refDoor:Door):
    refDoor.open()
    yield refDoor
    refDoor.close()
    return None
#======================================================================================
def CALL_Door_test2()->None:

    with OpenAndClose(Door("Time portal")) as myPortal:
        print("Door open to -> ", myPortal.where)

    return None
#======================================================================================

'''*************************************************************************************
@brief  Metoda "With" za pomocy generatora aby zamrozic obiekt
        Dodadkowo udekorowana dekoratorem aby korzystac z kontekst menagera bez tworzenia metod w samej klasie

@note   Fukcja która tylko zamyka jest to odchudzona wersja poprzedniej funkcji
'''
@contextmanager
def OnlyOpen(refDoor:Door):
    refDoor.open()
    yield refDoor
    return None
#-----------------------------
@contextmanager
def OnlyClose(refDoor:Door):
    yield refDoor
    refDoor.close()
    return None
#======================================================================================
def CALL_Door_test3()->None:

    with OnlyClose(Door("Time and space portal | test1")) as myPortal:
        myPortal.open()
        print("Door open to -> ", myPortal.where)

    with OnlyOpen(Door("Time and space portal | test2")) as myPortal:
        print("Door open to -> ", myPortal.where)
        myPortal.close()

    return None
#======================================================================================

'''*************************************************************************************
@brief  Wykorzystanie dla usuwania plików plików
        Przydatne jesli usuwamy plik który nie istnieje
'''
def RemoveFile(path:str)->bool:
    tBool = False
    with suppress(FileNotFoundError):
        os.remove(path)
        print(">> File removed")
        tBool = True

    return tBool

def CreateFile(path:str)->bool:
    file = open(file= path, mode= 'w') 
    file.close()
    print(">> File created")

#======================================================================================
def CALL_RemoveFile_test1()->None:

    CreateFile("E:/Dokumenty/testFiles/modulcontextlib.txt")
    RemoveFile("E:/Dokumenty/testFiles/modulcontextlib.txt")

    return None
#======================================================================================
def CALL_PrintToTxtFile_test1():
    '''
    Funkcja ta zamiast działac jak instrukcja print()
    Zapisuje wsztkie dane do pliku log na dysku
    '''
    from contextlib import redirect_stdout
    path = "E:/Dokumenty/testFiles/redirect_stdout.txt"
    file = open(path,'w')
    with redirect_stdout(file):
        print('welcome to CryNetSystem')
        d = Door('Raj')
        d.open()
        d.close()

    return None
#======================================================================================
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

if(__name__ == "__main__"):
    CALL_PrintToTxtFile_test1()
else:
    pass
