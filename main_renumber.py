#python main_renumber.py
from MyLibraries.SRC_lib.MyFunctions import ReplaceRowNumber

print("CALL -> main_renumber.py")

def CALL_main_renumber():
    mainDir = "C:/_Projekty_/__GM__/x00_GM5375/GM5375_01_60/NC/"
    mainDir = mainDir + ReplaceRowNumber.NC_FOLDERS['DE']['SUB']
    MyReplace = ReplaceRowNumber(inExtension='.ARC', inMainDir= mainDir)
    MyReplace.RenumberAllFiles(inStart= 000, inStep= 10)
    MyReplace.DeleteFiles(MyReplace.sourceNames)
    MyReplace.RenameAllFiles(MyReplace.destinNames, MyReplace.sourceNames)
    return

if __name__ == "__main__":
    CALL_main_renumber()
else:
    print("Indirect call ERROR!")