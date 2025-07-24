import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import gradio as gr

# Load data
df = pd.read_csv("news.csv")

# Split data
X = df['text']
y = df['label']
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = tfidf.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(X_train, y_train)

# Predict
def predict_news(text):
    vec = tfidf.transform([text])
    return model.predict(vec)[0]

# Gradio Interface
iface = gr.Interface(fn=predict_news, inputs="text", outputs="text", title="📰 Fake News Detector")

if __name__ == "__main__":
    iface.launch()
