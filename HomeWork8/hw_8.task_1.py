def acronim(in_words):
    word = []
    string = ""
    for lett in in_words.split():
        word.append(lett[0].upper())
    return string.join(word)


a = str(input("Write a several words. Please :"))
print(acronim(a))
