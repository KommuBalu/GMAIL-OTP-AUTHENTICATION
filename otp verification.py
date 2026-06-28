import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp=random.randint(1111,9999)
months={1:"january",2:"feb",3:"march",4:"april",5:"may",6:"june",7:"july",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}



name=input("Enter your Name: ")
date=int(input("Enter your Date of Birth : "))
month=int(input("Enter your Month of Birth: "))

tomail=input("Enter Mail id : ")
subject="OTP For verification"
body=f"Hello {name} !\n Date of Birth : {date} - {months[month]}\n your secret otp is {otp} :"


msg=MIMEMultipart()
msg['From']="kommupawan84@gmail.com"
msg['To']=tomail
msg['Subject']=subject
msg.attach(MIMEText(body,'plain'))


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("kommupawan84@gmail.com",'obsf xwfc uqxt jssh')
server.send_message(msg)
server.quit()


userinput=input("Enter OTP recived to your gmail:")
if userinput==str(otp):
    print("Otp validation successfull!")

else:
    print("wrong Otp Entered!")