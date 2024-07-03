title=input("Enter your notification title: ")
message=input("Enter your notification message: ")
timeout=input("Enter your notification timeout: ")
app_icon=input("Enter your notification app_icon: ")
timesleep=input("Enter your notification timesleep: ")

customnotification=f'''
from plyer import notification
import time

while True:
    notification.notify(
    title = "{title}",
    message ="{message}",
    timeout ={timeout},
    app_icon="{app_icon}"
    )
    time.sleep({timesleep})
'''
with open(f"{title}.pyw","w") as f:
    f.write(customnotification)
