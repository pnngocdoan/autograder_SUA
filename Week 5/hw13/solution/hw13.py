def check_date(s):
    month, day, year = s[0:2], s[3:5], s[6:]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= int(month) <= 12 and 1 <= int(day) <= days[int(month)-1] and  int(year) <= 9999
