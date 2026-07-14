<!-- # MedicBot

## How to run?
### STEPS:

Clone the repository

'''bash
Project repo: https://github.com/
'''

### STEP - 01: Create a virtual environment after opening the repository 

'''bash
python -m venv MedicBot
'''

'''bash
MedicBot\Scripts\activate.bat
...

### STEP - 02: install the requirements
'''bash
pip install -r requirements.txt
... -->

# 🩺 MedicBot – AI-Powered Medical Assistant

MedicBot is an AI-powered medical chatbot built using **Retrieval-Augmented Generation (RAG)**. It answers users' medical queries by retrieving relevant information from trusted medical reference documents and generating context-aware responses using a Large Language Model (LLM).

Unlike traditional chatbots, MedicBot first searches a vector database for the most relevant medical content before generating an answer, improving factual accuracy and reducing hallucinations.

> **⚠️ Disclaimer:** MedicBot is developed for educational and informational purposes only. It should not be used as a replacement for professional medical advice, diagnosis, or treatment.

---

# 🚀 Features

- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Powered by **Qwen LLM**
- 🔍 Semantic search using **Qdrant Cloud**
- 📚 Hugging Face Sentence Transformers for embeddings
- 📄 Automatic PDF ingestion and indexing
- 💬 Interactive chatbot interface
- ⚡ Fast semantic retrieval
- ☁️ Cloud deployment ready (Render)
- 🔒 Uses trusted medical documents instead of relying solely on LLM knowledge

---

# 🏗️ System Architecture

```
                 User Query
                      │
                      ▼
              Flask Web Application
                      │
                      ▼
             LangChain Retrieval Chain
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
  Qdrant Vector Database      Qwen LLM
        ▲
        │
Sentence Transformer
(all-MiniLM-L6-v2)
        ▲
        │
 Medical PDF Documents
```

---

# 📂 Project Structure

```
MedicBot/
│
├── Data/                    # Medical PDF files (not included in repository)
├── src/
│   ├── helper.py
│   └── prompt.py
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── store_index.py           # Creates vector database
├── app.py                   # Flask application
├── requirements.txt
├── setup.py
├── README.md
└── .env
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | Flask |
| LLM | Qwen |
| AI Framework | LangChain |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | Qdrant Cloud |
| PDF Processing | PyPDF |
| Deployment | Render |
| Environment | Python Virtual Environment |

---

# 📊 Project Highlights

- 📄 Processed multiple medical reference documents
- 🧩 Indexed **21,793+ semantic text chunks**
- 🧠 Generated **384-dimensional vector embeddings**
- 🔍 Implemented semantic similarity search using Qdrant Cloud
- ⚡ Built an end-to-end Retrieval-Augmented Generation pipeline
- ☁️ Cloud-ready architecture for deployment

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/R-snehal/MedicBot.git

cd MedicBot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv MedicBot

MedicBot\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv MedicBot

source MedicBot/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
QDRANT_URL=YOUR_QDRANT_URL

QDRANT_API_KEY=YOUR_QDRANT_API_KEY

HUGGINGFACEHUB_API_TOKEN=YOUR_HUGGINGFACE_API_TOKEN
```

---

# 📚 Prepare the Knowledge Base

Place your medical PDF documents inside the **Data/** directory.

Run:

```bash
python store_index.py
```

This script will:

- Load medical PDFs
- Split documents into semantic chunks
- Generate embeddings
- Create the Qdrant collection
- Upload embeddings to Qdrant Cloud

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:8080
```

---

# 💬 Example Questions

```
What is Acne?

Symptoms of Anaemia

Treatment of Asthma

What is the Amygdala?

What causes Diabetes?

Symptoms of Tuberculosis

How is Hypertension treated?
```

---

# 🔍 How MedicBot Works

### Step 1

Medical PDF documents are loaded.

⬇️

### Step 2

Documents are split into semantic chunks.

⬇️

### Step 3

Sentence Transformer converts every chunk into vector embeddings.

⬇️

### Step 4

Embeddings are stored inside Qdrant Cloud.

⬇️

### Step 5

When a user asks a question:

- Relevant document chunks are retrieved.
- Retrieved context is sent to the Qwen LLM.
- The model generates a context-aware answer.

---

# 📈 Future Enhancements

- 🎤 Voice-enabled chatbot
- 🌍 Multi-language support
- 📜 Conversation history
- 📚 Source citation for every answer
- 🖼️ Medical image understanding
- 👨‍⚕️ Doctor appointment integration
- 🏥 Hospital recommendation system
- 📱 Mobile-friendly interface

---

# 📸 Screenshots

Add screenshots here after deployment.

### Home Page

<img width="900" alt="Home Page" src="images/home.png">

### Chat Interface

<img width="900" alt="Chat Interface" src="images/chat.png">

### Example Conversation

<img width="900" alt="Conversation" src="images/conversation.png">

---

# 📄 Dataset

This project uses publicly available medical reference documents for educational purposes.

Due to GitHub's file size limitations, the dataset is **not included** in this repository.

Users can place their own medical PDF files inside the **Data/** directory before running the indexing script.

---

# ⚠️ Disclaimer

MedicBot is intended for educational and informational purposes only.

It is **not** a substitute for professional medical advice, diagnosis, or treatment.

Always consult a licensed healthcare professional before making medical decisions.

---

# 👩‍💻 Author

**Rishika Snehal**

B.Tech Computer Science Engineering

AI • Machine Learning

GitHub: https://github.com/R-snehal


---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.