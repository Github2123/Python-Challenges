from datetime import datetime
now=datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
from datetime import date
today=date.today()
today

from datetime import timedelta
now=datetime.now()
print(f"tomorrow:{now+timedelta(weeks=3)}")
empty_bytes=bytes()
zero_bytes=bytes(5)
from_strings=bytes('hello')
from_strings
print(zero_bytes)





    

empty_bytes=bytes()
zero_bytes=bytes(5)
from_strings=bytes('hello')
from_strings
print(zero_bytes)





    



#formatting datetime

from datetime import datetime
now=datetime.now().strftime("%y-%m-%d %H:%M:%S")
NOW=datetime.now().strftime("%A, %dth of %b %Y")
NOW
now


def age(n):
    now=datetime.now()
    current_year=now.year
    birthyear=n.year
    
bdaay=datetime(2001,1,15)
#scheduling future events and calcualting time remains 
#create a function(event_name,eventdate)
#retrun event:name
#date
#time remaining
#one week remainder 
#one day remainder


#nonetype
def add(a,b):
    return (a+b)
add(10,20)
print(add(10,20))

n=None
while n is None:
    input_aa=input("enter a values:").lower()
    if (input=="quit" or input=="exit"):
        break
    elif input_aa:
        print(f"you have enter:{input_aa}")
        
#binary type
#bytes:immutable,
#bytearray:mutable

#memoryview:memory efficient deals with a binary data




empty_bytes=bytes()
zero_bytes=bytes(5)
from_strings=bytes('hello',encoding='utf-8')
from_strings
print(zero_bytes)





    

