# Get sentence fom user and capitalize full of it adding fullstop at the end
sentence = input("Enter a sentence: ")
if not sentence.endswith('.'):
    sentence += '.' # Add full stop if not present
sentence = sentence.strip()  # Remove leading and trailing spaces
sentence = sentence.capitalize()  # Capitalize the first letter of the sentence
# Capitalize the whole sentence
cap_sentence = sentence.upper()  # Convert to uppercase
# Display the formatted sentence
print("Formatted sentence:", cap_sentence)