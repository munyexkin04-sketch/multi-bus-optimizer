import json
import os

# Simulate the app's load_users() function
USERS_FILE = 'users.json'
VALID_USERS = {}

if os.path.exists(USERS_FILE):
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if isinstance(users, dict):
            VALID_USERS = users
        else:
            VALID_USERS = {}
    except Exception as e:
        print(f"Error: {e}")
        VALID_USERS = {}
else:
    VALID_USERS = {}

print(f"VALID_USERS loaded: {list(VALID_USERS.keys())}")
print()

# Test all users
test_cases = [
    ('admin', 'password123'),
    ('user1', 'user1pass'),
    ('kudakwashe', 'Kuda@123'),
    ('admin', 'wrong_password'),
]

for username, password in test_cases:
    if username in VALID_USERS and VALID_USERS[username] == password:
        print(f"✓ LOGIN SUCCESS: {username} / {password}")
    else:
        print(f"✗ LOGIN FAILED: {username} / {password}")
