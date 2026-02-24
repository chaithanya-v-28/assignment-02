# take input from user
text = input("Enter text: ")
#split into words
words = text.split()
#count vowels
vowels = sum(1 for c in text.lower() if c in 'aeiou')
#count consonants
consonants = sum(1 for c in text.lower()if c.isalpha() and c not in 'aeiou')
#reverse the string
reversed_text = text[::-1]
#check if reversed or not
palindrome = ''.join(c.lower() for c in text if c.isalnum()) == ''.join(c.lower()for c in text if c.isalnum())[::-1]
#remove vowels
no_vowels = ''.join(c for c in text if c.lower() not in 'aeiou')
#count freq of each word
freq = {w: words.count(w) for w in set(words)}
#find the longest word 
longest = max(words, key = len) if words else " "
#display outputs
print(f"Words: {len(words)}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Reversd: {reversed_text}")
print(f"Palindrome: {'Yes' if palindrome else 'No'}")
print(f"Without vowels: {no_vowels}")
print(f"Longest word: {longest} ({len(longest)}letters)")
print(f"Word frequency:", ','.join(f"{k}:{v}" for k,v in freq.items()) )