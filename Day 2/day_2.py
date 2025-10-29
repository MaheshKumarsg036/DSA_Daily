
# 1. Check Empty String
# Problem: Given a string, check if it is empty or not.
# Example: Input: "" → Output: Empty String


def check_empty(s):
    if s == "":
        return "Empty String"
    return "Non-Empty String"

# 2. Check First Character
# Problem: Given a string, check if its first character is a vowel or consonant.
# Example: Input: "Apple" → Output: Vowel


def first_chat_vowel(s):
    vowels = ['a','e','i','o','u']

    if s[0].lower() in vowels:
        return "Vowel"
    return "Consonant"

# 3. String Length Check
# Problem: Given a string, check if its length is greater than 5.
# Example: Input: "Hi" → Output: Length is less than or equal to 5

def len_string(s):
    len = 0
    for char in s:
        len += 1
        if len > 5:
            return "Greater than 5"
        
    return "Less than or equal to 5"




    