from flask import Flask, request, jsonify, render_template
from transformers import BertTokenizer, TFBertForSequenceClassification
import numpy as np

app = Flask(__name__)

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('./saved_model2/tokenizer')
model = TFBertForSequenceClassification.from_pretrained('./saved_model2/model')

def preprocess_text(text):
    # Add your text preprocessing steps here
    text = text.lower()  # Example step: convert to lowercase
    return text

def handle_negation(text):
    # Add your negation handling steps here
    return text

def classify_text(text, model, tokenizer, max_length=128):
    print("WWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE AAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRREEEEEEEEEEEEEEEE in      classify")
    # Preprocess text
    text = preprocess_text(text)
    text = handle_negation(text)
    # Tokenize text
    print("WWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE AAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRREEEEEEEEEEEEEEEE in      Tokenize")
    inputs = tokenizer.encode_plus(text, max_length=max_length, truncation=True, padding='max_length', add_special_tokens=True)
    input_ids = np.array([inputs['input_ids']])
    attention_mask = np.array([inputs['attention_mask']])
    # Predict
    print("WWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE AAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRREEEEEEEEEEEEEEEE in      Predict")
    predictions = model.predict({'input_ids': input_ids, 'attention_mask': attention_mask})
    print("WWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE AAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRREEEEEEEEEEEEEEEE in      Predict RRRRRRRRRREEEEEEEEESUUUUUUUUUUUUUUULLLLLLLLLLT",predictions)
    label_id = np.argmax(predictions[0], axis=1).flatten()
    return label_id[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    text_to_classify = request.form['text']
    prediction = classify_text(text_to_classify, model, tokenizer)
    if prediction == 0:
        result = "Non-Racist. It is good to post."
    else:
        result = "Racist. You cannot post it."
    print("GFJGHVHGFDGHKJ",result)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
