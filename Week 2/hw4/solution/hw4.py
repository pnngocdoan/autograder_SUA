import math
def main():
    n = int(input("How many numbers? "))
    ans = 1
    for i in range(n):
        a = float(input("Type number # " + str(i + 1) + " : "))
        ans *= a
    ans = math.pow(ans, 1/n)
    print("Geometric mean =", round(ans, 3))
