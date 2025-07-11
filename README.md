# Mini ChatGPT++
A hybrid rule-based + NLP chatbot for DSA and CS queries.

Mini ChatGPT++ is a hybrid chatbot built with **C++**, **Python (Flask)**, and **React** that answers 100+ commonly asked **DSA** and **DBMS** questions. It uses **Trie-based keyword matching**, **semantic similarity using sentence embeddings**, and **Levenshtein distance** for typo tolerance.

## Features

-  100+ curated questions & answers from DSA and DBMS
-  Semantic similarity using `sentence-transformers`
-  Trie + fuzzy matching (C++ backend)
-  90%+ accuracy in internal testing
-  Modular Q&A corpus (easily add OS, CN, etc.)
-  React-based chatbot interface
-  Plug-and-play integration ready for GitHub


## Tech Stack

| Layer      | Technologies                            |
|------------|-----------------------------------------|
| Frontend   | React.js, Tailwind CSS (optional)       |
| Backend    | Python (Flask), CORS, Sentence Transformers |
| Core Logic | C++ (Trie, Fuzzy Match, CLI tools)       |
| Model      | `all-MiniLM-L6-v2` via `sentence-transformers` |



##  How to Run Locally

###  Backend (Python + Flask)
```bash
cd MiniChatGPTpp
pip install -r requirements.txt
python run.py
```
Runs on: `http://localhost:5000`

###  Frontend (React)
```bash
cd frontend
npm install
npm start
```
Runs on: `http://localhost:3000`


##  How It Works

1. User enters a query on the chat interface
2. Flask backend:
   - Computes semantic similarity between query & corpus using sentence embeddings
   - Uses Trie matching or Levenshtein to improve precision
3. Returns the best matching predefined answer


## Sample Questions
- What is binary search?
- Explain quick sort
- What are ACID properties?
- Difference between stack and queue
- What is normalization in DBMS?

## Future Enhancements
-  Voice input (Web Speech API)
-  Chat history + context memory
-  Add topics: OS, CN, System Design
-  Corpus editing via frontend


##  Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.
