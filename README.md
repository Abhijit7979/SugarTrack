# SugarTrack - Gamified Research Platform

SugarTrack is a gamified research platform that helps users track their research time, earn rewards, and engage with a community of researchers.

## Features

- **Time Tracking**: Track time spent on research websites
- **Gamification**: Earn Sugar Coins for time spent researching
- **Reward System**: Redeem coins for physical and digital rewards
- **AI Research Assistant**: Get help with research tasks using Groq LLM
- **Progress Tracking**: Set daily goals and track your progress
- **Marketplace**: Exchange earned coins for rewards
- **Community**: See how you compare with others on the leaderboard

## AI Research Assistant

The AI Research Assistant feature uses Groq's LLama 3.3 70B Versatile model to provide high-quality research assistance. You can use it to:

- Explain complex concepts
- Summarize research papers
- Find relevant resources
- Get help with research questions

### Implementation Details

The AI Research Assistant is implemented using:

- Frontend: JavaScript streaming API for real-time responses
- Backend: Flask route that proxies requests to Groq API
- API: Groq SDK for Python

Responses are streamed in real-time using Server-Sent Events (SSE) for a smoother user experience.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with the following variables:
   ```
   FLASK_APP=app
   FLASK_ENV=development
   FLASK_SECRET_KEY=your_secret_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Run the application: `flask run`

## Environment Variables

- `FLASK_APP`: The Flask application to run
- `FLASK_ENV`: The environment to run Flask in (development, production)
- `FLASK_SECRET_KEY`: Secret key for Flask session
- `GROQ_API_KEY`: API key for Groq LLM integration

## Dependencies

- Flask: Web framework
- Flask-Login: User authentication
- Groq SDK: LLM integration
- Python-dotenv: Environment variable management

## License

MIT
