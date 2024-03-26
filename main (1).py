import re
import random

# Get input from the user
user_input = input("Enter a multi-line sentence: \n")

# Ask the user if they want invisible hairs between words
invisible_hairs_between_words = input(
    "Do you want invisible hairs between words? (y/n) ").lower() == "y"

# Ask the user if they want invisible hairs within words
invisible_hairs_within_words = input(
    "Do you want invisible hairs within words? (y/n) ").lower() == "y"

# Ask the user if they want homoglyph substitution
homoglyph_substitution = input(
    "Do you want homoglyph substitution? (y/n) ").lower() == "y"

# List of invisible hairs
invisible_hairs = [
    "\U0001D179", "\U0001D178", "\U0001D176", "\U0001D174", "\U0001D173"
]

# Homoglyphs mapping, Some are skipped because they look too weird
homoglyphs = {
    'A': 'Α',
    'a': 'а',
    'B': 'Β',
    'b': 'b',
    'C': 'Ϲ',
    'c': 'ϲ',
    'E': 'Ε',
    'e': 'е',
    'H': 'Η',
    'I': 'Ι',
    'i': 'і',
    'J': 'Ј',
    'j': 'ј',
    'K': 'Κ',
    'k': 'k',
    'M': 'Μ',
    'm': 'm',
    'O': 'Ο',
    'o': 'о',
    'P': 'Ρ',
    'p': 'р',
    'Q': 'R',
    'q': 'ԛ',
    'S': 'Ѕ',
    's': 'ѕ',
    'T': 'Τ',
    't': 't',
    'W': 'W',
    'w': 'w',
    'X': 'Χ',
    'x': 'х',
    'Y': 'Ү',
    'y': 'у',
    'Z': 'Ζ',
    'z': 'z',
}

# Initialize the result string
result = ""

# Split the input text into sentences
sentences = re.split('(?<=[.!?]) +', user_input)
for i in range(len(sentences)):
  sentences[i] = sentences[i].strip()  # Remove leading/trailing spaces

# Add standard space between words and add a space after sentences that end with a period, exclamation mark, or question mark
for i, sentence in enumerate(sentences):
  words = sentence.split(" ")
  # Ensure at least one word in a sentence has an invisible hair
  words_with_length_greater_than_one = [
      word for word in words if len(word) > 1
  ]
  if words_with_length_greater_than_one:  # Check if the list is not empty
    word_with_hair = random.choice(words_with_length_greater_than_one)
    for j, word in enumerate(words):
      if word and len(word) > 1:  # Ignore words that are only one letter
        if invisible_hairs_within_words and (
            word == word_with_hair or random.random() < 0.67):  # 67% chance
          insert_position = random.randint(
              1,
              len(word) -
              1)  # Random position to insert the invisible hair space
          word = word[:insert_position] + random.choice(
              invisible_hairs) + word[
                  insert_position:]  # Insert the invisible hair space
        # Homoglyph substitution
        if homoglyph_substitution and random.random() < 0.33:
          word = ''.join([
              homoglyphs[char] if char in homoglyphs else char for char in word
          ])
      result += word  # Add the word to the result
      if j < len(words) - 1:  # If not the last word in the sentence
        if invisible_hairs_between_words and random.random(
        ) < 0.4:  # 40% chance
          result += random.choice(
              invisible_hairs
          )  # Add random invisible hair space after the space
        result += " "  # Add a standard space between words
    if i < len(sentences) - 1:  # If not the last sentence
      result += " "  # Add space after the sentence

# Display the result
print("Result:", result)
