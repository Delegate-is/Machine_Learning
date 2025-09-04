# count vowel variables in sent
sent = "This is a sample sentence to count vowels."
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in sent if char in vowels)
print(f"Number of vowels in the sentence: {vowel_count}")
# count consonant variables in sent
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
consonant_count = sum(1 for char in sent if char in consonants)
print(f"Number of consonants in the sentence: {consonant_count}")
# count special characters in sent
special_char_count = sum(1 for char in sent if not char.isalnum() and not char.isspace())
print(f"Number of special characters in the sentence: {special_char_count}")
sent2 = "Another example sentence, with punctuation!"
# count vowel variables in sent2
vowels = 'aeiouAEIOU'
vowel_count2 = 0
for i in sent2:
    if i in vowels:
        print(f"{i} is a vowel")
        vowel_count2 += 1
print(f"Total vowels counted in sent2: {vowel_count2}")