def clean_text(text):
    cleaned_text=text.strip().lower()
    return cleaned_text

def is_long_prompt(text):
    return len(text)>20