# Input string
input_string = "Pooja is a good good is a girl"

# Split the string into words
words = input_string.split()

# Create a dictionary to store word counts
word_counts = {}

# Iterate through the words and count their occurrences
for word in words:
    # Remove any punctuation or special characters (if needed)
    word = word.strip(".,!?")

    # Convert the word to lowercase to make the count case-insensitive
    word = word.lower()

    # Update the word count in the dictionary
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
