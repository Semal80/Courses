# вероятнее всего есть простое и более "красивое" решение.
# Считываю построчно загоняю в список, преобразовываю.
# Преобразование в глобальный список добавляю.
# Глобальный список загоняю в файл.

def filename(path):
    file_open = open(path)
    out_lines = []
    for line in file_open.readlines():
        outline = ""
        position = 0
        for symbol in line:
            position += 1
            # Проверка на условие 2 цифр подряд
            if (symbol.isdigit() is True) and (line[position-2].isdigit() is True):
                j = int(line[position-2:position])
                for i in range(j):
                    outline += line[position - 3]
            # проверка на условие 1 цифры, а следующая символ
            elif (symbol.isdigit() is True) and (line[position].isdigit() is False):
                j = int(symbol)
                for i in range(j):
                    outline += line[position-2]
        out_lines.append(outline + '\n')
    file_open.close()
    # чтобы файл не "рос" перезаписываю его
    file_out = open('output.txt', 'w')
    file_out.writelines(out_lines)
    file_out.close()


a = input("Input path to file:")
filename(a)
