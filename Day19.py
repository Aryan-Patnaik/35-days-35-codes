import random

def social_engineering_attack():
    employees = [
        {"name": "Alice", "role": "HR Manager", "email": "alice@example.com"},
        {"name": "Bob", "role": "IT Administrator", "email": "bob@example.com"},
        {"name": "Charlie", "role": "Sales Representative", "email": "charlie@example.com"},
        {"name": "David", "role": "Finance Director", "email": "david@example.com"}
    ]
    
    victim = random.choice(employees)
    
    attack_type = random.choice(["phishing email", "phone call"])
    
    if attack_type == "phishing email":
        phishing_subject = "Urgent: Account Verification Needed"
        phishing_body = f"Hello,\n\nThis is {victim['name']} from {victim['role']} department. We are currently upgrading our systems and need to verify your account details. Please click on the following link to verify your account:\n\nhttp://evilwebsite.com/verify?id=123456\n\nThank you,\n{victim['name']}"
        
        print("Phishing Email:")
        print(f"To: [Employee Email]")
        print(f"Subject: {phishing_subject}")
        print(f"Body:\n{phishing_body}")
        
    elif attack_type == "phone call":
        script_intro = f"Hello, this is {victim['name']} from {victim['role']} department."
        script_request = "I need your help with verifying some account details."
        script_urgency = "It's urgent and requires immediate attention."
        
        print("Phone Call Script:")
        print(script_intro)
        print(script_request)
        print(script_urgency)
    simulate_response(victim)

def simulate_response(victim):
    response = input(f"What would you do if you received this {random.choice(['email', 'phone call'])} from {victim['name']} ({victim['role']})? ")
    if "link" in response.lower() or "information" in response.lower():
        print("Warning: You might have fallen for a phishing attempt!")
    else:
        print("Good response! Always verify the authenticity of such requests.")

def main():
    print("Welcome to Social Engineering Training Scenario!")
    print("You will encounter simulated social engineering attacks.")
    print("Respond appropriately to avoid falling into traps.\n")
    
    while True:
        input("Press Enter to simulate a social engineering attack...")
        social_engineering_attack()
        
        choice = input("\nDo you want to continue training? (yes/no): ")
        if choice.lower() != 'yes':
            print("\nTraining session ended.")
            break

if __name__ == "__main__":
    main()
