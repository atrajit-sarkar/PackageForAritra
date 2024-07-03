import os

title=input("Enter your notification title: ")
message=input("Enter your notification message: ")
timeout=input("Enter your notification timeout: ")
app_icon=input("Enter your notification app_icon: ")
timesleep=input("Enter your notification timesleep: ")
startup=input("Enter the time in sec when you want the notification shows after you open pc: ")
onetime=input("Frequency: (onetime/repeatative)")
if onetime=="repeatative":

    customnotification=f'''
from plyer import notification
import time
time.sleep({startup})
while True:
    notification.notify(
    app_name="Python",
    title = "{title}",
    message ="{message}",
    timeout ={timeout},
    app_icon=r"{os.getcwd()}\icons\{app_icon}"
    )
    time.sleep({timesleep})
    '''
elif onetime=="onetime":
    customnotification=f'''
from plyer import notification
import time
time.sleep({startup})
notification.notify(
app_name="Python",
title = "{title}",
message ="{message}",
timeout ={timeout},
app_icon=r"{os.getcwd()}\icons\{app_icon}"
)
    '''

with open(f"{title}.pyw","w") as f:
    f.write(customnotification)
