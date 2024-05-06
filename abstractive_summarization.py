import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

# Initialize The Pretrained Model

model=T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer=T5Tokenizer.from_pretrained('t5-small')
device=torch.device('cpu')

def abstractive_summarizer(raw_text):

    input = tokenizer.encode("summarize: " + raw_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(
    input, 
    max_length=150, 
    min_length=40, 
    length_penalty=5.0, 
    num_beams=4, 
    early_stopping=True)
    
    x=outputs

    summary=(tokenizer.decode(x[0]))
    return summary

