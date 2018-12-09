import pyphen

s = pyphen.Pyphen(lang="en")

def count(word):
    """
    Returns the syllable count for a word
    """
    return len(s.inserted(word).split("-"))

print(count("elephant"))
print(count("Madagascar"))

# What makes a syllabe?
# Every syllable must have a vowel, and every vowel makes a syllable. 
# Exceptions: double vowels (aardvark, 3 vowels, 2 syllables)