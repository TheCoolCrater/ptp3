msg = input("Text >>> ")
words = msg.split(' ')
emoji = {
    ":)":"đ",
    ":(":"âšī¸",
    ":|":"đ",
    "=)":"đ",
    "-_-":"đ"
}

output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)