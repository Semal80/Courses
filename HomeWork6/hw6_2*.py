###################################
#           Herringbone *         #
###################################
while True:
    try:
        a = int(input("Input number:"))
    except ValueError:
        print("Only numbers please")
        continue

    for i in range(a):
        y = a - i - 1
        while y > 0:
            print(" ", end="")
            y -= 1
        for j in range(i + 1):
            print("**", end="")
        print()
