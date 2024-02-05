sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_legths = [len(word) for word in words if word != "the"]
# for word in words:
#     if word != "the":
#         word_legths.append(len(word))
print(words)
print(word_legths)


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(num) for num in numbers if num > 0]
print(newlist)