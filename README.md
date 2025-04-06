# SugarTrack - Gamified Research Platform 
### 418 hackathon hosted by Enigma under AEON 2025

SugarTrack is a gamified research platform that helps users track their research time, earn rewards, and engage with a community of researchers.

- [Product Requirements Document](https://github.com/Abhijit7979/SugarTrack/blob/main/prd.md)
- [Software Requirement Document](https://github.com/Abhijit7979/SugarTrack/blob/main/srd.md)
- [User Interface Design Document](https://github.com/Abhijit7979/SugarTrack/blob/main/ux.md)
  ##[Youtube Link](https://youtu.be/vr41ummdcZc)
## Features

- **Time Tracking**: Track time spent on research websites
- **Gamification**: Earn Sugar Coins for time spent researching
- **Reward System**: Redeem coins for physical and digital rewards
- **Progress Tracking**: Set daily goals and track your progress
- **Marketplace**: Exchange earned coins for rewards
- **Community**: See how you compare with others on the leaderboard

### Implementation Details
## Setup

  ### Step 1: setup the environment 💻
```bash
git clone https://github.com/Abhijit7979/SugarTrack.git
conda create -n project_env python=3.9
conda activate project_env
pip install -r requirements.txt
```

### Step 2: Create a `.env` file with the following variables:
   ```
   FLASK_APP=app
   FLASK_ENV=development
   FLASK_SECRET_KEY=your_secret_key_here
   ```
### Step 3 :Run the application: `flask run`

## Environment Variables

- `FLASK_APP`: The Flask application to run
- `FLASK_ENV`: The environment to run Flask in (development, production)
- `FLASK_SECRET_KEY`: Secret key for Flask session


## Dependencies

- Flask: Web framework
- Flask-Login: User authentication
- Python-dotenv: Environment variable management

