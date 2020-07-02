# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sumityadav25199@gmail.com", "ssssyadav") 
  
# message to be sent 
message = "This mail is notify the developer hat your latest code been failed ,please take action on it as soon as possibe"
  
# sending the mail 
s.sendmail("sumityadav25199@gmail.com", "sumityadav25199@gmail.com", message1) 
  
# terminating the session 
s.quit() 
