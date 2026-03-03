text = input('Enter a string:')

# Reversing the string using slicing
reversed_text = text[::-1]
print('Reversed string:', reversed_text)

# counting the number of vowels in the string
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print('Number of vowels in the string:', vowel_count)

# converting the string to uppercase
uppercase_text = text.upper()
print('Uppercase string:', uppercase_text)

# converting the string to lowercase
lowercase_text = text.lower()
print('Lowercase string:', lowercase_text)
 
# checking if the string is a palindrome
if text == reversed_text:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')

# counting the number of words in the string
word_count = len(text.split())
print('Number of words in the string:', word_count)

