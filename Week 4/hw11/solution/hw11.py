def main():
    file_to_read = open("BrightspaceFolders.txt", "r")
    file_to_write = open("[Solution]StudentSubmissions.txt", "w")
    data_to_read = file_to_read.readlines()
    data_to_write = []
    for data in data_to_read:
        
        trash, name, time = data.split(" - ")
        fullName = name.split()
        lastName = fullName[len(fullName)-1]

        firstName = name[:len(name)-len(lastName)-1]
        
        month, day, year, time1, AM_PM = time.split()
        if len(time1) == 4:
            hour, minute = time1[0:2], time1[2:]
        else:
            hour, minute = time1[0:1], time1[1:]

        day = day[:-1]
        
        data = []
        for each in [lastName,',',firstName,';',hour,':',minute,' ',AM_PM,';',day,'-',month,'-',year,'\n']: 
            data.append(each)
        data_to_write.append(''.join(data))
    file_to_write.writelines(data_to_write)        

if __name__ == "__main__":
    main()
