# #!/usr/bin/python

#Python program to convert date format from mm/dd/yyyy to yyyymmdd

from datetime import datetime

def datefunc(d1):
    o_d = datetime.strptime(d1,"%m/%d/%Y")
    n_d = datetime.strftime(o_d,"%Y%m%d")
    print "Date format changed to %s"%n_d


if __name__ == '__main__':
    print "Enter date in mm/dd/yyyy:"
    d1 = raw_input()
    datefunc(d1)
    
