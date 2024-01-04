'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
#=======================================================================================

'''*************************************************************************************
@name       CALL_datetime
@brief      module datetime can be used to asigned date or time
@param[in]  ...
@note       Date or time are from larger time scale to lower
@return     ...
'''
def CALL_datetime():
    from datetime import time
    from datetime import date

    myTime = time(hour= 21, minute= 0x9, second= 00)
    print(myTime)

    myDate = date(year= 2024, month= 1, day= 2)
    print(myDate)



    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_datetime
@brief      module datetime can be used to asigned date or time
@param[in]  ...
@note       Date or time are from larger time scale to lower
@return     ...
'''
def CALL_datetime_datetime():
    from datetime import datetime

    fullDate = datetime(2024, 1, 2, 21, 15)
    fullDate - datetime(year= 2014, month= 1, day= 2, hour= 21, minute= 30)
    print(fullDate)

    fullDate = fullDate.replace(day= 3)
    print(fullDate)

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_datetime_date_aritmetics
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_datetime_date_aritmetics():
    from datetime import date

    someDate1 = date(2024, 1, 2)
    someDate2 = date(2024, 6, 24)

    diffrenceDate = (someDate2 - someDate1)
    print(diffrenceDate)
    print("Type of date is : {}".format(type(diffrenceDate)))

    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_datetime_date_aritmetics
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_datetime_date_aritmetics():
    from datetime import time

    someTime1 = time(21, 30, 0)
    sometime2 = time(22, 30, 0)
    diffrence = (sometime2 - someTime1)
    print(diffrence)
    print("Type of time is : {}".format(type(diffrence)))
    return None
#=======================================================================================

'''*************************************************************************************
@name       CALL_datetime_date_aritmetics
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_datetime_datetime_aritmetics():
    from datetime import datetime

    date1 = datetime(year= 2028, month= 4, day= 9, hour= 21, minute= 30)
    date2 = datetime(year= 2014, month= 8, day= 1, hour= 4, minute= 31)
    date3 = (date1 - date2)

    print(date3)
    print("Type of time is : {}".format(type(date3)))
    return None
#=======================================================================================

if(__name__) == ("__main__"):
    CALL_datetime_datetime_aritmetics()
else:
    pass