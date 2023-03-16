def main():
    dollar = float(input("Dollar value: "))
    penny = int(dollar * 100)
    quarter = penny // 25
    remainder = penny % 25
    dime = remainder // 10
    remainder = remainder % 10
    nickel = remainder // 5
    remainder = remainder % 5
    penny = remainder
    print("Quarters:", quarter)
    print("Dimes:", dime)
    print("Nickels:", nickel)
    print("Pennies:", penny)
