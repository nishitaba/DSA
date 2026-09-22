#12.	Write a function to count vowels in a string.
def count_vowel(text):
    count = 0 
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1 
    return count
print(count_vowel("Nishitaba Rathore"))