### Language Detection and Translation Flask App

This Flask application provides endpoints for language detection and translation using the `langdetect` and `googletrans` libraries.

#### Setup

1. Install dependencies:
   ```bash
   pip install Flask langdetect googletrans==4.0.0-rc1
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

#### Endpoints

- **`/detect`**: Detects the language of the given text.
  - **Method**: POST
  - **Request Body**: JSON with a "text" field
  - **Response**: JSON with the detected language
  - Example Request:
    ```bash
    curl -X POST http://localhost:5000/detect \
      -H "Content-Type: application/json" \
      -d '{"text": "Hello, how are you?"}'
    ```
  - Example Response:
    ```json
    {"detected_language": "english"}
    ```

- **`/translate`**: Translates the given text to the specified target language.
  - **Method**: POST
  - **Request Body**: JSON with "text" and "target_language" fields
  - **Response**: JSON with the translated text
  - Example Request:
    ```bash
    curl -X POST http://localhost:5000/translate \
      -H "Content-Type: application/json" \
      -d '{"text": "Hello, how are you?", "target_language": "spanish"}'
    ```
  - Example Response:
    ```json
    {"translated_text": "Hola, ¿cómo estás?"}
    ```

#### Python Requests Example

Here's an example of how to make requests to the endpoints using Python's `requests` library:

```python
import requests

# URL for the detect endpoint
detect_url = 'http://localhost:5000/detect'
# Data for the detect endpoint
detect_data = {'text': 'Hello, how are you?'}

# Send POST request to detect endpoint
detect_response = requests.post(detect_url, json=detect_data)
# Print the detected language
print("Detected Language:", detect_response.json()['detected_language'])

# URL for the translate endpoint
translate_url = 'http://localhost:5000/translate'
# Data for the translate endpoint
translate_data = {
    'text': 'Hello, how are you?',
    'target_language': 'spanish'
}

# Send POST request to translate endpoint
translate_response = requests.post(translate_url, json=translate_data)
# Print the translated text
print("Translated Text:", translate_response.json()['translated_text'])
```

Ensure the Flask application is running (`python app.py`), then run the provided Python script to see how the `requests` library can be used to interact with the endpoints.

Feel free to modify the text and target language in the example for different translations and language detections.
### UML Sequence Diagram

Below is a detailed UML sequence diagram showing how requesting and receiving data works:


![sequence_diagram](https://github.com/AT-TMC/Microservice/assets/99299362/57ae3e43-da1a-404a-ab63-e24934ca1b30)

---


#### Note:
- Make sure to install the required libraries using `pip install langdetect googletrans==4.0.0-rc1`.
- Replace the `LANGUAGE_CODES` dictionary with the full list of language codes as needed.

### Thank you for using our Translation Microservice! 🌐

---
