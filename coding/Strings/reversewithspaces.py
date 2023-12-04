class stringexample:

    def stringrevers(self):
        str = "Today is a good day"
        print(str[::-1])

    def reverse_string_with_spaces(self):
        input_str = "Today is a good day"
        words = input_str.split(" ")

        # Reverse the list of words and join them back with spaces
        reversed_str = " ".join(reversed(words))

        print(reversed_str)

    def reverse_words_in_string_atsameplace(self):
        input_str = "ab bbb cccc dddddd"
        words = input_str.split(" ")

        for word in words:
            if word % 2 == 0:
                print(word)


val = stringexample()
val.stringrevers()
val.reverse_string_with_spaces()
val.reverse_words_in_string_atsameplace()
