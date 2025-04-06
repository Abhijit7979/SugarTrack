from flask import Blueprint, jsonify, request, Response, stream_with_context
from flask_login import login_required, current_user
import os
from groq import Groq
import json

tracking = Blueprint('tracking', __name__)

@tracking.route('/api/track/start', methods=['POST'])
@login_required
def start_tracking():
    # Mock implementation
    data = request.get_json()
    url = data.get('url')
    
    # In a real implementation, we would start timing and record it in the database
    
    return jsonify({
        'success': True,
        'message': f'Started tracking for URL: {url}',
        'sessionId': 'mock-session-123'
    })

@tracking.route('/api/track/stop', methods=['POST'])
@login_required
def stop_tracking():
    # Mock implementation
    data = request.get_json()
    session_id = data.get('sessionId')
    
    # In a real implementation, we would:
    # 1. Stop the timer
    # 2. Calculate duration
    # 3. Award coins based on time spent
    # 4. Update user's goal progress
    
    # Mock response - as if the user spent 35 minutes
    return jsonify({
        'success': True,
        'message': 'Tracking stopped',
        'durationMinutes': 35,
        'coinsEarned': 1, # 1 coin per 30 minutes
        'progress': 35/current_user.daily_goal_minutes * 100  # Using current user's goal
    })

@tracking.route('/api/tracking/status')
@login_required
def tracking_status():
    # Mock data for tracking status
    is_tracking = True
    current_session = {
        'url': 'https://learn.example.com/python',
        'startTime': '2025-04-05T15:30:00',
        'currentDuration': 12  # minutes
    }
    
    return jsonify({
        'isTracking': is_tracking,
        'currentSession': current_session if is_tracking else None
    })

@tracking.route('/api/chat/groq', methods=['POST'])
@login_required
def chat_with_groq():
    data = request.get_json()
    messages = data.get('messages', [])
    
    # Initialize Groq client with only the API key
    api_key = os.getenv('GROQ_API_KEY')
    
    # Create Groq client without any extra parameters
    groq_client = Groq(api_key=api_key)
    
    # Define generator function for streaming
    def generate():
        try:
            # Create chat completion with streaming, with only required parameters
            response = groq_client.chat.completions.create(
                messages=messages,
                model="llama-3.3-70b-versatile",
                stream=True
            )
            
            # Stream each chunk
            for chunk in response:
                if chunk.choices and len(chunk.choices) > 0:
                    # Using json.dumps instead of model_dump_json
                    chunk_json = json.dumps(chunk.dict()) if hasattr(chunk, 'dict') else json.dumps(chunk.model_dump())
                    yield f"data: {chunk_json}\n\n"
                    
        except Exception as e:
            # Log the error
            print(f"Error in Groq API: {str(e)}")
            # Return error message
            yield f"data: {{\"error\": \"{str(e)}\"}}\n\n"
    
    # Return streaming response
    return Response(
        stream_with_context(generate()),
        content_type='text/event-stream'
    ) 