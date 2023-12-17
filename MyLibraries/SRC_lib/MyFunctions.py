import re as RegExp
import os

#======================================================================================
class ReplaceRowNumber:
    """
    This class is used for change row number in a file.
    Default pattern configuration: 
    self.mainPattern    = "^N[0-9]*"
    """
    #Default configuration
    NC_FOLDERS_NAME_DE = {   
        'DEF':'Definitionen/',
        'CUS':'Herstellerzyklen/',
        'SAF':'Standardzyklen/',
        'PAR':'Teileprogramme/',
        'SUB':'Unterprogramme/',
        'WPC':'Werkstücke/',
        'CYC':'Zyklenpakete/'}

    NC_FOLDERS_NAME_EN = {   
        'DEF':'Definitions/',
        'CUS':'Suppliercycles/',
        'SAF':'Standardcycles/',
        'PAR':'Partprogramms/',
        'SUB':'Subprogramms/',
        'WPC':'Workpieces/',
        'CYC':''}

    NC_FOLDERS = {
        'DE': NC_FOLDERS_NAME_DE, 
        'EN': NC_FOLDERS_NAME_EN}

    EXTENSION = '.arc'
    RE_PATTERN_ROW = RegExp.compile("^N[0-9]*")
    RE_PATTERN_EXTENSION = RegExp.compile("[.][a-zA-Z]*")
    #==================================================================================

    #**********************************************************************************
    # Name      __init__
    # Brief     Initialization of renumber NC class       
    # parameter[in] inExtension - Main CD
    # parameter[in] inMainDir   - Extension for files
    def __init__(self, inExtension, inMainDir):
        self.mainDir        = inMainDir
        self.extension      = inExtension
        self.rowstart       = 0
        self.step           = 0
        self.amountOfZeros  = 0
        self.sourceNames    = self.__INTERN_CreateListOfSrcFiles(self.mainDir)
        self.destinNames    = self.__INTERN_RenameFilesNames(self.sourceNames, '_')
        #==============================================================================

    def __INTERN_CreateListOfSrcFiles(self, inMainDir):
        #Folder from dictionary
        #Extension default .arc
        filesInFolder = os.listdir(inMainDir)
        validFiles = []
        #Adding only files with extensions that match
        for file in filesInFolder:
            extension = self.__INTERN_ReturnExtension(file)
            if(extension == self.extension):
                validFiles.append(file)
            else:
                pass
        return validFiles
        #==============================================================================

    def __INTERN_RenameFilesNames(self, inNames, inStr):
        validFiles = []
        for file in inNames:
            tStr = self.__INTERN_AddCopyNameBefore(file, inStr)
            if(tStr):
                validFiles.append(tStr)
            else:
                pass
        return validFiles
        #==============================================================================

    def __INTERN_ReturnExtension(self, inFileName):
        # Internal functions: Check to demending extension.
        RE_search = self.RE_PATTERN_EXTENSION.search(inFileName)
        if (RE_search):
            return RE_search[0]
        else:
            return None
        #==============================================================================

    def __INTERN_RemoveExtension(self, inFileName):
        # Internal functions: Remove extension from file name
        RE_split = self.RE_PATTERN_EXTENSION.split(inFileName)
        if(RE_split):
            return RE_split[0]
        else:
            return None
        #==============================================================================

    def __INTERN_AddCopyNameAfter(self, inSrcFileName, inCoppyName):
        # Internal functions: Create name with extensions
        sourceNoExtension = self.__INTERN_RemoveExtension(inSrcFileName)
        if(sourceNoExtension):
            destinationName = sourceNoExtension + inCoppyName + self.EXTENSION
            return destinationName
        else:
            return None
        #==============================================================================

    def __INTERN_AddCopyNameBefore(self, inSrcFileName, inCoppyName):
        # Internal functions: Create name with extensions
        if(inSrcFileName):
            destinationName = inCoppyName + inSrcFileName
            return destinationName
        else:
            return None
        #==============================================================================

    def __INTERN_RetNewLine(self, inLine, inNewRowNum):
        # Internal functions: Return new line from file
        if(self.amountOfZeros == 0x00):
            myReplace = 'N'+str(inNewRowNum)
        else:
            tStr = str(inNewRowNum)
            tStr = tStr.zfill(self.amountOfZeros)
            myReplace = 'N'+ tStr
        return self.RE_PATTERN_ROW.sub(myReplace , inLine)
        #==============================================================================

    def CalculateAmountOfZeros(self, inSrcDir):
        try:
            SourceFile = open(inSrcDir, 'r')
            print('File opened: ', inSrcDir )

        except FileNotFoundError:
            print('File --', inSrcDir, '-- not found!')
            return False
        
        srcLine = SourceFile.readlines()
        nLines = 0
        for line in srcLine:
            if(line[0] == 'N'):
                nLines = nLines + 0x01

        self.amountOfZeros = len(str(nLines)) + 1
        SourceFile.close()
        return True
        #==============================================================================
    
    #**********************************************************************************
    # Name              RenumberOneFile
    # Brief             Renumber one file from source to coppy file
    # parameter[in]     inSrcDir - Source CD
    # parameter[in]     inDstDir - Destiantion CD
    def RenumberOneFile(self, inSrcDir, inDstDir):
        #Open source file 
        try:
            SourceFile = open(inSrcDir, 'r')
            print('File opened: ', inSrcDir )

        except FileNotFoundError:
            print('File --', inSrcDir, '-- not found!')
            return False

        #Open destination files if source file is found.
        try:
            DestinFile = open(inDstDir,'w')
            print('File Created:', inDstDir)

        except FileNotFoundError:
            SourceFile.close()
            print('File --', inDstDir, '-- not found!')
            return False

        #Writing changed line to new copy file
        myrow   = self.rowstart
        mystep  = self.step
        srcLine = SourceFile.readlines()
        for line in srcLine:
            if(line[0] == 'N'):
                newLine = self.__INTERN_RetNewLine(line, myrow)
                DestinFile.writelines(newLine)
                myrow = myrow + mystep
            else:
                DestinFile.writelines(line)

        #All opened file close
        print('Operation with sucess!!!')
        DestinFile.close()
        SourceFile.close()
        return True
        #==============================================================================

    #**********************************************************************************
    # Name              RenumberAllFiles
    # Brief             Renumber every file in folder from source to coppy file
    # parameter[in]     inStart - Start number 
    # parameter[in]     inStep - Step amount
    def RenumberAllFiles(self, inStart, inStep):
        self.rowstart = inStart
        self.step = inStep
        i = 0
        i_max = len(self.sourceNames) 
        j = 0
        j_max = len(self.destinNames) 
        while((i < i_max) and (j < j_max)):
            srcCD = self.mainDir + self.sourceNames[i]
            dstCD = self.mainDir + self.destinNames[j]
            self.CalculateAmountOfZeros(srcCD)
            self.RenumberOneFile(srcCD, dstCD)
            i = i + 1
            j = j + 1
        return None
        #==============================================================================

    #**********************************************************************************
    # Name              DeleteFiles
    # Brief             Source files that rowa been copied from are deleted
    # parameter[in]     inList - List of files to delete
    def DeleteFiles(self, inList):
        imax = len(inList)
        if (imax <= 0):
            return False

        for name in inList:
            if(name):
                myCD = self.mainDir + name
                try:
                    os.remove(myCD)
                    print('Delete: ', name)
                except:
                    print('File does not exist!')
            else:
                pass
        return True
        #==============================================================================

    #**********************************************************************************
    # Name              RenameAllFiles
    # Brief             All files in folder are renamed to name in list
    # parameter[in]     inListSRC - Source existin file list
    # parameter[in]     inListDST - Destination list of fiels
    def RenameAllFiles(self, inListSRC, inListDST):
        len_SRC = len(inListSRC)
        len_DST = len(inListDST)
        if(len_SRC == 0) or (len_DST == 0):
            return False
        
        i = 0
        while((i < len_SRC) and (i < len_DST)):
            if((inListSRC[i]) and (inListDST[i])):
                cd_SRC = self.mainDir + inListSRC[i]
                cd_DST = self.mainDir + inListDST[i]
                
                try:
                    os.rename(cd_SRC, cd_DST)
                    print('Rename from: ', inListSRC[i], " to :", inListDST[i])
                except:
                    print('File does not exist! ', cd_DST)
            else:
                pass
            i = i + 1

        return True
        #==============================================================================
#======================================================================================

