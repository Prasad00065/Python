import os
import math
import random
import smtplib
def funOtpGen():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg= otp
    return msg
n=funOtpGen()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("guribillivaraprasad0065@gmail.com", "blzixpfdtuzowcvf")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,n)
a = input("Enter Your OTP : ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")