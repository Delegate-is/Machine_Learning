from deep_translator import GoogleTranslator

def english_to_arabic():
    print("📘 English to Arabic Dictionary App")
    print("Type 'exit' to quit\n")

    while True:
        word = input("Enter an English word: ")
        if word.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            translation = GoogleTranslator(source='en', target='ar').translate(word)
            print(f"👉 Arabic Translation: {translation}\n")
        except Exception as e:
            print(f"❌ Error: Could not translate. {e}\n")

# Run the app
english_to_arabic()
