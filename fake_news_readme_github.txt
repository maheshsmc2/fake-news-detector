# 📰 Fake News Detector (ML Web App)

This machine learning app classifies news text as **FAKE** or **REAL** using **TF-IDF vectorization** and **PassiveAggressiveClassifier**. Built with **scikit-learn** and deployed via **Gradio**.

---

## 🚀 Live Demo
🔗 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/maheshc/fake-news-detector) *(replace with your actual link)*

---

## 📦 Features
- Classifies text as FAKE or REAL
- TF-IDF vectorization to convert text into numerical vectors
- PassiveAggressiveClassifier for fast online learning
- Gradio interface for interactive use
- Deployed to Hugging Face Spaces

---

## 🧠 Concepts Learned
- TF-IDF vectorization
- PassiveAggressiveClassifier for binary classification
- Text preprocessing
- Model training and testing
- Gradio UI app development

---

## 📊 Dataset
- Small custom dataset with 10 labeled news headlines:
  - FAKE: "COVID-19 vaccines cause microchip implants"
  - REAL: "NASA successfully landed astronauts on the moon in 1969"

---

## 🔁 ML Pipeline Flow
```text
1. Load and clean the dataset
2. Vectorize the text using TF-IDF
3. Train/test split
4. Train PassiveAggressiveClassifier
5. Define prediction function
6. Build Gradio web interface
7. Deploy to Hugging Face
```

---

## 💻 How to Run Locally
```bash
pip install -r requirements.txt
python app.py
```

---

## 📁 File Structure
```
├── app.py              # Gradio app script
├── news.csv            # Sample labeled dataset
├── requirements.txt    # Python dependencies
```

---

## 📸 Screenshot
*(Upload screenshot if available)*

---

## 👤 Author
Built by Mahesh C — Learning AI one project at a time 🤖

---

## 📝 License
This project is for learning purposes and is MIT-licensed.
