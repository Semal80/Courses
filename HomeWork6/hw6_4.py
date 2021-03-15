##################################
#       Leap Year                #
##################################

while True:
    try:
        a = int(input("Input a year:"))
    except ValueError:
        print("This is not number")
        continue
    if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
