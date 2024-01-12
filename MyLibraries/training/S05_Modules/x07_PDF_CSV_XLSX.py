import os
import csv

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

def CALL_OpenCSV():
    path = "MyLibraries/training/S05_Modules"
    os.chdir(path)
    os.getcwd()

    data_lines = list(blood_csv)
    for row in data_lines:
        for elem in row:
            print("| {}".format(elem), end='\t')
        print("\n ------------")

    return None

def CALL_OpenAndSafeNewfile():
    # Create instance for save new file
    new_blood_csv = open("new_blood_csv", mode= 'w', newline='')
    csv_writter = csv.writer(new_blood_csv, delimiter= ',')

    csv_writter.writerow(["C", "+"])
    csv_writter.writerow(["C", "-"])

    new_blood_csv.close()

def CALL_AppendNewLIne():
    data_csv_append = open("blood.csv",mode='a', encoding= "utf-8")
    blood_csv_append = csv.writer(data_csv_append, delimiter=';')

    blood_csv_append.writerow(["C", "+"])
    blood_csv_append.writerow(["C", "-"])

    data_csv_append.close()

if __name__ == "__main__":
    SetCurrentOSPath("MyLibraries/training/S05_Modules/files_CSV")
else:
    pass