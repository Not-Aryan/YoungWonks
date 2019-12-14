def aaa(word, offset):
    letters = "abcdefghijklmnopqrstuvwxyz" 
    output = ""
    for char in word:
        if char in letters:
            newIndex = (letters.index(char) + offset) % 26
            output = output + letters[newIndex]
        else:
            output = output + char
    return output
    


