from flask import Flask, render_template, request
import torch
import torch.nn.functional as F
import numpy as np
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load Emotion Model & Tokenizer
# -----------------------------
EMOTION_MODEL_PATH = "distilbert_emotion_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(EMOTION_MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(EMOTION_MODEL_PATH)
model.eval()

# -----------------------------
# Load Sarcasm Model & Tokenizer
# -----------------------------
SARCASM_MODEL_PATH = "distilbert_sarcasm_model"

sarcasm_tokenizer = DistilBertTokenizerFast.from_pretrained(SARCASM_MODEL_PATH)
sarcasm_model = DistilBertForSequenceClassification.from_pretrained(SARCASM_MODEL_PATH)
sarcasm_model.eval()

sarcasm_labels = ["not_sarcastic", "sarcastic"]

# -----------------------------
# Emotion Labels & Emojis
# -----------------------------
emotion_labels = ["anger", "fear", "joy", "love", "sadness", "surprise"]

emotion_emojis = {
    "anger": "😡",
    "fear": "😱",
    "joy": "😊",
    "love": "❤️",
    "sadness": "😢",
    "surprise": "😲"
}

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    scores = None
    emoji = None

    sarcasm = None
    sarcasm_confidence = None

    user_text = ""

    if request.method == "POST":
        user_text = request.form["text"]

        # ---------- Emotion Prediction ----------
        inputs = tokenizer(
            user_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)

        confidences = probs.numpy()[0]
        pred_index = int(np.argmax(confidences))

        prediction = emotion_labels[pred_index]
        emoji = emotion_emojis[prediction]
        confidence = round(float(confidences[pred_index]) * 100, 2)

        scores = [
            (emotion_labels[i], round(float(confidences[i]) * 100, 2))
            for i in range(len(emotion_labels))
        ]

        # ---------- Sarcasm Prediction ----------
        s_inputs = sarcasm_tokenizer(
            user_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            s_outputs = sarcasm_model(**s_inputs)
            s_probs = F.softmax(s_outputs.logits, dim=1)

        s_conf = s_probs.numpy()[0]
        s_index = int(np.argmax(s_conf))

        sarcasm = sarcasm_labels[s_index]
        sarcasm_confidence = round(float(s_conf[s_index]) * 100, 2)

    return render_template(
        "index.html",
        text=user_text,
        prediction=prediction,
        confidence=confidence,
        scores=scores,
        emoji=emoji,
        sarcasm=sarcasm,
        sarcasm_confidence=sarcasm_confidence
    )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
