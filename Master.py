def anagramComp(word1, word2):
        return word1.lower() == word2.lower()



print("What are the words that you want to check if they are anagram?")
word1 = input("Input the first word here: ")
word2 = input("Input the second word here: ")
anagramComp(word1, word2)
