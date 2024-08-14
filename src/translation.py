import requests

def translate_to_french(text):
    """
    Translates the given text to French using the Google Translate API.
    """
    try:
        # Example API call (replace with actual API details)
        url = "https://translation.googleapis.com/language/translate/v2"
        params = {
            'q': text,
            'target': 'fr',
            'key': 'YOUR_API_KEY'  # Replace with your actual API key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        translation = response.json().get('data', {}).get('translations', [{}])[0].get('translatedText', '')
        return translation
    except Exception as e:
        print(f"Error during translation: {e}")
        return text  # Return original text in case of error
