import io
import os
import zipfile
from shutil import make_archive as Shutil_make_archive
from shutil import unpack_archive as Shutil_unpack_archive
'''*************************************************************************************
@name       FileLocations
@brief      File location static class
@note       Contain static methods and constants
'''
class FileLocations:
    mainDir = os.getcwd()

    LOC_DIR_TOZIP = "MyLibraries/training/S05_Modules/zip_unzip/to_zip"
    LOC_DIR_UNZIP = "MyLibraries/training/S05_Modules/zip_unzip/to_unzip"

    @staticmethod
    def SetCurrentPath(somePath : str)->None:
        return None

    @staticmethod
    def MakeFullDir_TOZIP(fileName : str) -> str:
        fullPath = FileLocations.mainDir + '/'
        fullPath = fullPath + FileLocations.LOC_DIR_TOZIP + '/'
        fullPath = fullPath + fileName
        return fullPath
    @staticmethod
    def MakeFullDir_UNZIP(fileName : str) -> str:
        fullPath = FileLocations.mainDir + '/'
        fullPath = fullPath + FileLocations.LOC_DIR_UNZIP + '/'
        fullPath = fullPath + fileName
        return fullPath
    
    @staticmethod
    def MakeLocDir_TOZIP(fileName : str) -> str:
        return (FileLocations.LOC_DIR_TOZIP + "/" + fileName)
    @staticmethod
    def MakeLocDir_UNZIP(fileName : str) -> str:
        return (FileLocations.LOC_DIR_UNZIP + "/" + fileName)
#===========================================================================================
    
'''*****************************************************************************************
@name       FileOperation
@brief      Operation on opened file 
@param[in]  io.TextIOWrapper : OpenedFile - Opened text file 
@note       This function is wraped
@return     io.TextIOWrapper : OpenedFile 
'''
def FileOperation(OpenedFile : io.TextIOWrapper) -> io.TextIOWrapper:
    print("FILE IS OPENED !!!!!")

    OpenedFile.write("test.txt\n")

    return OpenedFile
#=======================================================================================

'''*************************************************************************************
@name       PrintFileContent
@brief      Operation on opened file 
@param[in]  OpenedFile : io.TextIOWrapper - Opened text file 
@note       This function is wraped
@return     None 
'''
def PrintFileContent(OpenedFile : io.TextIOWrapper) -> None:
    for line in OpenedFile:
        print(line, end= '')
    return None
#=======================================================================================

'''*************************************************************************************
@name       OpenTextFile
@brief      ...
@param[in]  fullDir : str - Full direction to file
@param[in]  FileOperation : FileOperation - Function to operate on file 
@param[in]  mode : str = 'r' - Mode to wrok on file
@note       ... 
@return     None 
'''
def OpenTextFile(fullDir : str, FileOperation : FileOperation, mode : str = 'r') -> None:
    try:
        OpenedFile = open(fullDir, mode)

        OpenedFile = FileOperation(OpenedFile)

        OpenedFile.close()
    except FileNotFoundError:
        print("DIR error!")
        print(fullDir)

    return None
#=======================================================================================

'''*************************************************************************************
@name       TestZipFile
@brief      ...
@param[in]  name : str = "new.zip" 
@param[in]  fullDir : str = ""
@note       ... 
@return     None 
'''
def TestZipFile(fullZipName : str, fullFileName : str) -> None:
    try:
        compresedFile = zipfile.ZipFile(file= fullZipName)
        compresedFile.write(fullFileName)
        compresedFile.close()
    except:
        print("Wrong location or name")

    return None
#=======================================================================================

#=======================================================================================
def CALL_open_modyfi() -> None:
    OpenTextFile(FileLocations.MakeFullDir("test.txt"), FileOperation, mode= 'a+')
    return None
#=======================================================================================

"""*************************************************************************************
file        - File location to comprese object full direction
mode        - ('r', 'w', 'x', 'a')
instZipFile - zipfile.ZipFile(file= file, mode= mode)

filename        - Fille full name to comprese
compress_type   - zipfile.ZIP_DEFLATED
instZipFile.write(filename= filename, compress_type= compress_type)
"""
def CALL_zipfile_ZipFile_write() -> None:
    """
    File extract problem
    Entire location is compresed
    After extraction whole directory is extracted
    """
    file        = FileLocations.MakeLocDir_UNZIP("new_zipfile.zip")
    mode        = "w"
    instZipFile = zipfile.ZipFile(file= file, mode= mode)

    fileName1 = FileLocations.MakeLocDir_TOZIP("test.txt")
    fileName2 = FileLocations.MakeLocDir_TOZIP("test1.txt")
    fileName3 = FileLocations.MakeLocDir_TOZIP("test2.txt")
    instZipFile.write(filename= fileName1, compress_type= zipfile.ZIP_DEFLATED)
    instZipFile.write(filename= fileName2, compress_type= zipfile.ZIP_DEFLATED)
    instZipFile.write(filename= fileName3, compress_type= zipfile.ZIP_DEFLATED)

    instZipFile.close()

    print("Comprese files Method test:")
    print("instZipFile - zipfile.ZipFile(file= file, mode= mode)")
    print("instZipFile.extractall(path= path)")

    return None
#=======================================================================================

"""*************************************************************************************
file        - File location to comprese object full direction
mode        - ('r', 'w', 'x', 'a')
instZipFile - zipfile.ZipFile(file= file, mode= mode)

path        - Path to unpact file
instZipFile.extractall(path= path)
"""
def CALL_zipfile_ZipFile_extractall() -> None:

    file    = FileLocations.MakeLocDir_UNZIP("new_zipfile.zip")
    mode    = 'r'
    instZipFile  = zipfile.ZipFile(file= file, mode= mode)

    path    = FileLocations.LOC_DIR_UNZIP
    instZipFile.extractall(path= path)

    print("Extract files Method test:")
    print("instZipFile - zipfile.ZipFile(file= file, mode= mode)")
    print("instZipFile.extractall(path= path)")

    return None
#=======================================================================================

"""*************************************************************************************
base_name   - Path where compresed file will be placed
format      - File format example .zip 
root_dir    - Path to folder that will be compresed
base_dir    - Directory widhin direcory 
Tested OK
"""
def CALL_Shutil_make_archive() -> None:

    base_name   = FileLocations.MakeLocDir_UNZIP("Shutil_make_archive_ZIP")
    format      = "zip"
    root_dir    = FileLocations.FULL_DIR_TOZIP
    base_dir    = ""

    name = Shutil_make_archive(base_name= base_name, format= format, root_dir= root_dir)
    print("file name = {}".format(name))

    return None
#=======================================================================================

"""*************************************************************************************
filename    - Full name to file with direction
extract_dir - Direction where extract file
format      - Compres format
Tested OK
"""
def CALL_Shutil_unpack_archive() -> None:

    filename    = FileLocations.MakeLocDir_UNZIP("Shutil_make_archive_ZIP.zip")
    extract_dir = FileLocations.LOC_DIR_UNZIP
    format      = "zip"

    Shutil_unpack_archive(filename= filename, extract_dir= extract_dir, format= format)

    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_zipfile_ZipFile_write()
    CALL_zipfile_ZipFile_extractall()
else:
    pass