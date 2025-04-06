from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user = User.get_by_email(email)
        
        # Check if user exists and password is correct
        if not user or not user.check_password(password):
            flash('Please check your login details and try again.', 'danger')
            return redirect(url_for('auth.login'))
            
        # If the above check passes, the user has the right credentials
        login_user(user, remember=remember)
        flash('Login successful!', 'success')
        
        # If the user was trying to access a page that requires login,
        # redirect them there after successful login
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        
        return redirect(url_for('main.dashboard'))
        
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        daily_goal = int(request.form.get('daily_goal', 120))
        
        # Check if user already exists
        user = User.get_by_email(email)
        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('auth.signup'))
            
        # Create a new user with the form data
        new_user = User.create(
            username=username,
            email=email,
            password=password,
            daily_goal_minutes=daily_goal
        )
        
        # Log in the new user
        login_user(new_user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.dashboard'))
        
    return render_template('signup.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login')) 