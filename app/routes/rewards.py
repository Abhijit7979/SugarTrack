from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_login import login_required, current_user

rewards = Blueprint('rewards', __name__)

@rewards.route('/marketplace')
@login_required
def marketplace():
    # Mock rewards data
    reward_items = [
        {
            'rewardId': '001',
            'name': 'SugarTrack Hoodie',
            'coinCost': 200,
            'stock': 5,
            'category': 'swag',
            'image': 'hoodie.jpeg'
        },
        {
            'rewardId': '002',
            'name': 'Hackathon Pass',
            'coinCost': 150,
            'stock': 3,
            'category': 'ticket',
            'image': 'hackathon.jpeg'
        },
        {
            'rewardId': '003',
            'name': '30-min Mentorship Session',
            'coinCost': 100,
            'stock': 10,
            'category': 'mentorship',
            'image': 'mentorship.jpeg'
        },
        {
            'rewardId': '004',
            'name': 'SugarTrack Cap',
            'coinCost': 75,
            'stock': 15,
            'category': 'swag',
            'image': 'cap.jpeg'
        }
    ]
    
    # Use current_user instead of mock data
    return render_template('marketplace.html', rewards=reward_items, user=current_user)

@rewards.route('/api/reward/redeem', methods=['POST'])
@login_required
def redeem_reward():
    data = request.get_json()
    reward_id = data.get('rewardId')
    
    # Mock implementation - would check if user has enough coins
    # and if reward is in stock in a real application
    
    # For the prototype, just return success
    return jsonify({
        'success': True,
        'message': 'Reward redeemed successfully',
        'redemptionId': 'mock-redemption-456',
        'updatedCoinBalance': 25  # current_user.coin_balance - 50 (assuming reward cost is 50)
    })

@rewards.route('/redemption-history')
@login_required
def redemption_history():
    # Mock redemption history
    redemptions = [
        {
            'redemptionId': 'r001',
            'rewardName': 'SugarTrack Sticker Pack',
            'redeemedAt': '2023-03-25',
            'status': 'shipped'
        }
    ]
    
    return render_template('redemption_history.html', redemptions=redemptions) 