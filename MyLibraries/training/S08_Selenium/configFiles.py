# Selenium tutorial part 1.
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# C:\Program Files (x86)\Google

class SelenumConstants:
    _MAIN_PATH = r"D:\ProgramData\Selenium"
    
    _NAME_EDGE = r"\edgedriver_win64\chromedriver.exe"
    _NAME_CHROME = r"\chromedriver-win64\msedgedriver.exe"

    WEB_HTTP_LINK1 = "https://techwithtim.net"

    def __init__(self):
        self.ChromePath = self._MAIN_PATH + self._NAME_CHROME
        self.EdgePath = self._MAIN_PATH + self._NAME_EDGE