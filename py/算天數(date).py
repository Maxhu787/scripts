from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('1/1/2000', date_format)
b = datetime.strptime('3/1/2019', date_format)
delta = b - a
print ( delta.days) # that's it
