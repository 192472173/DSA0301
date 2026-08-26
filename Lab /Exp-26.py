from transformers import pipeline

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = input("Enter English text: ")

result = translator(text)

print("French Translation:")
print(result[0]["translation_text"])
