msg = input("Text >>> ")
words = msg.split(' ')
emoji = {
    ":)":"🙂",
    ":(":"☹️",
    ":|":"😐",
    "=)":"😊",
    "-_-":"😑"
}

output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)