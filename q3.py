#Ask user for the input
sentence = input("enter a sentence: ")
#Calculation for length of sentence with space
with_space = len(sentence)
#Calculation for length of sentence without space
without_space = len("".join(sentence.split()))
#Calculation for words
words = sentence.split()

#Display result
#print original sentence
print("Original: ", sentence)
#print sentence with space
print("Character (with space):" ,with_space)
#print sentence without space
print("Character (without space):" ,without_space)
#print length of words
print("words:",len(words))
#print sentence in uppercase
print(sentence.upper())
#print sentence in lower case
print(sentence.lower())
#print title of the sentence
print(sentence.title())
#print first word of the sentence
print("First word:",words[0])
#print last word of the sentence
print("Last word:", words[-1])
#print reversed sentence
print("Reversed:", sentence[::-1])
