from transformers import pipeline

classifier = pipeline('text-classification', model='tinybert-sentiment-analysis', device='cuda')
# classifier(data)