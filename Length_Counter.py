def length_counter(wordarg):
    words = wordarg.split(" ")

    word_length = []
    
    for word in words:
        to_add = len(word)

        if to_add not in word_length:
            word_length.append(to_add)
 
    return word_length

word = "Cart Cart Tea Sea Winter Mark"

print("The lengths are: ", length_counter(word))
