def check_date(s):
    month, day, year = s[0:2], s[3:5], s[6:]
    return 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and int(year) <= 9999
   
