# look at EmojiConverter.py for Reference
def emoji_converter(word):
    words = word.split(' ')  # to make the words split and not be together
    emojis = {
        ":)": "😀",
        ":(": "🙁"
    }
    converter = ""
    for word in words:
        converter += emojis.get(word, word) + ' '
    return converter


word = input(">")
print(emoji_converter(word))





