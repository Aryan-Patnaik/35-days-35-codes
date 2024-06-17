import random  # Importing the random module for shuffling quiz options

class CyberSecurityModule:
    def __init__(self):
        """Initialize the CyberSecurityModule with lessons data."""
        self.lessons = [
            {
                'title': 'Lesson 1: Password Security',
                'content': 'In this lesson, you will learn about the importance of strong passwords and how to create them.',
                'quiz': {
                    'questions': [
                        {
                            'question': 'What makes a password strong?',
                            'options': ['Length and complexity', 'Short and simple', 'Using common words'],
                            'answer': 'Length and complexity'
                        },
                        {
                            'question': 'Why is it important to avoid using common words or phrases as passwords?',
                            'options': ['They are easy to remember', 'They are difficult for hackers to guess', 'They are susceptible to dictionary attacks'],
                            'answer': 'They are susceptible to dictionary attacks'
                        },
                        {
                            'question': 'Which of the following is a recommended practice for creating strong passwords?',
                            'options': ['Using personal information like birthdays', 'Using a combination of letters, numbers, and special characters', 'Using short passwords for easy memorization'],
                            'answer': 'Using a combination of letters, numbers, and special characters'
                        },
                        {
                            'question': 'What is a passphrase?',
                            'options': ['A single word password', 'A sequence of words used as a password', 'A biometric authentication method'],
                            'answer': 'A sequence of words used as a password'
                        },
                        {
                            'question': 'What does two-factor authentication add to the security of an account?',
                            'options': ['A second password', 'A second form of verification', 'A stronger encryption algorithm'],
                            'answer': 'A second form of verification'
                        }
                    ]
                }
            },
            {
                'title': 'Lesson 2: Phishing Awareness',
                'content': 'This lesson covers how to recognize phishing attempts and avoid falling victim to them.',
                'quiz': {
                    'questions': [
                        {
                            'question': 'Which of the following is a common phishing technique?',
                            'options': ['Sending deceptive emails that appear to be from a trusted source', 'Sending physical letters with malicious content', 'Making phone calls to request personal information'],
                            'answer': 'Sending deceptive emails that appear to be from a trusted source'
                        },
                        {
                            'question': 'How can you identify a phishing email?',
                            'options': ['By checking for spelling and grammar errors', 'By looking at the sender\'s email address and domain', 'By the presence of attachments or links that you were not expecting'],
                            'answer': 'By looking at the sender\'s email address and domain'
                        },
                        {
                            'question': 'What should you do if you receive a suspicious email asking for your personal information?',
                            'options': ['Reply to the email with your information', 'Ignore the email and delete it', 'Click on any links provided to verify the request'],
                            'answer': 'Ignore the email and delete it'
                        },
                        {
                            'question': 'What is a common goal of phishing attacks?',
                            'options': ['To install malware on your computer', 'To improve email communication', 'To promote a product or service'],
                            'answer': 'To install malware on your computer'
                        },
                        {
                            'question': 'How can you protect yourself from phishing attacks?',
                            'options': ['By enabling two-factor authentication', 'By sharing your passwords with trusted friends', 'By using the same password for multiple accounts'],
                            'answer': 'By enabling two-factor authentication'
                        }
                    ]
                }
            },
            {
                'title': 'Lesson 3: Social Engineering Awareness',
                'content': 'This lesson covers how to recognize and defend against social engineering tactics used to manipulate individuals into divulging confidential information.',
                'quiz': {
                    'questions': [
                        {
                            'question': 'What is social engineering?',
                            'options': ['A method to improve social skills', 'A psychological manipulation tactic', 'A hardware security measure'],
                            'answer': 'A psychological manipulation tactic'
                        },
                        {
                            'question': 'Which of the following is an example of social engineering?',
                            'options': ['Phishing emails', 'Software vulnerabilities', 'Network firewall breaches'],
                            'answer': 'Phishing emails'
                        },
                        {
                            'question': 'How can you protect against social engineering attacks?',
                            'options': ['By sharing personal information freely', 'By being cautious of unsolicited requests for information', 'By ignoring security awareness training'],
                            'answer': 'By being cautious of unsolicited requests for information'
                        },
                        {
                            'question': 'What is pretexting?',
                            'options': ['A technique to enhance memory', 'A form of social engineering where attackers create a fabricated scenario', 'A type of encryption algorithm'],
                            'answer': 'A form of social engineering where attackers create a fabricated scenario'
                        },
                        {
                            'question': 'Why is awareness training important for defending against social engineering?',
                            'options': ['It increases employee productivity', 'It helps employees recognize and respond to suspicious behavior', 'It reduces the need for security controls'],
                            'answer': 'It helps employees recognize and respond to suspicious behavior'
                        }
                    ]
                }
            },
            {
                'title': 'Lesson 4: Internet and Email Security',
                'content': 'This lesson focuses on safe practices for using the internet and email securely to protect against various cyber threats.',
                'quiz': {
                    'questions': [
                        {
                            'question': 'Why is it important to use strong, unique passwords for online accounts?',
                            'options': ['To make it easier to remember passwords', 'To minimize the impact of data breaches', 'To impress friends and colleagues'],
                            'answer': 'To minimize the impact of data breaches'
                        },
                        {
                            'question': 'What should you do before clicking on links in emails or on websites?',
                            'options': ['Verify the source of the link', 'Close your eyes', 'Click on them without hesitation'],
                            'answer': 'Verify the source of the link'
                        },
                        {
                            'question': 'What is malware?',
                            'options': ['A type of computer hardware', 'A software designed to harm or infiltrate a computer system', 'A digital currency'],
                            'answer': 'A software designed to harm or infiltrate a computer system'
                        },
                        {
                            'question': 'How can you secure your email communications?',
                            'options': ['By sending emails with sensitive information in plain text', 'By using encryption for sensitive information', 'By sharing email passwords with colleagues'],
                            'answer': 'By using encryption for sensitive information'
                        },
                        {
                            'question': 'What is a VPN and how does it help protect your internet connection?',
                            'options': ['A virtual private network that encrypts your internet traffic', 'A video playing network', 'A type of spam filter'],
                            'answer': 'A virtual private network that encrypts your internet traffic'
                        }
                    ]
                }
            }
        ]

    def display_lessons(self):
        """Display lessons' titles, content, and associated quizzes."""
        for lesson in self.lessons:
            print(lesson['title'])
            print(lesson['content'])
            self.display_quiz(lesson['quiz'])

    def display_quiz(self, quiz):
        """Display quiz questions and handle user interaction."""
        for i, question in enumerate(quiz['questions'], 1):
            print(f"\nQuestion {i}: {question['question']}")
            
            options = question['options']
            random.shuffle(options)  # Shuffle options to avoid bias
            
            for j, option in enumerate(options, 1):
                print(f"{j}. {option}")
            
            user_answer_index = int(input("Your answer (enter option number): ").strip()) - 1
            
            correct_answer_index = options.index(question['answer'])
            self.evaluate_answer(user_answer_index, correct_answer_index)

    def evaluate_answer(self, user_answer_index, correct_answer_index):
        """Evaluate user's answer and provide feedback."""
        if user_answer_index == correct_answer_index:
            print("Correct!\n")
        else:
            correct_answer = correct_answer_index + 1
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

if __name__ == "__main__":
    # Create an instance of CyberSecurityModule and display lessons
    module = CyberSecurityModule()
    module.display_lessons()
