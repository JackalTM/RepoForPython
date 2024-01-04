import os
import requests

def SearchFiles(iFilesPath, iStrSearch, iFileExten):
    """
    Generator dla nazw plików zawieracjących okreslony napis
    """
    print(">> File extension -> .{}".format(iFileExten))
    print(">> String to find -> '{}'".format(iStrSearch))
    print(">> Files found:   -> ")
    for (dirPath, dirNames, fileNames) in os.walk(iFilesPath):
        """
        print(dirPath)
        print(dirNames)
        print(fileNames)
        """
        for name in fileNames:
            if (name.endswith(iFileExten)):
                #tempDir = '{}/{}'.format(dirPath, name)
                fullDir = os.path.join(dirPath, name)
                f = open(fullDir)
                for line in f:
                    if iStrSearch in line:
                        outValue = fullDir
                        break
                yield outValue
                f.close()
            else:
                pass
            """
            f = open(os.path.join(dirPath, name))
            f.close()
            """


    return None

'''
Generator który skłąda sie z dwuch osobnych generatorów.
'''
def GenFilesWithExtension(iMainPath, iExtension):
    i = 0
    for (dirPath, dirNames, fileNames) in os.walk(iMainPath):
        pass

    for name in fileNames:
        if(name.endswith(iExtension)):
            full = os.path.join(dirPath, name)
            yield full
        else:
            pass

    return None

def GenCheckFile(Generator, iStr):
    for file in Generator:
        f = open(file)
        for l in f:
            if (iStr in l):
                value = '{} -> {}'.format(file, iStr)
                yield value
            else:
                pass
        f.close()
    return None



#===============================
def Main():
    iFilesPath      = 'C:/Users/User/Documents/Python/AB_PythonAdvancedCurse/Curse02_10Generatory'
    iStrSearch      = 'AUG'
    iFileExten      = 'txt'
    #for i in SearchFiles(iFilesPath, iStrSearch, iFileExten):
     #   print(i)

    '''
     Generator jako parametr dla innego generatora
    '''
    for i in GenCheckFile(GenFilesWithExtension(iFilesPath, iFileExten), 'AUG'):
        print(i)
    return None
#===============================
Main()
