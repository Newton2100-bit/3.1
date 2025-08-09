import smtplib
import time

sender = 'adabyron005@gmail.com'
# cusy liso meey gwdy 
receiver = 'mwauranewton99@gmail.com'#'olindamuruginyaga@gmail.com'
password = 'cusy liso meey gwdy' #'newtonirungu' #'your-app-password-here'  # Get Gmail App Password
subject = 'python email test'
body = "This is my sample message that was written in python3"

# Create properly formatted message
message = f"""From: {sender}
To: {receiver}
Subject: {subject}

{body}"""
try:
    total_start = time.process_time()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    login_start = time.process_time()
    server.login(sender, password)
    # login_end = time.process_time()
    login_end = time.process_time()
    print(f'Logged in ...\nTook {login_end - login_start:.4f}s')

    send_start = time.process_time()
    server.sendmail(sender, receiver, message)  # Now 'message' is defined
    send_end = time.process_time()
    print("Email sent .....\nTook {send_end - send_start:.4f}s")
    server.quit()  # Close connection
    total_end = time.process_time()
    print(f"Total time taken is {total_end - total_start:.4f}s")
except OSError as e:
    print("\033[31;9;4mAN ERROR OCCURED\033[0m")
