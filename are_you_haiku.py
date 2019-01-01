# What makes a syllabe?
# Every syllable must have a vowel, and every vowel makes a syllable. 
# Exceptions: double vowels (aardvark, 3 vowels, 2 syllables)

vowels = set(["a", "e", "i", "o", "u", "y"])

def count_vowel_groups(word):
    """
    Counts syllables in words
    """
    last = None
    count = 0
    for l in word:
        if l not in vowels:
            last = l
        elif l in vowels and last in vowels:
            last = l
        elif l in vowels and last not in vowels:
            count += 1
            last = l
    return count

def add_word_to_vowel_count(tweet):
    """
    Takes a tweet, splits it into words
    counts the syllable for each word:
    "Hello, World"
    [("Hello,", 2), ("World", 1)]
    """
    tweet = tweet.split()
    counts = []
    for word in tweet:
        count = count_vowel_groups(word)
        counts.append((word, count))
    return counts

def fits_in_5_7_5(parsed_tweet):
    """
    Takes words and counts, returns haikuified tweet or False
    """
    line = 0
    target = 5
    reformed = ""
    for word_info in parsed_tweet:
        line += word_info[1]
        reformed += word_info[0] + " "
        if line < target:
            continue
        if line == target:
            target = 12 if target == 5 else 17
            reformed += "\n"
        elif line > target:
            return False
    return reformed


tweet = "I was in fire, The room was dark and somber. I sleep peacefully."
tweet = "Mellow, mild, May day, calling children out to play. Summer's on her way!"

tweet = add_word_to_vowel_count(tweet)
print(fits_in_5_7_5(tweet))