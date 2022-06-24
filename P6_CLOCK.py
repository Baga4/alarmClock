#2078/09/30
#completed bitch you can use this alarm but its not that user friendly 
import datetime 
import time
import androidhelper 

droid=androidhelper.Android ()

def n_time (alarm):
    while True:
        clock=datetime.datetime.now().strftime("%H:%M:%S")
        print (clock,end='\r')
        time.sleep (1)
        if clock==alarm:
            print ("\n\tIts alarm ringing")
            droid.vibrate ()
            droid.makeToast (f"Its {alarm} o'clock")
            droid.notify ("Alarm",f"Its {alarm} 0'clock")

print("\n\tSet an alarm")
alarm=input ("\t\n must be int and followed by ':'\n\t -> ")
n_time (alarm)
