from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session, Response
from flask_login import login_required, current_user
import random
import os
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('landing.html')

@main.route('/dashboard')
@login_required
def dashboard():
    # Mock data for demonstration
    user_stats = {
        'total_minutes': 1245,
        'average_daily': 95,
        'streak': 5,
        'coin_balance': current_user.coin_balance
    }
    
    daily_progress = {
        'goal': current_user.daily_goal_minutes,
        'current': 35,
        'percentage': 35 / current_user.daily_goal_minutes * 100
    }
    
    return render_template('dashboard.html', stats=user_stats, progress=daily_progress, user=current_user)

@main.route('/summary', methods=['GET', 'POST'])
@login_required
def summary():
    if request.method == 'POST':
        summary_text = request.form.get('summary')
        
        # Store the summary in the session so we can use it for quiz generation
        session['user_summary'] = summary_text
        
        # In a real app, we would save this summary to the database
        # and associate it with the current user and date
        
        # Now, we redirect to the quiz route which will generate a quiz based on the summary
        flash('Summary submitted! Here\'s a quiz based on your research.', 'success')
        return redirect(url_for('main.quiz'))
    
    return render_template('summary.html')

def generate_quiz_from_summary(summary_text):
    """Generate quiz questions from a research summary without using LLM"""
    # Simplified version with predefined questions
    return {
        "questions": [
            {
                "question": "What is a recursive function in Python?",
                "options": [
                    "A function that calls itself", 
                    "A function that calls another function", 
                    "A function that never terminates", 
                    "A function that iterates through lists"
                ],
                "correct_index": 0
            },
            {
                "question": "What is required in every proper recursive function?",
                "options": [
                    "A loop statement", 
                    "A base case to stop recursion", 
                    "At least two parameters", 
                    "Global variables"
                ],
                "correct_index": 1
            },
            {
                "question": "What is a common issue with recursive functions?",
                "options": [
                    "They are too fast", 
                    "They cannot handle mathematical operations", 
                    "Stack overflow with deep recursion", 
                    "They only work with strings"
                ],
                "correct_index": 2
            },
            {
                "question": "Which is an example of a problem well-suited for recursion?",
                "options": [
                    "Simple counting loops", 
                    "Basic arithmetic operations", 
                    "String concatenation", 
                    "Tree traversal algorithms"
                ],
                "correct_index": 3
            },
            {
                "question": "What is Python's default recursion limit?",
                "options": [
                    "1000", 
                    "100", 
                    "10000", 
                    "Unlimited"
                ],
                "correct_index": 0
            }
        ]
    }

@main.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    if request.method == 'POST':
        # In a real app, we would check the answers and award coins
        # based on correct answers
        
        # Mock - award 5 coins for completing the quiz
        current_user.coin_balance += 5
        flash('Quiz completed! You earned 5 Sugar Coins.', 'success')
        return redirect(url_for('main.dashboard'))
    
    # Check if there's a summary in the session
    user_summary = session.get('user_summary')
    
    if not user_summary:
        # Fallback to a mock summary for demonstration
        user_summary = """
        My research today focused on machine learning applications in healthcare. 
        I studied how neural networks can be used for early disease detection using patient data.
        The research showed that deep learning models can identify patterns in medical images
        with accuracy comparable to expert radiologists. I also learned about ethical considerations 
        regarding patient privacy and data security when implementing these systems.
        """
    
    # Generate quiz based on the summary
    quiz_data = generate_quiz_from_summary(user_summary)
    
    return render_template('quiz.html', quiz=quiz_data)

@main.route('/leaderboard')
@login_required
def leaderboard():
    # Mock leaderboard data
    users = [
        {'username': 'alex', 'coins': 350, 'streak': 12, 'totalCoins': 350, 'rank': 1},
        {'username': 'jordan', 'coins': 310, 'streak': 8, 'totalCoins': 310, 'rank': 2},
        {'username': 'sam', 'coins': 285, 'streak': 5, 'totalCoins': 285, 'rank': 3},
        {'username': current_user.username, 'coins': current_user.coin_balance, 'streak': 4, 'totalCoins': current_user.coin_balance, 'rank': 4},
        {'username': 'taylor', 'coins': 200, 'streak': 3, 'totalCoins': 200, 'rank': 5},
        {'username': 'casey', 'coins': 180, 'streak': 2, 'totalCoins': 180, 'rank': 6},
        {'username': 'morgan', 'coins': 150, 'streak': 1, 'totalCoins': 150, 'rank': 7},
    ]
    
    # Sort by coins
    users.sort(key=lambda x: x['coins'], reverse=True)
    
    # Add rank
    for i, user in enumerate(users):
        user['rank'] = i + 1
    
    return render_template('leaderboard.html', leaders=users)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', profile=current_user)

@main.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@main.route('/api/chat/groq', methods=['POST'])
@login_required
def chat_groq():
    data = request.get_json()
    messages = data.get('messages', [])
    
    # Find the user's last message
    user_message = ""
    for message in reversed(messages):
        if message.get('role') == 'user':
            user_message = message.get('content', '').strip().lower()
            break
    
    # Predefined responses
    responses = {
        "explain recursive functions in python": """
Recursive functions in Python are functions that call themselves within their own definition. They consist of:

1. Base case: A condition that stops the recursion
2. Recursive case: Where the function calls itself with a modified argument

Example of a recursive function to calculate factorial:

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)
```

Common recursive algorithms:
- Factorial calculation
- Fibonacci sequence
- Tree traversals
- Divide and conquer algorithms

Advantages:
- Code can be cleaner and more readable
- Natural solution for problems with recursive structure

Considerations:
- May cause stack overflow with deep recursion
- Often less efficient than iterative solutions
- Python's recursion limit (default 1000)

Tail recursion optimization isn't automatically applied in Python, unlike some other languages.
""",
        "how does blockchain technology work?": "Blockchain is a distributed ledger technology that maintains a continuously growing list of records (blocks) that are linked using cryptography. Each block contains a timestamp, transaction data, and a reference to the previous block, creating an immutable chain.",
        "summarize the key points of machine learning": "Machine learning is a subset of AI that enables systems to learn and improve from experience without explicit programming. Key points include: supervised vs. unsupervised learning, training data importance, feature selection, model evaluation, overfitting prevention, and various algorithms like regression, decision trees, neural networks, and clustering techniques.",
        "find resources for learning react": "For learning React, consider: React official documentation, freeCodeCamp's React course, React tutorials on YouTube by channels like Traversy Media and Web Dev Simplified, React project tutorials on Scrimba, and community resources like Stack Overflow and React subreddit."
    }
    
    def generate():
        try:
            # Check if we have a predefined response
            response_text = ""
            for key, value in responses.items():
                if key in user_message:
                    response_text = value
                    break
            
            # If no predefined response found, provide a default
            if not response_text:
                response_text = "I'm sorry, I don't have information on that topic. Please try asking about recursive functions in Python, blockchain technology, machine learning, or resources for learning React."
            
            # Split response into smaller chunks to simulate streaming
            chunks = [response_text[i:i+20] for i in range(0, len(response_text), 20)]
            
            for chunk in chunks:
                data = json.dumps({
                    "choices": [
                        {
                            "delta": {
                                "content": chunk
                            }
                        }
                    ]
                })
                yield f"data: {data}\n\n"
                
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            error_data = json.dumps({"error": str(e)})
            yield f"data: {error_data}\n\n"
    
    return Response(generate(), mimetype='text/event-stream') 