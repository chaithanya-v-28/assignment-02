#ask for user input
text = input("Enter word: ")
#store original
original = text
#reverse the input
reversed_text = text[::-1]
#display original and reversed
print("Original: ", original)
print("Reversed: ", reversed_text)
#check palindrome
if text.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")     