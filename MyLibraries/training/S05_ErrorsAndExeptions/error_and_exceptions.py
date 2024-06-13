'''*************************************************************************************
@name       ClculateMean
@brief      ...
@param[in]  some_list - Input lsit with integers
@note       ... 
@return     int - mean value calculated from list
'''
def ClculateMean(some_list : list)->int:
    if(type(some_list) == list):
        tSum = 0
        n = 0
        for i in some_list:
            n = n + 1
            tSum = tSum + i
        return(tSum / n)

    elif(type(some_list) == int):
        return some_list
#=======================================================================================
    
'''*************************************************************************************
@name       ConvertToInt
@brief      ...
@param[in]  input_data - int
@note       ... 
@return     int - Data converted to int
'''
def ConvertToInt(input_data)->int:
    try:
        i = int(input_data)
    except:
        i = -1
    finally:
        return i
#=======================================================================================

'''*************************************************************************************
@name       OpenFile
@brief      ...
@param[in]  fullDirectory - String to file directory
@param[in]  mode - Read or write mode 
@note       ... 
@return     str - String content from file 
'''
def OpenFile(fullDirectory : str, mode : str)->str:
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
#=======================================================================================

'''*************************************************************************************
@name       WriteFile
@brief      ...
@param[in]  fullDirectory - String to file directory
@param[in]  mode - Read or write mode 
@param[in]  some_text - Content to add into file
@note       ... 
@return     int  - state of operation
'''
def WriteFile(fullDirectory : str, mode : str, some_text : str)->int:
    try:
        file = open(fullDirectory, mode)
        file.write(some_text)
        err = 0x00
    except TypeError:
        print("TypeError!")
        err = 0x11
    except OSError:
        print("OSError!")
        err = 0x22
    finally:
        return err
#=======================================================================================
    