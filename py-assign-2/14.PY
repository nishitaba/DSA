#14.	Write a function to check whether a string is a palindrome.
def is_palindrome(text):
    clean_text = text.lower()
    return clean_text == clean_text[::-1]
print