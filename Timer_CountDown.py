import time

def countDownTimer(t):
    while t:
        min,sec=divmod(t,60)
        timer='{:02d} : {:02d}'.format(min,sec)
        print(timer, end="\r")
        time.sleep(1)
        t=t-1
    
    print("Timer completed sucessfully")
    
t=int(input("Enter Time in seconds"))
countDownTimer(t)
        
    