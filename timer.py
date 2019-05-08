'''
what should it do?
it should decrease the seconds on the same line
after the seconds go to 0, it should decrease a minute and get 59 on the seconds
after this the iteration should repeat itself for the seconds
when the minutes get to 0, the hour should decrease by 1, the minutes to 59, seconds to 59
and the iteration for the seconds should repeat itself.
'''
import time
import os 
import sys

print "Working here, take another computer."
print "It will show how to terminate after the time is done"
print "I mean If I don't come by the timer eta"

h = 2
m = 1
s = 5

# if the time given is negative or not wanted
if s > 59 or m>59 or m<0 or s<0 or h<0:
    print "error. Please type the correct time."
    sys.exit(0)

# the main idea
while h>-1:
    print str(h)+':'+str(m)+':'+str(s)
    os.system('clear')

    if -1<s:
        s = s-1
        time.sleep(1)
    if s==-1:
        m = m-1
        if m  == -1:
            h = h-1
            if h==0 and s==0:
                m = 0
                s - 59
            m=59
            s=59
        s = 59
    

