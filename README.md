# 📝 Text Summarization Tool

A professional Python-based **Text Summarization Tool** that leverages **Natural Language Processing (NLP)** techniques to automatically condense lengthy articles into concise summaries.  
This project demonstrates the use of **NLTK** for tokenization, stopword removal, frequency analysis, and sentence ranking.  

---

## 🎯 Objective
The goal of this task is to:
- Develop a tool that summarizes lengthy articles using NLP techniques.  
- Provide a Python script that showcases both **input text** and the resulting **concise summary**.  

---

## 🚀 Key Features
- **Sentence & Word Tokenization** using NLTK  
- **Stopword Filtering** for noise reduction  
- **Word Frequency Calculation** to identify importance  
- **Sentence Scoring & Ranking** based on frequency  
- **Concise Summary Generation** from top-ranked sentences  

---

## 📂 Project Structure
📁 text-summarizer
├── summarizer.py # Core summarization logic


---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer

2. Install the required Python libraries:

pip install nltk


3. Download necessary NLTK resources:

python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> nltk.download('punkt_tab')
>>> exit()

---

▶️ Usage
Run the script from your terminal:

python summarizer.py


Example Output:

--- Original Text ---
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals and humans. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in Tesler's Theorem says "AI is whatever hasn't been done yet." For instance, optical character recognition is frequently excluded from things considered to be "AI", having become a routine technology. Modern machine capabilities generally classified as AI include successfully understanding human speech, competing at the highest level in strategic game systems (such as chess and Go), autonomous cars, intelligent routing in content delivery networks and military simulations.

==================================================

--- Concise Summary ---

As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.
Modern machine capabilities generally classified as AI include successfully understanding human speech, competing at the highest level in strategic game systems (such as chess and Go), autonomous cars, intelligent routing in content delivery networks and military simulations.

---

## 🔮 Future Scope

1.Summarization from external files (TXT, PDF, DOCX)
2.Summarization from web articles/URLs
3.Interactive Streamlit Web Application for user-friendly summarization

---


📬 Contact
Feel free to connect regarding the project

LinkedIn at https://www.linkedin.com/in/sowmiya-k-378b14328

or
email at sowmiya140605@mail.com
