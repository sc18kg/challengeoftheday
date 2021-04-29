def alphasort(string):
    string_split = string.split(' ')

    word_list = []
    for i in string_split:
        if i not in word_list:
             word_list.append(i)
        else:
            continue
        word_list.sort()
    return ((' ').join(word_list))

