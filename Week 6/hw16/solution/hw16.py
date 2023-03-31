def getNum():
    n = input()
    if n.isdigit():
        return int(n)
    
    temp = n.replace(',','')
    if temp.isdigit():
        for i in range(len(n)-4, -1, -4):
            if n[i] != ',':
                return getNum()
        return int(temp)
    else:
        return getNum()
                
def getBase():
    while 1:
        n = input()
        if n.isdigit() and 2 <= int(n) <= 35:
            return int(n)    

def convert(num,base):
    res = ''
    if num == 0:
        return 0
    while num > 0:
        if num % base > 9:
            res = chr(num % base + 55) + res
        else:
            res = str(num % base) + res
        num = num // base
    return res

def main():
    num = getNum()
    base = getBase()
    convert(num, base)
    
