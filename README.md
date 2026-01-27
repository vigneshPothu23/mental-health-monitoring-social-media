# 🧠 Mental Health Monitoring on Social Media
### An NLP System Combining Emotion and Sarcasm Signals for Context-Aware Analysis

---

## 🌍 Overview

This project presents a **fusion-based system** for monitoring mental health signals on social media by combining **emotion detection** and **sarcasm detection**.  
Instead of relying on a single prediction, the system integrates multiple perspectives to produce more context-aware insights.

---

## 🏗️ High-Level System Flow

Social Media Input
│
▼
Emotion Detection ─┐
├──► Fusion Inference ───► Final Output
Sarcasm Detection ─┘
│
▼
Flask App


---

## 📓 Notebooks Used

The core logic of the system is implemented across **three Jupyter notebooks**:

- `01_data_loading-restored.ipynb` – data preparation and preprocessing  
- `02_sarcasm_detection.ipynb` – sarcasm classification pipeline  
- `03_fusion_inference.ipynb` – fusion logic and final inference  

These notebooks collectively define the **end-to-end learning and inference workflow**.

---

## 🔁 Reproducibility & Design Philosophy

- The repository focuses on **clarity, structure, and reproducibility**
- All learning and inference logic is captured in notebooks
- Dependencies are explicitly defined for consistent execution
- Version control is used to track **system evolution**, not data storage

---

## 🛠️ Tech Stack

- Python  
- Transformers (DistilBERT)  
- Scikit-learn  
- Pandas, NumPy  
- Flask  
- Jupyter Notebook  

---

## 🎯 Potential Applications

- Mental health trend monitoring  
- Social media behavior analysis  
- Emotion–sarcasm interaction studies  
- NLP system design demonstrations  

---

## 👤 Author

**Vignesh Pothu**  
Computer Science | Machine Learning & NLP





\## Note

Datasets, training splits, and trained models are intentionally excluded

from this repository.



