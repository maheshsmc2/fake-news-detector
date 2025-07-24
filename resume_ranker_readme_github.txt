# 📄 Resume Ranker (AI NLP Project)

This project ranks multiple resumes based on their relevance to a given **job description** using **TF-IDF** vectorization and **Cosine Similarity**. Built with **Gradio** for easy web interaction.

---

## 🚀 Live Demo
🔗 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/maheshc/resume-ranker) *(replace with your actual link)*

---

## 📦 Features
- Upload or use preloaded resumes
- Paste job description to get ranked matches
- Uses TF-IDF + Cosine Similarity for relevance scoring
- Lightweight NLP-based app (no training required)
- Built with Gradio and scikit-learn

---

## 🧠 Concepts Learned
- TF-IDF vectorization for text representation
- Cosine Similarity for matching
- Real-world HR use-case with resumes
- Text preprocessing and comparison logic
- Gradio UI app building and deployment

---

## 📊 Sample Dataset
- `job_description.txt`: 1 job spec for a Data Scientist
- `resume1.txt` to `resume4.txt`: Various resumes with varying skillsets

---

## 🔁 Flow
```text
1. Load job description and resumes (text format)
2. Convert all text to TF-IDF vectors
3. Use cosine similarity to compare resumes with job
4. Sort and display resume scores
5. Interact using Gradio
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
├── app.py                # Gradio-based main app
├── job_description.txt   # Sample job description
├── resume1.txt           # Resume samples (1–4)
├── requirements.txt      # Python dependencies
```

---

## 📸 Screenshot
*(Optional: Add screenshot here)*

---

## 👤 Author
Built by Mahesh C — Project-based AI learning journey ✨

---

## 📝 License
This project is for educational purposes and is MIT-licensed.
