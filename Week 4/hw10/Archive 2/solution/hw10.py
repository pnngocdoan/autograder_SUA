import math
def main():
    filename = input("Name of text file (including extension): ")
    file = open(filename, 'r')
    data = file.readlines()
    ans = 1
    count = 0
    for i in data:
        ans *= float(i)
        count += 1
    ans = math.pow(ans, 1/count)
    print("Geometric mean = {0:0.3f}".format(ans))
