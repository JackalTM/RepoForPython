import io
import zipfile
from shutil import make_archive as Shutil_make_archive
from shutil import unpack_archive as Shutil_unpack_archive
'''*************************************************************************************
@name       FileLocations
@brief      ...
@note       ... 
'''
class FileLocations:
    FULL_DIR_TOZIP = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/zip_unzip/to_zip"
    FULL_DIR_UNZIP = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/zip_unzip/to_unzip"

    MAIN_DIR = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python"

    LOC_DIR_TOZIP = "MyLibraries/training/S05_Modules/zip_unzip/to_zip"
    LOC_DIR_UNZIP = "MyLibraries/training/S05_Modules/zip_unzip/to_unzip"

    @staticmethod
    def MakeFullDir_TOZIP(fileName : str) -> str:
        return (FileLocations.FULL_DIR_TOZIP + "/" + fileName)
    @staticmethod
    def MakeFullDir_UNZIP(fileName : str) -> str:
        return (FileLocations.FULL_DIR_UNZIP + "/" + fileName)
    
    @staticmethod
    def MakeLocDir_TOZIP(fileName : str) -> str:
        return (FileLocations.LOC_DIR_TOZIP + "/" + fileName)
    @staticmethod
    def MakeLocDir_UNZIP(fileName : str) -> str:
        return (FileLocations.LOC_DIR_UNZIP + "/" + fileName)
#===========================================================================================
    
'''*************************************************************************************
@name       FileOperation
@brief      Operation on opened file 
@param[in]  OpenedFile - Opened text file 
@note       This function is wraped
@return     None 
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
    return OpenedFile
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

#=======================================================================================
def CALL_zip_test() -> None:
    """
    File extract problem
    Entire location is compresed
    After extraction whole directory is extracted
    """
    destinationFile = FileLocations.MakeFullDir_TOZIP("zip_test.zip")

    sourceFile1 = FileLocations.MakeFullDir_TOZIP("test.txt")
    sourceFile2 = FileLocations.MakeFullDir_TOZIP("test1.txt")
    sourceFile3 = FileLocations.MakeFullDir_TOZIP("test2.txt")

    print("Destination file: {}".format(destinationFile))
    print("Inclue file:      {}".format(sourceFile1))
    print("Inclue file:      {}".format(sourceFile2))
    print("Inclue file:      {}".format(sourceFile3))

    compresedFile = zipfile.ZipFile(file= destinationFile, mode= 'w')
    compresedFile.write(filename= sourceFile1, compress_type= zipfile.ZIP_DEFLATED)
    compresedFile.write(filename= sourceFile2, compress_type= zipfile.ZIP_DEFLATED)
    compresedFile.write(filename= sourceFile3, compress_type= zipfile.ZIP_DEFLATED)

    compresedFile.close()

    return None
#=======================================================================================

"""*************************************************************************************
base_name   - Path where compresed file will be placed
format      - File format example .zip 
root_dir    - Path to folder that will be compresed
base_dir    - Directory widhin direcory 
"""
def CALL_Shutil_make_archive() -> None:

    base_name   = FileLocations.MakeLocDir_UNZIP("newZIP")
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
"""
def CALL_Shutil_unpack_archive() -> None:

    filename    = FileLocations.MakeLocDir_UNZIP("newZIP.zip")
    extract_dir = FileLocations.LOC_DIR_UNZIP
    format      = "zip"

    Shutil_unpack_archive(filename= filename, extract_dir= extract_dir, format= format)

    return None
#=======================================================================================

#=======================================================================================
def CALL_unzip_test() -> None:

    sourceFile = FileLocations.MakeFullDir_TOZIP("zip_test.zip")
    destinationFolder = FileLocations.MAIN_DIR_UNZIP

    print("Source file: {}".format(sourceFile))
    print("Destination: {}".format(destinationFolder))

    zipObj = zipfile.ZipFile(file= sourceFile, mode= 'r')
    zipObj.extractall(path= destinationFolder)

    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_Shutil_unpack_archive()
else:
    pass