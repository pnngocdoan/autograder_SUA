def main():
    n = int(input("How many numbers? "))
    ans = 0
    for i in range(n):
        a = float(input("Type number # " + str(i + 1) + " : "))
        ans += a
    ans = ans/n
    print("Arithmetic mean =", round(ans,3))
