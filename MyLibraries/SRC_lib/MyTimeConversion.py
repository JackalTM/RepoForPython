class MyTimeConvert:
#**********************************************************************************************
    def SecondsToTime_d_h_m_s(self, secAmount : int)->tuple:
        days = secAmount // (60 * 60 * 24) # 60 * 60 * 24
        secAmount %= (60 * 60 * 24)
        hours = secAmount // (60 * 60) # 60 * 60
        secAmount %= (60 * 60)
        minutes = secAmount // 60
        secAmount %= 60
        #return "%02i:%02i:%02i" % (hours, minutes, secAmount)
        return (days, hours, minutes, secAmount)
#==============================================================================================
#**********************************************************************************************
    def SecondsToTime_h_m_s(self, secAmount : int)->tuple:
        hours = secAmount // (60 * 60) # 60 * 60
        secAmount %= (60 * 60)
        minutes = secAmount // 60
        secAmount %= 60
        #return "%02i:%02i:%02i" % (hours, minutes, secAmount)
        return (hours, minutes, secAmount)
#==============================================================================================
#**********************************************************************************************
    def SecondsToTime_h_m(self, secAmount : int)->tuple:
        hours = secAmount // (3600)
        secAmount %= (3600)
        minutes = secAmount // 60
        secAmount %= 60
        #return "%02ih%02imin" % (hours, minutes)
        return (hours, minutes)
#============================================================================================== 
myTimeConvert = MyTimeConvert()