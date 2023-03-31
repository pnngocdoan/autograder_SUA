def getNum():
    n = input()
    while (not n.isdigit() or int(n) < 0):
        n = input()
    return int(n)

def dec2hex(num):
    res = ''
    dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',13: 'D', 14: 'E', 15: 'F'}
    if num == 0:
        return 0
    while num > 0:
        res = dict[num % 16] + res
        num = num // 16
    return res

def main():
    num = getNum()
    dec2hex(num)
    
