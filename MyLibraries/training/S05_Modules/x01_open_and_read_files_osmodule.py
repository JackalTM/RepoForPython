'''*************************************************************************************
@name       SetCurrentOSPath
@brief      Set current directory to demand one
@param[in]  toPath - Demand directory 
@note       ... 
@return     None
'''
def SetCurrentOSPath(toPath : str):
    currentCD = os.getcwd()
    print("CD before: \t{}".format(currentCD))
    try:
        currentCD = currentCD + "/" + toPath
        os.chdir(toPath)
    except:
        print("Wrong PATH!")
        return None

    print("CD after: \t{}".format(os.getcwd()))

    return None
#=======================================================================================

'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
import os
def CALL_os_module_current_directory():
    currectPath = os.getcwd()
    print("Curent working directory:")
    print(currectPath)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_OpenFile
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_OpenFile():
    FULL_DIR = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/files_folder/some_file.txt"
    mainDir = os.getcwd()
    fullDir = "{}\{}".format(mainDir, "files_folder\somefile.txt")
    
    try:
        myFile = open(FULL_DIR, 'w+')
        myFile.write("File directory: {}".format(FULL_DIR))
        myFile.close()
    except:
        print("Direction error:")
        print(fullDir)
        print(FULL_DIR)
    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_ListALlFilesInFolder
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_ListALlFilesInFolder():
    currentDir = os.getcwd()
    fileList = os.listdir()
    print("DIR: {}".format(currentDir))
    print(fileList)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CAll_shutil_module
@brief      This functionality can move file to other filder 
@param[in]  ...
@note       In this function file is moved between folders for test
@return     ...
'''
import shutil
def CAll_shutil_module():
    FULL_DIR_1 = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/files_folder_1/"
    FULL_DIR_2 = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/files_folder_2/"
    FILE_NAME = "some_file.txt"

    listDir1 = os.listdir(FULL_DIR_1)
    listDir2 = os.listdir(FULL_DIR_2)

    if FILE_NAME in listDir1:
        print("File found in {}".format(FULL_DIR_1))
        print("Moved to {}".format(FULL_DIR_2))
        srcCD = FULL_DIR_1 + FILE_NAME
        shutil.move(src= srcCD, dst= FULL_DIR_2)

    elif FILE_NAME in listDir2:
        print("File found in {}".format(FULL_DIR_2))
        print("Moved to {}".format(FULL_DIR_1))
        srcCD = FULL_DIR_2 + FILE_NAME
        shutil.move(src= srcCD, dst= FULL_DIR_1)

    else:
        print("No file {} is found".format(FILE_NAME))

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_os_walk
@brief      os.walk() make tree object with directins to folders and files
@param[in]  ...
@note       This method is usefull with searching folder and fiels.
            Every folder from path is opened and cheked.
            This functionality need tuple unpacking.
@return     ...
'''
def CALL_os_walk():

    myDirectory = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MaterialsPythonBootcamp/Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/Example_Top_Level"
    for (folder, subFolder, files) in os.walk(myDirectory):
        print("Currently looking: {}".format(folder))
        print('\n')

        print("Subfolders: ")
        for sf in subFolder:
            print("\t Subfolder: {}".format(sf))

        print('\n')
        print("The files are:")
        for f in files:
            print("\t File: {}".format(f))

        print('\n')

    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_os_walk()
else:
    pass