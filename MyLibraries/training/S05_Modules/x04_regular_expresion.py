import re as RegEx

'''*************************************************************************************
@name       FileLocations
@brief      ...
@note       ... 
'''
class FileLocations:
    DEFAULT_FILE_NAME = "phone_numbers.txt"
    MAIN_DIR = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/MyLibraries/training/S05_Modules/regex_files/"
    
    @staticmethod
    def MakeFullDir(fileName) -> str:
        return (FileLocations.MAIN_DIR + fileName)
#===========================================================================================
    
'''*****************************************************************************************
@name       OpenCloseFile
@brief      Open and close text file
@param[in]  None 
@note       Function to wrap
@return     None 
'''
def OpenCloseFile(fullName, RE_TestMethods) -> None:
    try:
      OpenedFile = open(file= fullName, mode= 'r')
      print("- File opened.")
    except FileNotFoundError:
      print("File not found: {}".format(fullName))
      print("Cheq the file directory!")
      return None

    RE_TestMethods(OpenedFile)

    OpenedFile.close()
    print("- File closed")

    return None
#=======================================================================================
    
'''*************************************************************************************
@name       RE_TestMethods_search
@brief      Test method RegEx.search()
@param[in]  OpenedFile - From OpenedFile function
@note       ... 
@return     None 
'''
def RE_TestMethods_search(OpenedFile) -> None:
    toFind = "48"
    lineNum = 0
    for line in OpenedFile:
        lineNum += 1
        print("- {} line : {}".format(lineNum,line), end= '\t')
        match = RegEx.search(pattern= toFind, string= line)
        print("re.search()= {}".format(match))

    return None
#=======================================================================================
'''*************************************************************************************
@name       RE_TestMethods_findall
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def RE_TestMethods_findall(OpenedFile) -> None:
    toFind = "48"
    lineNum = 0
    for line in OpenedFile:
        lineNum += 1
        print("- {} line : {}".format(lineNum,line))

        matches = RegEx.findall(pattern= toFind, string= line)
        for m in matches:
            print("matches = RegEx.findall: {}".format(m))

    return None
#=======================================================================================
    
'''*************************************************************************************
@name       RE_TestMethod_pattern_qualifiers
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def RE_TestMethod_pattern_qualifiers(OpenedFile) -> None:
  rePattern = "\d\d\d-\d\d\d-\d\d\d"
  lineNum = 0
  print("qualifier= {}".format(rePattern))
  for line in OpenedFile:
        lineNum += 1
        phoneNunObj = RegEx.search(pattern= rePattern, string= line)
        print("- {} RegEx.search()= {} | RegEx.search().group()= {}".format(lineNum, phoneNunObj, phoneNunObj.group()))

  return None 
#=======================================================================================

'''*************************************************************************************
@name       RE_TestMethod_pattern_quantifiers
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def RE_TestMethod_pattern_quantifiers(OpenedFile) -> None:
  rePattern = r"\d{2} \d{3}-\d{3}-\d{3}"
  lineNum = 0
  print("quantifier= {}".format(rePattern))
  for line in OpenedFile:
        lineNum += 1
        phoneNunObj = RegEx.search(pattern= rePattern, string= line)
        print("- {} RegEx.search()= {} | RegEx.search().group()= {}".format(lineNum, phoneNunObj, phoneNunObj.group()))

  return None 
#=======================================================================================

'''*************************************************************************************
@name       RE_TestMethod_pattern_or_wildcard
@brief      Compile patterc coded as groups "()"
@param[in]  None 
@note       .group() can be indexed <1, n>
@return     None 
'''
def RE_TestMethod_pattern_or_wildcard(OpenedFile) -> None:
  compiledPattern = RegEx.compile(r".{5}\.txt")
  lineNum = 0
  print("Search using RegEx.compile()")
  for line in OpenedFile:
        lineNum += 1

        machObj = RegEx.search(pattern= compiledPattern, string= line)
        if machObj:
            print("RegEx.search().group()= {}".format(machObj.group()))
        else:
            print("No mach")
        print(line, end= '\n')

  return None 
#=======================================================================================

'''*************************************************************************************
@name       RE_TestMethod_pattern_exclude
@brief      Posibility to remove some of text
@param[in]  None 
@note       Excluded part are remove and rest is inside list 
@return     None 
'''
def RE_TestMethod_pattern_exclude(OpenedFile) -> None:
  compiledPattern = RegEx.compile(r"[^\d]+")
  compiledPattern = RegEx.compile(r"[^\d ]+")
  lineNum = 0
  print("Search using RegEx.compile()")
  for line in OpenedFile:
        lineNum += 1

        machObj = RegEx.findall(pattern= compiledPattern, string= line)
        if machObj:
            print(machObj, end= '\t')
            print("".join(machObj))
        else:
            print("No mach")
        print(line, end= '\n')

  return None 
#=======================================================================================

'''*************************************************************************************
@name       RE_TestMethod_pattern_exclude
@brief      Posibility to remove some of text
@param[in]  None 
@note       Excluded part are remove and rest is inside list 
@return     None 
'''
def RE_TestMethod_pattern_with_mark_inside(OpenedFile) -> None:
  compiledPattern = RegEx.compile(r"[\w]+\.[\w]+")
  # [\w]+ is looking for group alpha numeric. It will find group of letters word for example.
  # \. Threat dot " . " as dot. 
  lineNum = 0
  print("Search using RegEx.compile()")
  for line in OpenedFile:
        lineNum += 1

        machObj = RegEx.findall(pattern= compiledPattern, string= line)
        if machObj:
            print(machObj, end= '\t')
            print("".join(machObj))
        else:
            print("No mach")

        print("string= {}".format(line), end= '\n')

  return None 
#=======================================================================================

'''*************************************************************************************
@name       CALL_RegularExpresion
@brief      ...
@param[in]  None 
@note       ... 
@return     None 
'''
def CALL_RegularExpresion() -> None:

    #OpenCloseFile(FileLocations.MakeFullDir("phone_numbers.txt"), RE_TestMethod_pattern_compile)
    OpenCloseFile(FileLocations.MakeFullDir("other_normal_text.txt"), RE_TestMethod_pattern_with_mark_inside)

    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_RegularExpresion()
else:
    pass