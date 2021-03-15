############################
#  Решето Эратосфена       #
############################
while True:
    try:
        a = int(input("Input number:"))
    except ValueError:
        print("Only numbers please")
        continue

    era_numbers = list(range(a + 1))

    for i in era_numbers:
        if i > 1:
            # это решение c интернета оно "красивое", но пока не понимаю 3 переменных в методе
            # for j in range(i + i, len(era_numbers), i):
            #     era_numbers[j] = 0
            for j in range(i + 1, len(era_numbers)):
                if era_numbers[j] % era_numbers[i] == 0:
                    era_numbers[j] = 0
    # перевожу в множества и обратно для удаления дубликатов нуля
    era_numbers = list(set(era_numbers))
    print(era_numbers)
