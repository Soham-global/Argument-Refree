# ⚖️ Argument Referee

An AI-powered argument referee that listens to both sides, gives a neutral verdict, identifies logical fallacies, and suggests a compromise — built with FastAPI, LangChain, and Groq.

---

## 🧠 What It Does

Paste two sides of any argument — a couple fight, a roommate dispute, an online debate — and the AI gives you:

- 🏆 A verdict on who has the stronger argument
- 🔵 Analysis of Person 1's strong and weak points
- 🔴 Analysis of Person 2's strong and weak points
- 🤝 A fair compromise both sides can agree on

---

## 🗂️ Project Structure

```
argementRefree/
│
├── .env                   # API keys (never commit this)
├── pyproject.toml         # Project dependencies
├── template.py            # Auto-generates project structure
│
├── backend/
│   ├── __init__.py        # Makes backend a Python package
│   ├── main.py            # FastAPI app and routes
│   ├── config.py          # Model settings and env vars
│   ├── prompt.py          # LangChain PromptTemplate
│   └── chain.py           # LangChain chain (LLM + prompt + parser)
│
└── frontend/
    ├── index.html         # UI layout
    ├── style.css          # Styling
    └── script.js          # API calls and DOM logic
```

---

## ⚙️ Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Frontend  | HTML, CSS, Vanilla JS               |
| Backend   | Python, FastAPI                     |
| AI Chain  | LangChain Core                      |
| LLM       | Groq API (llama-3.3-70b-versatile)  |
| Server    | Uvicorn                             |
| packaging | uv                                  |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/argementRefree.git
cd argementRefree
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up your `.env` file

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Run the backend

```bash
uvicorn backend.main:app --reload
```

Backend runs at `http://127.0.0.1:8000`

### 5. Run the frontend

Open `frontend/index.html` using **Live Server** in VS Code (click **Go Live** in the bottom right), or just double-click the file in your file explorer.

Frontend runs at `http://127.0.0.1:5500/frontend/index.html`

---

## 🔌 API Endpoints

### `GET /`
Health check

**Response:**
```json
{ "message": "Argument Referee API is running 🏆" }
```

### `POST /verdict`
Submit both sides and get a verdict

**Request body:**
```json
{
  "person1": "I think we should get a dog.",
  "person2": "We don't have time or space for a dog."
}
```

**Response:**
```json
{
  "verdict": "1. 🏆 VERDICT\n Person 2 has the stronger argument..."
}
```

---

## 📦 Dependencies

```
fastapi
uvicorn
langchain
langchain-groq
langchain-core
python-dotenv
pydantic
```

---

## 🛡️ Notes

- Never commit your `.env` file — it's already in `.gitignore`
- The Groq free tier is generous enough to run this project without any cost
- CORS is set to `*` for local development — restrict it before deploying to production

---

## 🙌 Built By

Made with ❤️ by Sahil