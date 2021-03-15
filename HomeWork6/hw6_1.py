#################################################
# Calculator ['+', '-', '*', '/', '**', 'sqrt'] #
#################################################
while True:
    try:
        a = int(input('Input number 1:'))
    except ValueError:
        print("Only numbers please")
        continue

    c = str(input('Input operation'))

    try:
        b = int(input('Input number 2:'))
    except ValueError:
        print("Only numbers please")
        continue

    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a * b)
    elif c == "**":
        print(a ** b)
    elif c == "sqrt":
        print(a ** (1 / b))
    else:
        print("I don`t know this operatin. I`m still learning!")
