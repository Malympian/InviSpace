# Get input from the user
user_input = input("Enter a multi-line sentence: \n")

# Split the input text into sentences
sentences = user_input.split(". ")
for i in range(len(sentences)):
    sentences[i] = sentences[i].strip()  # Remove leading/trailing spaces

# Join the sentences back with ". " to account for any splits missed
joined_sentences = ". ".join(sentences)

# Replace exclamation marks and question marks with unique symbols to preserve them
joined_sentences = joined_sentences.replace("!", "\u00A1 ")  # Unique symbol for exclamation mark
joined_sentences = joined_sentences.replace("?", "\u00BF ")  # Unique symbol for question mark

# Split the modified joined sentences into sentences
unique_sentences = joined_sentences.split(". ")
for i in range(len(unique_sentences)):
    unique_sentences[i] = unique_sentences[i].strip()  # Remove leading/trailing spaces

# Join the sentences back with ". " to maintain the modified unique symbols
modified_joined_sentences = ". ".join(unique_sentences)

# Replace back the unique symbols with exclamation marks and question marks
modified_joined_sentences = modified_joined_sentences.replace("\u00A1", "! ")
modified_joined_sentences = modified_joined_sentences.replace("\u00BF", "? ")

# Initialize the result string
result = ""

# Add standard space between words and add a space after sentences that end with a period, exclamation mark, or question mark
for i, quest_sentence in enumerate(modified_joined_sentences.split(". ")):  # Split by period
    words = quest_sentence.split(" ")
    for j, word in enumerate(words):
        if word:
            if j < len(words) - 1:  # If not the last word in the sentence
                if word[0].isupper():  # If the word starts with a capital letter
                    result += word + "\u0020" + "\U0001D178"  # Standard space followed by invisible hair space
                else:
                    result += word + "\u0020"  # Standard space
            else:  # If the last word in the sentence
                last_char = word[-1]
                if last_char in ['.', '!', '?']:  # If the last character is a punctuation mark
                    result += word[:-1] + "\U0001D178" + last_char + " "  # Invisible hair space, punctuation, and standard space
                else:  # If no punctuation mark at the end of the word
                    result += word + "\u0020"  # Standard space
            if i < len(unique_sentences) - 1:  # If not the last sentence
                result += "\U0001D178 "  # Add invisible hair space and space after the sentence

# Remove the extra space at the end
result = result.strip()

# Display the result
print("Result:", result)
