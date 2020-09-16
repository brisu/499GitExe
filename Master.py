from collections import Counter
def anagramComp(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return Counter(word1.strip()) == Counter(word2.strip())



print("What are the words that you want to check if they are anagram?")
word1 = input("Input the first word here: ")
word2 = input("Input the second word here: ")
anagramComp(word1, word2)
