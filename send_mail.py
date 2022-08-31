import smtplib
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication Your Email Address That You Used IN Solution 1
s.login("satyam.sharma19981310@gmail.com", "lpkrhydnwyobfnwx")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("satyam.sharma19981310@gamil", "satyam.sharma19981310@gamil", message)
  
# terminating the session
s.quit()
