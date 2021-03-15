###################################
#            Herringbone          #
###################################

while True:
    try:
        a = int(input("Input number:"))
    except ValueError:
        print("Only numbers please")
        continue
    for i in range(a):
        for j in range(i+1):
            print("*", end="")
        print()
