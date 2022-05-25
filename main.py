# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(word1, word2):
    # [assignment] Add your code here
    import re

    temp = re.compile('[\W_]+')
    check = 0
    subject = temp.sub('', word1).lower()
    anagram = temp.sub('', word2).lower()
    for char in subject:
        if char in anagram:
            check += 1
    if check == len(anagram):
        print(f'"{word1}" and "{word2}" are Anagrams')
        return True
    else:
        print(f'"{word1}" and "{word2}" are not Anagrams')
        return False


find_anagrams('adobe', 'abode')
find_anagrams('New York Times', 'monkeys write')
find_anagrams('Church of Scientology','rich-chosen goofy cult')
find_anagrams('McDonald\'s restaurants', 'Uncle Sam\'s standard rot')
find_anagrams('coronavirus', "carnivorous")
find_anagrams("She Sells Sanctuary", "Santa; shy, less cruel")
find_anagrams("adultery", "true lady")
find_anagrams("eleven plus two", "twelve plus one")
