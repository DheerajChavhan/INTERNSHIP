from prompt_utils import clean_text, is_long_prompt

cleaned_text=clean_text(" Write a detailed blog on Generative AI in simple words ")
is_long_prompt(" Write a detailed blog on Generative AI in simple words ")

print(cleaned_text)
print(is_long_prompt(cleaned_text))