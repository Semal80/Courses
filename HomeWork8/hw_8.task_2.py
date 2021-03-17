def division(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    return numbers

if __name__ == '__main__':
    a = int(input("Input number please:"))
    print(division(a))
