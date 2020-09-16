def anagramComp(word1, word2):
    if word1.lower() == word2.lower():
        print(word1 + " and "+ word2 + " are anagram")
        return
    else:
        print(word1 + " and "+ word2 + " are NOT anagram")



print("What are the words that you want to check if they are anagram?")
word1 = input("Input the first word here: ")
word2 = input("Input the second word here: ")
anagramComp(word1, word2)
