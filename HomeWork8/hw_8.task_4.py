import os
import pprint


def wolk_recursion(path):
    list_p = []
    list_tuple = ()
    dir_names = []
    file_names = []
    for list_name in os.listdir(path):
        path_name = os.path.join(path, list_name)
        if os.path.isdir(path_name):
            dir_names.append(list_name)
        else:
            file_names.append(list_name)
    list_tuple = (path, dir_names, file_names)
    list_p.append(list_tuple)
    print(list_p)

    if (dir_names == []) and (file_names == []):
        return
    else:
        for list_name in os.listdir(path):
            path_name = os.path.join(path, list_name)
            if os.path.isdir(path_name):
                wolk_recursion(path_name)


if __name__ == '__main__':
    print(wolk_recursion('/home/nepromah/TestWalkRecurs'))
    # Для сверки результатов
    # print(pprint.pprint(list(os.walk('/home/nepromah/TestWalkRecurs'))))
