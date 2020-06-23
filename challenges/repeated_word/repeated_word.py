def repeated_word(string):
    word_array = []
    lowered_string = string.lower()
    for word in lowered_string.split():
        if word in word_array:
            print(word)
            return word
            break
        else:
            word_array.append(word)

repeated_word('Dog cat turtle dog')