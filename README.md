<div align="center">
  <img src="https://img.icons8.com/fluency/256/artificial-intelligence.png" width="120" alt="SkillForge AI Logo">

  <h1>SkillForge — Skill Gap Analyzer</h1>

  <p><strong>AI-powered skill gap analysis and career roadmap generator</strong></p>

  <p>
    <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Frontend-Next.js-black?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" /></a>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
    <a href="https://groq.com/"><img src="https://img.shields.io/badge/AI_Engine-Groq_Llama_3.3-f55036?style=for-the-badge" alt="Groq AI" /></a>
    <a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/Auth-Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=white" alt="Firebase" /></a>
    <a href="https://www.netlify.com/"><img src="https://img.shields.io/badge/Deployed_on-Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white" alt="Netlify" /></a>
  </p>

  <p>
    Bridge the gap between where you are and where you want to be.
  </p>
</div>

---

## About the project

**SkillForge** is a full-stack web application that compares a user’s current skills with the requirements of a target role and generates a personalized learning roadmap.

It helps users answer three practical questions:

* What skills am I missing?
* What should I learn first?
* Which resources should I use?

The project combines a **Next.js frontend**, a **FastAPI backend**, **Groq Llama 3.3** for roadmap generation, **YouTube resource suggestions**, and **Firebase authentication** for a smooth user experience.

---

## Features

### Skill gap analysis

* Compare current skills with target job requirements
* Identify missing technical skills and fundamentals
* Adapt recommendations based on experience level
* Generate results quickly using Groq

### Personalized roadmap

* Turn skill gaps into a step-by-step learning plan
* Organize topics by priority and dependency
* Show progress through a clear roadmap view
* Support completion tracking for learning flow

### Learning resources

* Fetch relevant YouTube resources for each topic
* Surface tutorials and crash courses alongside the roadmap
* Keep resources tied to the current learning stage

### Dashboard

* View analysis results and roadmap progress in one place
* Track completion status and remaining goals
* Resume learning from where you left off

### Authentication

* Google and GitHub sign-in via Firebase
* No password handling in the app itself
* Session persistence across devices

---

## Tech stack

### Frontend

* **Next.js** — app routing and UI
* **Tailwind CSS** — styling
* **React Context / Hooks** — state management

### Backend

* **FastAPI** — REST API
* **Python** — backend logic
* **Groq API** — AI roadmap generation
* **YouTube Data API v3** — learning resource lookup
* **Firebase Auth** — authentication
* **Firestore** — user data storage

### Deployment

* **Netlify** — frontend hosting
* **Render** — backend hosting
* **Firebase** — auth and database

---

## Architecture

```text
User Browser
   ↓
Next.js Frontend (Netlify)
   ↓ HTTPS REST API
FastAPI Backend (Render)
   ├── Groq AI Engine
   ├── YouTube Data API
   └── Skill processing logic
   ↓
Firebase
   ├── Authentication
   └── Firestore Database
```

---

## Project structure

```text
skill-gap-analyzer/
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── context/
│   │   ├── data/
│   │   └── lib/
│   ├── public/
│   ├── netlify.toml
│   └── .env.example
│
├── backend/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── data/
│   ├── requirements.txt
│   └── .env.example
│
└── README.md
```

---

## Getting started

### Prerequisites

* Node.js 18+
* Python 3.9+
* npm or yarn
* Groq API key
* YouTube Data API key
* Firebase project

### 1) Clone the repository

```bash
git clone https://github.com/yourusername/skill-gap-analyzer.git
cd skill-gap-analyzer
```

### 2) Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Run the backend:

```bash
uvicorn main:app --reload --port 8000
```

### 3) Frontend setup

```bash
cd ../frontend
npm install
cp .env.example .env.local
npm run dev
```

The frontend runs at:

```bash
http://localhost:3000
```

---

## Firebase setup

1. Create a Firebase project.
2. Enable **Authentication** and turn on **Google** and **GitHub** providers.
3. Create a **Firestore Database**.
4. Add security rules so users can only access their own data.

Example rule:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/{document=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

---

## API endpoints

| Method | Endpoint             | Description                                  |
| ------ | -------------------- | -------------------------------------------- |
| GET    | `/job-roles`         | Get available job roles                      |
| POST   | `/analyze-skills`    | Analyze current skills against a target role |
| POST   | `/roadmap`           | Generate a learning roadmap                  |
| GET    | `/youtube-resources` | Fetch resources for a topic                  |
| GET    | `/dashboard`         | Get dashboard analytics                      |

### Example request

```json
{
  "current_skills": ["HTML", "CSS", "JavaScript", "React"],
  "target_role": "Full Stack Engineer",
  "experience_level": "junior"
}
```

### Example response

```json
{
  "gap_analysis": "You are missing backend, database, and deployment fundamentals.",
  "roadmap": [
    {
      "week": 1,
      "topic": "Node.js & Express",
      "priority": "high",
      "estimated_hours": 10
    },
    {
      "week": 2,
      "topic": "PostgreSQL & SQL Fundamentals",
      "priority": "high",
      "estimated_hours": 8
    }
  ],
  "total_estimated_weeks": 12
}
```

---

## Deployment

### Frontend on Netlify

* Connect the repo to Netlify
* Set the base directory to `frontend`
* Build command: `npm run build`
* Publish directory: `.next`

### Backend on Render

* Connect the repo to Render
* Set the root directory to `backend`
* Build command: `pip install -r requirements.txt`
* Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Contributing

1. Fork the repository
2. Create a branch
3. Make your changes
4. Commit with a clear message
5. Open a pull request

Use conventional commit messages where possible.

---

## Acknowledgements

* Groq — AI inference
* Meta AI — Llama model family
* Netlify — frontend deployment
* Firebase — authentication and database
* YouTube Data API — learning resources

---

<div align="center">

**Built to help developers and students understand their skill gaps and plan their next steps**

</div>
