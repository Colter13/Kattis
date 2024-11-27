from transformers import pipeline

# Load a pre-trained model and tokenizer
classifier = pipeline('sentiment-analysis')

text = "I am not super happy with the results of my project."
result = classifier(text)

print(result)
