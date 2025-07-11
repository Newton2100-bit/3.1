import threading
import time

def walk_dog():
    print('Walk dog executing','6 secs')
    time.sleep(6)
    print('You finish walking the Dog')

def take_out_trash():
    print('Taking out the trash','2 secs')
    time.sleep(2)
    print('You take the trash')

def get_mail():
    print('Waiting for the email','4 secs')
    time.sleep(4)
    print('You get the mail')

# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target= walk_dog, name='walking the dog')
chore1.start()

chore2 = threading.Thread(target= take_out_trash, name='taking the trash out')
chore2.start()

chore3 = threading.Thread(target= get_mail, name= 'get te email')
chore3.start()


chore1.join()
chore2.join()
chore3.join()


print('Executing the main thread \nAnd the program has come to an end\n')

# Possible arguments to the Thread Class of init constructor
# target this holds the name of the function that is intended this is intended to be called by the run() method form the Threads class
# group _ just like goto in java which is left for a later date
# args this holds arguments to the target method
# kwargs This holds the **kwargs to the target
# daemon This is bool method that determines wheather the thread ca run as a daemon at any particular point
# name This defines the name we assign to our thread explicitly
# Note that the args should be a tuple and never something else

