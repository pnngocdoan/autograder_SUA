def main():
    def formattedtext(line):
        part = line.strip().split("-")
        print(part)
        name = part[2].split()
        time = part[3].split()
        day = time[1].replace(",", "")
        timeDay = time1[:2] + ":" + time1[2:]
        if len(name) == 2:
            namebreak = name[1] + "," + name[0]
        else:
            namebreak = name[2] + "," + name[0] + " " + name[1]
        result = namebreak + ";" + timeDay + " " + time[4] + ";" + day + "-" + time[0] + "-" + time[2] + "\n"
        return result
    
    inputfile = open("BrightspaceFolders.txt", "r")
    outputfile = open("StudentSubmissions.txt", "w")

    outputfile.write("NAME;TIME;DATE\n")
  
    for line in inputfile:
        finaltext= formattedtext(line)
        outputfile.write(finaltext)   

    inputfile.close()
    outputfile.close()

if __name__ == '__main__':
    main()
