message = input('>')
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "🙁"
}
converter = ""
for word in words:
    converter += emojis.get(word, word) + ' '
print(converter)