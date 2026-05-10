<div align="center">
  <img src="https://img.icons8.com/fluency/256/artificial-intelligence.png" width="120" alt="SkillForge AI Logo">

  <h1>🧠 SkillForge — Skill Gap Analyzer</h1>

  <p><strong>Next-Generation AI Career & Skill Progression Ecosystem</strong></p>

  <p>
    <a href="https://nextjs.org/"><img src="https://img.shields.io/badge/Frontend-Next.js-black?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" /></a>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
    <a href="https://groq.com/"><img src="https://img.shields.io/badge/AI_Engine-Groq_Llama_3.3-f55036?style=for-the-badge" alt="Groq AI" /></a>
    <a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/Auth-Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=white" alt="Firebase" /></a>
    <a href="https://www.netlify.com/"><img src="https://img.shields.io/badge/Deployed_on-Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white" alt="Netlify" /></a>
  </p>

  <br/>

  > **Bridge the gap between where you are and where you want to be — powered by AI.**

</div>

---

## 📖 About SkillForge

**SkillForge** is a robust, enterprise-grade AI-powered web application designed to bridge the gap between a developer's current skill set and their dream job requirements. It eliminates the guesswork in career progression by providing a highly personalized, automated, and dynamic learning roadmap.

Powered by the lightning-fast **Groq Llama 3.3 AI Model** and engineered with a modern **Next.js frontend**, SkillForge guarantees real-time, highly accurate curriculum generation while delivering a premium user experience with fluid UI animations.

Whether you're a junior developer aiming for a senior role, a frontend engineer pivoting to full-stack, or a software engineer targeting ML engineering — SkillForge crafts a tailored learning journey **just for you**.

---

## 🌟 Key Features & Ecosystem

### 🤖 1. AI-Powered Gap Analysis
- **Intelligent Profiling:** Cross-references your current skills with the latest industry demands for your exact target role.
- **Precision Mapping:** Identifies distinct knowledge gaps, missing tech stacks, and necessary theoretical fundamentals.
- **Contextual Understanding:** Adapts the difficulty and scope of the roadmap based on your existing seniority level.
- **Sub-second Generation:** Groq's ultra-fast inference ensures roadmaps are generated in real-time with zero waiting.

### 🗺️ 2. Dynamic Interactive Roadmaps
- **Step-by-Step Curriculum:** Breaks down monumental learning tasks into digestible, daily or weekly modules.
- **Visual Progress Tracking:** Interactive timeline components that visually reflect your upskilling journey.
- **Adaptive Adjustments:** Allows users to mark nodes as complete, dynamically recalculating remaining effort.
- **Priority Ordering:** Topics are ranked by importance and dependency, so you always learn in the right sequence.

### 📹 3. Automated Resource Generation
- **YouTube API Integration:** Automatically fetches the highest-rated, most relevant tutorials and crash courses for every generated topic.
- **Curated Filtering:** Avoids outdated content by prioritizing modern, well-reviewed educational materials.
- **In-App Viewing Engine:** Seamless video playback directly within the learning dashboard — no tab-switching needed.

### 📊 4. User Dashboard & Analytics
- **Macro Analytics:** Real-time dashboards monitoring completion percentages and remaining skill targets.
- **Persistent State:** Cloud-synced state management allows users to pick up their learning journey exactly where they left off.
- **Progress Visualization:** Charts and indicators to keep you motivated throughout the journey.

### 🔐 5. Secure Authentication
- **Google OAuth & GitHub OAuth** via Firebase — fast, frictionless, and secure.
- No raw passwords. No unnecessary data collection.
- Session persistence across devices.

---

## 🛠️ Technical Architecture & Stack

### Frontend Application

| Technology | Purpose |
|---|---|
| **Next.js (React)** | Server-side rendering, routing, and SEO optimization |
| **Tailwind CSS** | Utility-first responsive styling |
| **React Context + Hooks** | Lightweight, optimized global state management |

### Backend Infrastructure

| Technology | Purpose |
|---|---|
| **FastAPI (Python)** | Asynchronous, high-performance REST API endpoints |
| **Groq API (Llama-3.3-70b)** | Sub-second AI roadmap and curriculum generation |
| **YouTube Data API v3** | Dynamic educational video resource fetching |
| **Firebase Auth** | Secure Google & GitHub OAuth 2.0 authentication |
| **Firebase Firestore** | Real-time NoSQL cloud database for user data |

### Deployment

| Service | Role |
|---|---|
| **Netlify** | Frontend deployment with global CDN |
| **Render** | Backend API hosting |
| **Firebase** | Auth + Database |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER BROWSER                         │
│              Next.js Frontend (Netlify)                 │
│            Tailwind CSS + Animated UI                   │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTPS REST API
                        ▼
┌─────────────────────────────────────────────────────────┐
│            FastAPI Backend (Render)                      │
│  ┌──────────────────┐     ┌──────────────────────────┐  │
│  │  Groq AI Engine  │     │  YouTube Data API v3     │  │
│  │  Llama-3.3-70b   │     │  (Resource Aggregator)   │  │
│  └──────────────────┘     └──────────────────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  Firebase Platform                      │
│         Firebase Auth  │  Firestore Database            │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
skill-gap-analyzer/
│
├── frontend/                      # Next.js application
│   ├── src/
│   │   ├── app/                   # App router pages
│   │   │   ├── layout.tsx         # Root layout
│   │   │   ├── page.tsx           # Landing page
│   │   │   ├── globals.css        # Global styles
│   │   │   ├── login/             # Login page
│   │   │   ├── skill-input/       # Skill input page
│   │   │   ├── dashboard/         # Dashboard page
│   │   │   └── roadmap/           # Roadmap page
│   │   ├── components/            # Reusable UI components
│   │   │   ├── AnalysisResults.tsx
│   │   │   ├── AuthGuard.tsx
│   │   │   ├── LearningTimeline.tsx
│   │   │   ├── ProgressChart.tsx
│   │   │   ├── RoadmapSteps.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── SkillForm.tsx
│   │   │   ├── SkillGapCards.tsx
│   │   │   └── YoutubeResourceList.tsx
│   │   ├── context/               # React Context providers
│   │   │   └── AuthContext.tsx
│   │   ├── data/                  # Mock/fallback data
│   │   │   └── mockData.ts
│   │   └── lib/                   # Firebase config & utilities
│   │       └── firebase.ts
│   ├── public/                    # Static assets
│   ├── netlify.toml               # Netlify deployment config
│   ├── next.config.ts             # Next.js configuration
│   ├── package.json
│   ├── tsconfig.json
│   ├── postcss.config.mjs
│   ├── eslint.config.mjs
│   └── .env.example               # Environment template
│
├── backend/                       # FastAPI application
│   ├── main.py                    # Entry point & route registration
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py             # Pydantic request/response models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analysis.py            # AI gap analysis endpoints
│   │   ├── dashboard.py           # Dashboard data endpoints
│   │   ├── jobs.py                # Job roles endpoint
│   │   ├── resources.py           # YouTube resource endpoints
│   │   └── roadmap.py             # Roadmap generation endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_service.py          # Groq AI integration
│   │   ├── skill_service.py       # Skill processing logic
│   │   └── youtube_service.py     # YouTube API integration
│   ├── data/
│   │   └── jobs.json              # Job roles reference data
│   ├── requirements.txt           # Python dependencies
│   └── .env.example               # Environment template
│
├── .gitignore
└── README.md
```

---

## 🔒 Security Posture

- **🔐 Encrypted Transmission:** All client-server communication is secured via HTTPS with authenticated API routes.
- **🛡️ OAuth 2.0 Standards:** Strict implementation of GitHub and Google login via Firebase — no raw passwords ever touch the database.
- **🔒 Data Silos:** Firestore Security Rules ensure users can only query and mutate their own roadmap data.
- **✅ No Sensitive Storage:** No credit cards, no passwords, no PII beyond what OAuth providers supply.

---

## ⚙️ Installation & Local Setup

### Prerequisites

| Requirement | Version |
|---|---|
| Node.js | v18.0.0 or higher |
| Python | v3.9+ |
| npm / yarn | Latest stable |
| Groq API Key | [Get it here](https://console.groq.com) |
| YouTube Data API Key | [Google Cloud Console](https://console.cloud.google.com) |
| Firebase Project | [Firebase Console](https://console.firebase.google.com) |

---

### 🚀 Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/skill-gap-analyzer.git
cd skill-gap-analyzer
```

---

#### 2. Backend Setup (FastAPI)

```bash
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file from the template:

```bash
cp .env.example .env
# Then fill in your actual API keys
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

The backend will be live at: `https://skill-gap-analyzer-hp2q.onrender.com`
API docs available at: `https://skill-gap-analyzer-hp2q.onrender.com/docs`

---

#### 3. Frontend Setup (Next.js)

```bash
cd ../frontend

# Install dependencies
npm install
```

Create a `.env.local` file from the template:

```bash
cp .env.example .env.local
# Then fill in your Firebase config and backend URL
```

Start the development server:

```bash
npm run dev
```

The frontend will be live at: `http://localhost:3000`

---

#### 4. Firebase Configuration

1. Go to [Firebase Console](https://console.firebase.google.com) and create a new project.
2. Enable **Authentication** → Turn on **Google** and **GitHub** providers.
3. Create a **Firestore Database** in production mode.
4. Add the following Firestore Security Rules:

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

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/job-roles` | Get available job roles |
| `POST` | `/analyze-skills` | Submit skills + target role → get AI analysis |
| `POST` | `/roadmap` | Generate a learning roadmap |
| `GET` | `/youtube-resources` | Fetch YouTube resources for a topic |
| `GET` | `/dashboard` | Get dashboard analytics |

### Example Request — Analyze Skills

```json
POST /analyze-skills
{
  "current_skills": ["HTML", "CSS", "JavaScript", "React"],
  "target_role": "Full Stack Engineer",
  "experience_level": "junior"
}
```

### Example Response

```json
{
  "gap_analysis": "You are missing backend, database, and DevOps fundamentals...",
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

## 🚀 Deployment

### Frontend (Netlify)

1. Connect your GitHub repository to [Netlify](https://app.netlify.com).
2. Set the **Base directory** to `frontend`.
3. Build command: `npm run build`
4. Publish directory: `.next`
5. Install the **@netlify/plugin-nextjs** plugin (already configured in `netlify.toml`).
6. Set all `NEXT_PUBLIC_*` environment variables in the Netlify dashboard.

### Backend (Render)

1. Connect your GitHub repository to [Render](https://render.com).
2. Create a new **Web Service**.
3. Set the **Root directory** to `backend`.
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Set `GROQ_API_KEY` and `YOUTUBE_API_KEY` as environment variables.

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get involved:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "feat: add your feature description"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature idea? [Open an issue](https://github.com/yourusername/skill-gap-analyzer/issues) with:

- A clear, descriptive title
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Screenshots if applicable

---

---

## 🙏 Acknowledgements

- [Groq](https://groq.com/) — for blazing-fast LLM inference
- [Meta AI](https://ai.meta.com/) — for the Llama 3.3 model
- [Netlify](https://www.netlify.com/) — for seamless frontend deployment
- [Firebase](https://firebase.google.com/) — for auth and database infrastructure
- [YouTube Data API](https://developers.google.com/youtube/v3) — for educational resource aggregation

---

<div align="center">

  **Built with ❤️ to help developers level up their careers**

  <br/>

  **⭐ this repo** if SkillForge helped you on your learning journey!

</div>
