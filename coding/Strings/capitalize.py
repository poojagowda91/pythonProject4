input_str = "pooja is a good girl"
words = input_str.split(" ")

capitalized_words = []
for word in words:
    capitalized_word = word.capitalize()
    capitalized_words.append(capitalized_word)

result_str = " ".join(capitalized_words)
print(result_str)


