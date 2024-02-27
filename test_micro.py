from translator_microservice import detect_language
from translator_microservice import translate_text

if __name__ == "__main__":
    while True:
        text = input("Enter a text to detect its language and translate (or 'exit' to quit): ")
        if text.lower() == "exit":
            break
        target_language = input("Enter the target language (e.g. French): ")
        detected_language = detect_language(text)
        print("Detected language:", detected_language)
        translated_text = translate_text(text, target_language)
        print("Translated text:", translated_text)
