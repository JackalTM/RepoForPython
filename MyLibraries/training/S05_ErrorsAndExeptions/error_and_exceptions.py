def ClculateMean(some_list):
    if(type(some_list) == list):
        tSum = 0
        n = 0
        for i in some_list:
            n = n + 1
            tSum = tSum + i
        return(tSum / n)

    elif(type(some_list) == int):
        return some_list
    

def ConvertToInt(input_data):
    try:
        i = int(input_data)
    except:
        i = -1
    finally:
        return i
    

def OpenFile(fullDirectory, mode):
    some_text = " "
    try:
        file = open(fullDirectory, mode)
        some_text = file.read()
    except TypeError:
        print("TypeError!")
    except OSError:
        print("OSError!")
    finally:
        return some_text
    
def WriteFile(fullDirectory, mode, some_text):
    try:
        file = open(fullDirectory, mode)
        file.write(some_text)
    except TypeError:
        print("TypeError!")
    except OSError:
        print("OSError!")
    finally:
        return
    