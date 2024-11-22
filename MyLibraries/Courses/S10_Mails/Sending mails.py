import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()
smtp_object.starttls()

email = input("email: ")
pasword = input('enter password: ')
smtp_object.login(email, password)

from_address = email
to_address = email
subject = input('Text of mesage')
mesage = input('Enter the body of mesage')
msg = "Subject: "+subject+'\n'+mesage

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()

'''*************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ... 
@return     ...
'''
def CALL_Mail_send()->None:
    pass
#=======================================================================================

if __name__ == "__main__":
    pass
else:
    pass