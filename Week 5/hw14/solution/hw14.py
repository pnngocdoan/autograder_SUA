def check_date(s):
    month, day, year = s[0:2], s[3:5], s[6:]
    if month.isnumeric() and day.isnumeric() and year.isnumeric():
        if int(year) % 4 == 0: 
            if (int(year) >= 400 and int(year) % 400 == 0) or (int(year) >= 400 and int(year) % 100 != 0) or (100 <= int(year) < 400 and int(year) % 100 != 0) or (int(year) < 100):
                days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return 1 <= int(month) <= 12 and 1 <= int(day) <= days[int(month)-1] and  int(year) <= 9999
    return False
