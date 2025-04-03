import os
import time
import pyotp
from flask import Flask, render_template, request, jsonify
from username_secretkey import user_secrets 

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    # Pass the list of usernames to the HTML template
    return render_template('index.html', usernames=user_secrets.keys())

@app.route('/usernames', methods=['GET'])
def get_usernames():
    # Return the list of usernames
    return jsonify({'usernames': list(user_secrets.keys())})

@app.route('/generate-secret', methods=['GET'])
def generate_secret():
    # Generate a random secret key
    secret = pyotp.random_base32()
    return jsonify({'secret': secret})

@app.route('/get-totp', methods=['POST'])
def get_totp():
    data = request.get_json()
    username = data.get('username', '')
    
    if not username or username not in user_secrets:
        return jsonify({'error': 'Invalid username'}), 400

    secret = user_secrets.get(username)
    
    try:
        # Create TOTP object
        totp = pyotp.TOTP(secret)
        
        # Get current code
        current_code = totp.now()
        
        # Calculate time remaining
        time_remaining = 30 - int(time.time()) % 30
        
        return jsonify({
            'code': current_code,
            'timeRemaining': time_remaining
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
