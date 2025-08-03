## 🃏 Poker Trivia API — Backend

This is the FastAPI-based backend for the Poker Trivia App. It serves structured trivia questions about poker, including strategy, math, and terminology.

---

### 🌐 Live API

Hosted on [Render](https://render.com):

```
https://trivia-poker-backend.onrender.com
```

---

### 🚀 Features

* 🎲 Random poker trivia questions
* 🔍 Search and filter by keyword or tag
* 📊 Multiple choice with explanations
* 📁 JSON-based question database

---

### 📁 Project Structure

```
poker-trivia-backend/
├── main.py               ← FastAPI app
├── questions.json        ← Trivia database
├── dedupe_questions.py  ← Utility to remove duplicate entries
├── requirements.txt
└── README.md
```

---

### 📦 Installation

```bash
git clone https://github.com/yourusername/poker-trivia-backend.git
cd poker-trivia-backend
pip install -r requirements.txt
```

---

### 🧪 Endpoints

* `/trivia/random`
* `/trivia/search?q=bluff`
* (More endpoints coming soon)

---

### 🧠 Trivia Format (JSON)

```json
{
  "id": 1,
  "question": "What is the best possible hand in Texas Hold'em?",
  "options": ["Flush", "Full House", "Four of a Kind", "Royal Flush"],
  "correct_answer": "Royal Flush",
  "explanation": "A Royal Flush is the highest possible hand, consisting of A-K-Q-J-10 of the same suit.",
  "tags": ["hand rankings"]
}
```

---