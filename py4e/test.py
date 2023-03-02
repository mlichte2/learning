
array = ['hello', 'world', 'this', 'is', 'great']


def smash(words):
    string = ""
    string = " ".join(words)
    return string


new_string = smash(array)
print(new_string)
