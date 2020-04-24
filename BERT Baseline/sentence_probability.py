import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM
import numpy as np
import math

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

def predict(text, bert_model, bert_tokenizer):
    # Tokenized input
    # text = "[CLS] I got restricted because Tom reported my reply [SEP]"
    text = "[CLS] " + text + " [SEP]"
    tokenized_text = bert_tokenizer.tokenize(text)
    # text = "[CLS] Stir the mixture until it is done [SEP]"
        #masked_index = 4
    sentence_prob = 1
    for masked_index in range(1,len(tokenized_text)-1):
        # Mask a token that we will try to predict back with `BertForMaskedLM`
        masked_word = tokenized_text[masked_index]
        #tokenized_text[masked_index] = '[MASK]'
        # assert tokenized_text == ['[CLS]', 'who', 'was', 'jim', 'henson', '?', '[SEP]', 'jim', '[MASK]', 'was', 'a', 'puppet', '##eer', '[SEP]']
        # print (tokenized_text)

        # Convert token to vocabulary indices
        indexed_tokens = bert_tokenizer.convert_tokens_to_ids(tokenized_text)
        # Define sentence A and B indices associated to 1st and 2nd sentences (see paper)
        # segments_ids = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        length = len(tokenized_text)
        segments_ids = [0 for _ in range(length)]
        # Convert inputs to PyTorch tensors
        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        # If you have a GPU, put everything on cuda
        tokens_tensor = tokens_tensor.to('cuda')
        segments_tensors = segments_tensors.to('cuda')

        # Load pre-trained model (weights)
        # bert_model = BertForMaskedLM.from_pretrained('bert-large-uncased')
        # bert_model.eval()

        # If you have a GPU, put everything on cuda
        tokens_tensor = tokens_tensor.to('cuda')
        segments_tensors = segments_tensors.to('cuda')
        bert_model.to('cuda')

        # Predict all tokens
        with torch.no_grad():
            predictions = bert_model(tokens_tensor, segments_tensors)

        predictions = torch.nn.functional.softmax(predictions, -1)

        index = bert_tokenizer.convert_tokens_to_ids([masked_word])[0]

        curr_prob = predictions[0, masked_index][index]
        # predict_list = predictions[0, masked_index]
        sentence_prob *= curr_prob
        #tokenized_text[masked_index] = masked_word
    return math.pow(sentence_prob, 1/(len(tokenized_text)-3))
    #return sentence_prob
'''
# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('./tmp/swag_output/')
# Load pre-trained model (weights)
model = BertForMaskedLM.from_pretrained('./tmp/swag_output/')
model.eval()

'''

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
# Load pre-trained model (weights)
model = BertForMaskedLM.from_pretrained('bert-large-uncased')
model.eval()


# prob = predict(sentence_1, bert_model=model, bert_tokenizer=tokenizer)

with open("ConcatenatedSentences.txt", "r") as f:
    file = f.readlines()

num = len(file)
count = 0
curr = 0
for i in file:
    label, sentence_1, sentence_2, sentence_3 = i.split("\001")
    print (label[0])
    prob_1 = predict(sentence_1, bert_model=model, bert_tokenizer=tokenizer)
    prob_2 = predict(sentence_2, bert_model=model, bert_tokenizer=tokenizer)
    prob_3 = predict(sentence_3, bert_model=model, bert_tokenizer=tokenizer)
    answer = max(prob_1, prob_2, prob_3)
    if (prob_1 == answer and label[0] == "A") or (prob_2 == answer and label[0] == "B") \
            or (prob_3 == answer and label[0] == "C"):
        count += 1
        print (count)

    print(count, curr)
    curr += 1
print (count/num)












