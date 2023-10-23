message = input(">>> ")

emoji_mapping = {
    ":)" : "🙂",
    ":D" : "😁",
    ":(" : "☹️",
    ":|" : "😐",
}

words = message.split(" ")

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "

print(output)