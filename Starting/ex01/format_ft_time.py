from datetime import datetime
from time import time

# get the current time in seconds since the epoch
seconds = time() 

# get the current date and time
date = datetime.now()


print("Seconds since January 1, 1970:",f"{seconds:,.4f}", "or " ,f"{seconds:.3}" , "in scientific notation")
new_forma_date = date.strftime("%b %d %Y")
print(new_forma_date)

