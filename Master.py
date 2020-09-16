from collections import Counter
def anagramComp(word1, word2):
    word2 = word2.lower()

    temp1,temp2 = "", ""
    for i in word1:
        if i.isalpha():
            word1 = "".join([temp1, i])
    word1 = temp1.lower()

    for i in word2:
        if i.isalpha():
            word2 = "".join([temp2, i])
    word2 = temp2.lower()

    return sorted(word1) == sorted(word2)



print("What are the words that you want to check if they are anagram?")
word1 = input("Input the first word here: ")
word2 = input("Input the second word here: ")
anagramComp(word1, word2)
