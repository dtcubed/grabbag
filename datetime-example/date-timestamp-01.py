#!/usr/bin/python

import datetime
import sys

#####
# We let the datetime object do the validation as this is a Happy Path Program.
#####
s_year    = int(sys.argv[1],10)
s_month   = int(sys.argv[2],10)
s_day     = int(sys.argv[3],10)
s_hours   = int(sys.argv[4],10)
s_minutes = int(sys.argv[5],10)
s_seconds = int(sys.argv[6],10)

l_hours   = int(sys.argv[7],10)
l_minutes = int(sys.argv[8],10)
l_seconds = int(sys.argv[9],10)

start_dt = datetime.datetime(s_year, s_month, s_day, s_hours, s_minutes, s_seconds)
print("\nStarting Datetime Stamp:")
print(start_dt.strftime("%Y%m%d-%H%M"))

l_timedelta = datetime.timedelta(hours=l_hours, minutes=l_minutes, seconds=l_seconds)
print("\nLength Time Delta:")
print l_timedelta 

end_dt = start_dt + l_timedelta
print("\nEnding Datetime Stamp:")
print(end_dt.strftime("%Y%m%d-%H%M\n"))

sys.exit(0)
#################################### EOF ##############################################
