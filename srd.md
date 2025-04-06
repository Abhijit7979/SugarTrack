

# ✅ System Design

**SugarTrack** is a gamified website that promotes productive online research through time tracking, daily learning summaries, AI quizzes, coin rewards, and a reward redemption marketplace. It encourages learning by rewarding users with “Sugar Coins” for time spent on productive websites, daily summaries, and quizzes — coins can be redeemed for real-world perks.

---

# 🏗 Architecture Pattern

- **Frontend**: website UI + optional Flask-based dashboard
- **Backend**: Serverless architecture using Firebase or Supabase
- **AI Services**: LLM-based summary parsing, quiz generation, and chatbot assistant
- **Browser Integration**: Real-time site tracking and assistant via Chrome APIs

---

# 🧠 State Management

- **Local**: website popup state managed via JavaScript/React state
- **Global/App-wide**: Firebase or Supabase real-time data (user profiles, coins, summaries)
- **Session**: Tracked per user using secure auth tokens
- **Persistent**: Coin balances, goal data, summary logs, and redemption history saved per user

---

# 🔁 Data Flow

- **Tracking**: User visits high-value site → timer begins
- **Goal & Coin Engine**: Time tracked → matches goal → coins awarded or penalties applied
- **Daily Summary**: User submits summary → LLM parses → quiz generated
- **Quiz**: User answers quiz → correct answers → earn coins
- **Redemption**: User opens Marketplace → selects item → confirms → coins deducted, reward marked

---

# 🧱 Technical Stack

- **Frontend**: Flask
- **Backend**: Firebase 
- **AI Tools**: Groq (or similar) for LLM quiz & chatbot
- **Authentication**: Email/password via Firebase Auth
- **Hosting**: Vercel (optional for dashboard)

---

# 🔐 Authentication Process

- **User Signup/Login** via email/password
- **Session Management** via secure tokens (Firebase Auth)
- **Permissions** enforced at DB and UI level (user owns their data)
- **Access Control**: Only user can view/edit their progress, history, and redemptions

---

# 🌐 Route Design (for Dashboard)

| Route          | Description                              |
| -------------- | ---------------------------------------- |
| `/dashboard`   | Main view: coin count, tracking stats    |
| `/summary`     | Daily summary input and quiz module      |
| `/marketplace` | Browse and redeem rewards                |
| `/profile`     | Update goal, view timeline, coin history |
| `/leaderboard` | Global, weekly, monthly rankings         |
| `/chat`        | Agentic AI chatbot interface             |

---

# 🔌 API Design

| Endpoint             | Method | Description                       |
| -------------------- | ------ | --------------------------------- |
| `/api/track/start`   | POST   | Start tracking a research session |
| `/api/track/stop`    | POST   | Stop tracking and store session   |
| `/api/summary`       | POST   | Submit daily summary              |
| `/api/quiz/submit`   | POST   | Submit quiz answers               |
| `/api/coins/log`     | GET    | Retrieve coin transactions        |
| `/api/reward/redeem` | POST   | Redeem a reward item              |
| `/api/leaderboard`   | GET    | Retrieve ranking data             |

---

# 📊 Database Design (Entities, Fields, and Rules)

---

### **1. User**

| Field            | Type      | Description                  |
| ---------------- | --------- | ---------------------------- |
| userId           | UUID      | Unique ID                    |
| username         | String    | Display name                 |
| email            | String    | Login credential             |
| dailyGoalMinutes | Integer   | User-set daily research goal |
| coinBalance      | Integer   | Real-time Sugar Coin count   |
| streakCount      | Integer   | Days of consistent research  |
| createdAt        | Timestamp | Account creation date        |

**Validations**

- Email must be unique and valid
- dailyGoalMinutes ≥ 10 and ≤ 600
- coinBalance ≥ 0

**Actions**

- Update goal
- View progress
- View coin history
- Earn/lose coins
- Submit summary

---

### **2. ResearchSession**

| Field           | Type      | Description             |
| --------------- | --------- | ----------------------- |
| sessionId       | UUID      | Unique ID               |
| userId          | UUID      | Foreign key             |
| url             | String    | Tracked site URL        |
| startTime       | Timestamp | Start of session        |
| endTime         | Timestamp | End of session          |
| durationMinutes | Integer   | Computed session length |

**Validations**

- Duration ≥ 1 minute
- Only count high-value URLs

**Actions**

- Start/stop timer
- Generate earned coins
- Contribute to daily goal

---

### **3. SugarCoinTransaction**

| Field         | Type      | Description                               |
| ------------- | --------- | ----------------------------------------- |
| transactionId | UUID      | Unique ID                                 |
| userId        | UUID      | FK                                        |
| type          | Enum      | earn, penalty, redeem                     |
| amount        | Integer   | Positive/negative integer                 |
| source        | String    | e.g., "Quiz", "Redemption", "Login Bonus" |
| timestamp     | Timestamp | When transaction occurred                 |

**Validations**

- Coin balance must not go negative
- amount ≠ 0

---

### **4. DailySummary**

| Field         | Type    | Description                  |
| ------------- | ------- | ---------------------------- |
| summaryId     | UUID    | Unique ID                    |
| userId        | UUID    | FK                           |
| content       | Text    | User-entered content         |
| date          | Date    | Daily summary date           |
| quizGenerated | Boolean | True if quiz created from it |

**Validations**

- One summary per user per day

**Actions**

- Submit summary
- Trigger quiz generation

---

### **5. Quiz**

| Field          | Type    | Description                    |
| -------------- | ------- | ------------------------------ |
| quizId         | UUID    | Unique ID                      |
| userId         | UUID    | FK                             |
| summaryId      | UUID    | FK                             |
| questions      | Array   | Array of MCQs                  |
| correctAnswers | Integer | Score achieved                 |
| totalQuestions | Integer | Always 3 to 5                  |
| coinsEarned    | Integer | Coins based on correct answers |

---

### **6. Notification**

| Field          | Type      | Description                    |
| -------------- | --------- | ------------------------------ |
| notificationId | UUID      | Unique ID                      |
| userId         | UUID      | FK                             |
| type           | Enum      | motivation, reminder, fun-fact |
| content        | String    | Message body                   |
| dateShown      | Timestamp | Last shown timestamp           |

**Note**: Sticky and playful notifications triggered by streaks, inactivity, etc.

---

### **7. ChatbotQuery**

| Field      | Type      | Description                |
| ---------- | --------- | -------------------------- |
| queryId    | UUID      | Unique ID                  |
| userId     | UUID      | FK                         |
| question   | Text      | User input                 |
| response   | Text      | AI-generated answer        |
| urlContext | String    | Page context if applicable |
| timestamp  | Timestamp | Date/time of interaction   |

---

### **8. LeaderboardEntry** (virtual/aggregated)

| Field      | Type    | Description                    |
| ---------- | ------- | ------------------------------ |
| userId     | UUID    | FK                             |
| username   | String  | Display name                   |
| totalCoins | Integer | Sum of earned coins            |
| rankGlobal | Integer | Position in global leaderboard |
| rankWeekly | Integer | Position this week             |

---

### **9. RewardItem**

| Field    | Type    | Description                    |
| -------- | ------- | ------------------------------ |
| rewardId | UUID    | Unique ID                      |
| name     | String  | Display name                   |
| coinCost | Integer | Cost to redeem                 |
| stock    | Integer | Available inventory            |
| category | Enum    | e.g., swag, ticket, mentorship |

---

### **10. Redemption**

| Field        | Type      | Description                 |
| ------------ | --------- | --------------------------- |
| redemptionId | UUID      | Unique ID                   |
| userId       | UUID      | FK                          |
| rewardId     | UUID      | FK                          |
| redeemedAt   | Timestamp | Date of redemption          |
| status       | Enum      | pending, confirmed, shipped |

---

# 📜 Business Logic Rules

| Rule ID | Description                                                            |
| ------- | ---------------------------------------------------------------------- |
| R1      | +1 Sugar Coin every 30 minutes of active research on approved websites |
| R2      | +1 Coin for daily login                                                |
| R3      | -3 Coins if no research activity detected that day                     |
| R4      | -3 Coins if user completes <30% of daily goal                          |
| R5      | Coin balance must be ≥ reward cost to redeem item                      |
| R6      | User can submit 1 summary per day; triggers quiz                       |
| R7      | Correct quiz answers = bonus coins (e.g., +1 per correct)              |
| R8      | Leaderboard ranks by total coin count, updated daily                   |
| R9      | Notifications trigger based on streaks, inactivity, or events          |
| R10     | Chatbot uses active tab context if query initiated from tracked site   |

---

# 🔐 Permissions Model

| Permission         | Description                      |
| ------------------ | -------------------------------- |
| `user:read`        | View profile, goal, coin balance |
| `user:update`      | Update goal, username            |
| `research:create`  | Start a research session         |
| `summary:create`   | Submit a daily summary           |
| `quiz:answer`      | Submit and get results from quiz |
| `coins:view`       | View coin logs                   |
| `reward:redeem`    | Redeem rewards                   |
| `chat:query`       | Use chatbot                      |
| `leaderboard:view` | View rankings                    |

---

# ✅ Summary

**System Name**: SugarTrack  
**Platform**: website + Optional Web Dashboard  
**Core Modules**:

- Time Tracker
- Daily Summary + AI Quiz
- Sugar Coin Economy
- AI Chatbot
- Leaderboard
- Reward Marketplace

This document outlines all major entities, relationships, flows, and rules for the MVP version of SugarTrack. Let me know if you’d like a **UML class diagram**, **ERD**, or **workflow diagrams** to complement this SRS.

Would you like a downloadable version (PDF/Markdown/Word), or should we move on to refining one specific module (e.g., AI quiz logic, tracking algorithm)?
