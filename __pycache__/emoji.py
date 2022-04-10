


message=input(">")
words=message.split(" ")
print(words)
emoji={
    ":)": "happy",
    ":(": "sad"
}
output=""
for word in words:
    output+=emoji.get(word,word)+ " "
print(output)