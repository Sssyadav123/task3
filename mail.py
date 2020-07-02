 import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587)  
s.starttls() 
s.login("sumityadav25199@gmail.com", "ssssyadav") 
message = "This mail is notify the developer hat your latest code been failed ,please take action on it as soon as possibe"
s.sendmail("sumityadav25199@gmail.com", "sumityadav25199@gmail.com", message1) 
s.quit() 
