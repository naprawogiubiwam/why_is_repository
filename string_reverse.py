def string_reverse(text):
    reverse_text = ''
    for i in text:
        reverse_text = i + reverse_text
    return reverse_text

text = input("Enter a string to reverse: ")
print(string_reverse(text))

