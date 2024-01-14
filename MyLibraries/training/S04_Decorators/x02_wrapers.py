def ReadFile(line : int)->str:
    return "Line number {}".format(line)

def OpenFile(MyFileOperation : ReadFile):
    def _Internal(*args, **kwargs):
        print("File is opened:")
        status = MyFileOperation(*args, **kwargs)
        print("File is closed:")
        return status
    return _Internal


def CALL_Test1():
    NewReadFile = OpenFile(ReadFile)
    print(NewReadFile(5))
    return None

if (__name__ == "__main__"):
    CALL_Test1()
else:
    pass