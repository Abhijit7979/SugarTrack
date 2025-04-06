 UI Design for SugarTrack

This document outlines the **User Interface Design Document (UIDD)** for **SugarTrack**
---

## 🎨 Layout Structure

### **Overall Layout**

- **Left-Hand Sidebar (Navigation):**
  - Collapsible panel hosting key navigation items.
- **Main Content Area:**
  - Dynamic zone updating based on navigation selection.

### **Left-Hand Sidebar**

- **Navigation Items:**
  - **Dashboard**
  - **Daily Summary**
  - **Quiz**
  - **Marketplace**
  - **Leaderboard**
  - **Profile**
- **Bottom Section:**
  - Profile Icon → triggers dropdown for logout.
  - Theme toggle (dark/light mode).

### **Main Content Area**

- Displays:
  - Coin count and research progress
  - Daily summaries and quiz interactions
  - Marketplace browsing and redemptions
  - Leaderboard rankings
  - AI Chatbot panel (if open)

---

## 🧩 Core Components

### **Collapsible Sidebar Navigation**

- Icons + labels (modern flat icons)
- Hover/active/focus states for accessibility
- Auto-collapse for compact mode

### **Main Content Screens**

- **Dashboard View:**
  - Coin total, goal progress, streak indicator
  - Quick action to start/stop tracking
- **Summary Input:**
  - Rich text input with emoji and markdown
  - “Submit” triggers AI quiz generation
- **Quiz Module:**
  - MCQs with immediate feedback
  - Score display and coin reward message
- **Marketplace:**
  - Grid view of redeemable rewards
  - Coin cost tags + “Redeem” buttons
- **Leaderboard:**
  - Tab switcher for Global, Weekly, Monthly
- **Chatbot (Slide-Out Panel):**
  - Prompt input + response thread
  - Contextual awareness of tracked tabs

---

## 🎛 Interaction Patterns

### **Navigation Behavior**

- Sidebar toggles between full/compact view
- Click = updates content area instantly
- Profile Icon = opens logout/settings dropdown

### **Theme Toggle**

- Persistent toggle across all screens
- Animation when switching
- Saved preference per user

### **Tracking & Rewards**

- Timer starts/stops with button toggle
- Tracks current active domain (visible in UI)
- Coin reward animations for:
  - Time-based research (+1 coin)
  - Daily login (+1)
  - Quiz accuracy (+X coins)
  - Redemption (-X coins)

### **Quiz Interaction**

- Answers scored instantly with reward popup
- Disabled re-attempts once submitted
- Tooltip on each question for hints

### **Redemption Flow**

- Click redeem → modal confirmation
- On confirm: coins deducted, item marked “pending”
- Success toast + updated inventory

---

## 🌗 Visual Design & Theme

### **Dark Mode (Default)**

- **Background:** #121212 to #1C1C1C gradients
- **Accent Color:** #FFD600 (vibrant yellow)
- **Text Colors:** #FFFFFF, #CCCCCC for contrast
- **Buttons & Highlights:** Yellow with hover darkening

### **Light Mode (Accessible)**

- **Background:** #F9F9F9 with subtle grey panels
- **Text:** #333333
- **Accent Yellow:** Retained for brand continuity

### **Components Styling**

- Cards for summaries, rewards
- Hover shadows and borders
- Smooth transitions between screen states

---

## 🔤 Typography

- **Font:** Inter or Roboto (clean sans-serif)
- **Weights:** Bold for headers/buttons, regular for body
- **Size Scale:**
  - Headline: 24–28px
  - Section Titles: 18–22px
  - Body Text: 14–16px
  - Button Text: 14px uppercase

---

## ♿ Accessibility

### **Contrast & Color**

- All text passes WCAG AA minimum contrast
- Dark mode uses yellow/white; light mode uses black/yellow
- Minimal red/green combinations (colorblind friendly)

### **Keyboard Navigation**

- Sidebar, modals, toggles, and quiz fully keyboard-navigable
- “Tab” and “Enter” interactions tested

### **Screen Reader Support**

- ARIA labels on:
  - Navigation items
  - Quiz questions and choices
  - Reward items and redeem buttons

### **Responsive Design**

- Responsive pop-up layout (website panel)
- Web dashboard (optional) supports:
  - 1440px (desktop)
  - 768px (tablet)
  - 375px (mobile)

---

## 📊 Dashboard View Details

### **Dashboard Overview (Default Screen)**

- Research Time Progress Ring
- Coin Counter with +X coin indicators
- Streak Bar: 🔥 emojis and day count
- Button: Start/Stop Tracking (status-aware)

### **Graph Section**

- Bar chart of time tracked per day
- Hover tooltip shows site + minutes
- Trendline for streaks

---

## 🧠 Summary & Quiz UI

### **Daily Summary Input**

- Markdown-enabled text input
- AI-generated feedback tooltip (optional)
- Submit Button → triggers quiz generation

### **Quiz Screen**

- 3–5 multiple-choice questions
- Coins shown next to each correct answer
- Answer lock-in animation

---

## 🎁 Marketplace UI

### **Reward Grid**

- Card design for each item
  - Image, title, coin cost, category tag
  - "Redeem" button + tooltip if underfunded

### **Redemption Modal**

- Shows:
  - Reward name and coin cost
  - Confirm and Cancel buttons
  - Success message after action

---

## 🏆 Leaderboard UI

- Tabs: Global | Weekly | Monthly
- User’s rank highlighted in yellow
- Tooltips on ranks (“Top 5% this week!”)

---

## 🧑‍💼 Profile Page

- Avatar + username
- Goal setting input (minutes per day)
- Lifetime Coins Earned
- Pie Chart of category-based research

---

## 📚 Summary

**SugarTrack’s UI** borrows the visual rhythm and clean hierarchy of Levercast, adapting it to a website’s constraints and SugarTrack’s unique gamified mechanics. Its sidebar-first layout, collapsible flexibility, real-time content feedback, and accessible color scheme aim to keep users productive and motivated — while maintaining a fun, polished, and rewarding experience.

---
