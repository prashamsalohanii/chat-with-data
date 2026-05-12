#Chat with Your Data  AI CSV Analyzer
An AI-powered chatbot that lets you explore any CSV dataset using plain English. Upload your data, ask questions, and get instant intelligent answers no SQL or coding required!


## What It Does

Upload any `.csv` file and ask questions like:

- *"What is the average age?"*
- *"Which city has the most orders?"*
- *"How many rows have missing values?"*
- *"What is the total revenue?"*
- *"Summarize this dataset for me"*

---

##  Features

- Upload any CSV — works with any dataset
- Natural language chat — ask questions in plain English
-  Auto dataset summary — rows, columns, data types shown instantly
-  Context-aware answers — AI uses actual data stats to answer
- Super fast — powered by Groq's low-latency API
-  Chat history — remembers your conversation in the session

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Streamlit | Frontend web UI |
| Groq API | LLM (llama-3.3-70b-versatile) |
| Pandas | Data loading and analysis |
| python-dotenv | Secure API key management |

---

##  Installation & Setup

### 1. Clone the repository
git clone https://github.com/Prashamsalohanii/chat-with-data.git
cd chat-with-data

### 2. Install dependencies
pip install -r requirements.txt

### 3. Get your free Groq API key
- Go to https://console.groq.com
- Sign up for free (no credit card needed)
- Click API Keys → Create API Key

### 4. Create a .env file
GROQ_API_KEY=your_api_key_here

### 5. Run the app
streamlit run app.py

### 6. Open browser
http://localhost:8501

---

---

##  How It Works

1. User uploads a CSV file
2. Pandas reads and analyzes the dataset
3. Dataset info sent to Groq LLM as context
4. User asks a question in plain English
5. Groq LLM answers based on real data
6. Answer displayed in clean chat UI

---

## Security

- .env file is in .gitignore — your API key is never uploaded to GitHub
- No user data is stored — everything stays in your browser session

---

##  Author

**Prashamsa Lohani**
- Website: https://prashamsalohani.com.np
- Email: Prashamsalohani18@gmail.com
- GitHub: https://github.com/Prashamsalohanii

---

##  License

This project is open source and available under the MIT License.

---
