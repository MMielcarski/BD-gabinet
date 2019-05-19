import smtplib
import haslo
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = 'bdgabinet@gmail.com' # Your email
password = haslo.haslo()

#reciever = whu you are sending the message to
#passwd - generated password for new user
def send_first_time_email(reciever, passwd):
    subject = "Witamy w serwisie dbgabinet!"
    messageHTML = '<p>Dziękujemy za rejestrację'+\
                  '<p> Wejdź na <a href="http://dbgabinet.cba.pl/"> www.dbgabinet.cba.pl<a> aby zarejestrować się do wybranego lekarza.'+\
                  '<p> Twoje hasło:'+passwd + \
                  '<p><p><p> Zespół bdgabinet'

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(messageHTML, 'html'))
    msg.attach(MIMEText(messagePlain, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
    server.starttls() # Use TLS
    server.login(my_email, password) # Login to the email server
    text = msg.as_string()
    server.sendmail(my_email, reciever ,text) # Send the email
    server.quit() # Logout of the email server



def send_confirm_email(reciever, doctor, date, hour):
    subject = "Potwierdzenie wizyty"
    messageHTML = '<p>Twoja wizyta do' + doctor + ' została potwierdzona!' + \
                  '<p> Data: ' + date  + '  Godzina:'+ hour + \
                  '<p><p><p> Zespół bdgabinet'

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(messageHTML, 'html'))
    #msg.attach(MIMEText(messagePlain, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
    server.starttls()  # Use TLS
    server.login(my_email, password)  # Login to the email server
    text = msg.as_string()
    server.sendmail(my_email, reciever, text)  # Send the email
    server.quit()  # Logout of the email server


def send_reject_email(reciever, doctor, date, hour):
    subject = "Odrzucenie wizyty"
    messageHTML = '<p> Twoja wizyta do ' + doctor + ' na dzień ' + date + ' '+ hour + ' została odrzucona!' + \
                  '<p> Wejdź na <a href="http://dbgabinet.cba.pl/"> www.dbgabinet.cba.pl<a> aby ponownie zarejestrować się do wybranego lekarza.' + \
                  '<p><p><p> Zespół bdgabinet'

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(messageHTML, 'html'))
    #msg.attach(MIMEText(messagePlain, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
    server.starttls()  # Use TLS
    server.login(my_email, password)  # Login to the email server
    text = msg.as_string()
    server.sendmail(my_email, reciever, text)  # Send the email
    server.quit()  # Logout of the email server

def send_cancel_email(reciever, doctor, date, hour):
    subject = "Anulowanie wizyty"
    messageHTML = '<p> Twoja wizyta do ' + doctor + ' na dzień ' + date + ' '+ hour + ' została anulowana!' + \
                  '<p> Wejdź na <a href="http://dbgabinet.cba.pl/"> www.dbgabinet.cba.pl<a> aby ponownie zarejestrować się do wybranego lekarza.' + \
                  '<p><p><p> Zespół bdgabinet'

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(messageHTML, 'html'))
    #msg.attach(MIMEText(messagePlain, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
    server.starttls()  # Use TLS
    server.login(my_email, password)  # Login to the email server
    text = msg.as_string()
    server.sendmail(my_email, reciever, text)  # Send the email
    server.quit()  # Logout of the email server


# send_first_time_email('dbgabinet@gmail.com', 'abc')
# send_confirm_email('bdgabinet@gmail.com', 'Arkadiusz Mróz', '20-01-2019r.', '19:00')
# send_reject_email('bdgabinet@gmail.com', 'Arkadiusz Mróz', '20-01-2019r.', '19:00')
# send_cancel_email('bdgabinet@gmail.com', 'Arkadiusz Mróz', '20-01-2019r.', '19:00')