import hashlib
import time
from collections import defaultdict

# Constants
LOCKOUT_THRESHOLD = 8  # Number of allowed failed attempts
LOCKOUT_TIME = 300  # Lockout time in seconds (5 minutes)
RATE_LIMIT_WINDOW = 60  # Time window for rate limiting in seconds
RATE_LIMIT_THRESHOLD = 10  # Number of allowed attempts within the rate limit window

# User database (for demonstration purposes)
users = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest()
}

# Tracking failed login attempts
failed_attempts = defaultdict(list)
lockouts = {}

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_account_locked(username):
    """Checks if an account is locked."""
    if username in lockouts:
        lockout_time = lockouts[username]
        if time.time() - lockout_time < LOCKOUT_TIME:
            return True
        else:
            del lockouts[username]
    return False

def record_failed_attempt(username):
    """Records a failed login attempt."""
    failed_attempts[username].append(time.time())
    # Clean up old attempts outside the rate limit window
    failed_attempts[username] = [
        attempt for attempt in failed_attempts[username]
        if time.time() - attempt < RATE_LIMIT_WINDOW
    ]

def is_rate_limited(username):
    """Checks if an account is rate limited."""
    if len(failed_attempts[username]) >= RATE_LIMIT_THRESHOLD:
        return True
    return False

def login(username, password):
    """Attempts to log in a user."""
    if is_account_locked(username):
        print(f"Account {username} is locked. Please try again later.")
        return False

    if username in users and users[username] == hash_password(password):
        print(f"Login successful for {username}.")
        # Reset failed attempts after successful login
        if username in failed_attempts:
            del failed_attempts[username]
        return True
    else:
        print(f"Login failed for {username}.")
        record_failed_attempt(username)
        if len(failed_attempts[username]) >= LOCKOUT_THRESHOLD:
            lockouts[username] = time.time()
            print(f"Account {username} has been locked due to too many failed attempts.")
        elif is_rate_limited(username):
            print(f"Account {username} is temporarily rate limited due to too many attempts.")
        return False

if __name__ == "__main__":
    # Test the login function
    test_user1 = "user1"
    test_password1 = "password1"
    
    test_user2 = "user2"
    test_password2 = "password2"
    
    # Simulate failed login attempts
    for i in range(7):
        login(test_user1, "wrongpassword")
        time.sleep(1)  # Simulate time delay between attempts

    # Attempt to login with the correct password after lockout
    time.sleep(5)
    login(test_user1, test_password1)
    login(test_user2, test_password2)