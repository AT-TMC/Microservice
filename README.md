### README
---

## Translation Microservice

### Communication Contract

This microservice provides language detection and translation functionalities. Below are the instructions on how to programmatically request and receive data.

#### Requesting Data

To request language detection or translation, call the following functions in your Python code:

- `detect_language(text)`: Pass the `text` to detect the language.
- `translate_text(text, target_language)`: Pass the `text` and `target_language` to translate the text.

Example Usage:
```python
detected_language = detect_language("Hello, how are you?")
print("Detected Language:", detected_language)

translated_text = translate_text("Hello, how are you?", "Spanish")
print("Translated Text:", translated_text)
```

#### Receiving Data

The functions will return the following:

- For `detect_language(text)`:
  - Returns: Detected language as a string.
- For `translate_text(text, target_language)`:
  - Returns: Translated text as a string.

### UML Sequence Diagram

Below is a detailed UML sequence diagram showing how requesting and receiving data works:

![sequence_diagram](https://github.com/AT-TMC/Microservice/assets/99299362/4424ceb3-ce9a-46b5-a4d3-e345d7ef7da3)

---


#### Note:
- Make sure to install the required libraries using `pip install langdetect googletrans==4.0.0-rc1`.
- Replace the `LANGUAGE_CODES` dictionary with the full list of language codes as needed.

### Thank you for using our Translation Microservice! 🌐

---
