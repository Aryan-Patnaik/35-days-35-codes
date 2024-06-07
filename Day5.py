import bleach

ALLOWED_TAGS = ['b', 'i', 'u', 'em', 'strong', 'a', 'p', 'ul', 'ol', 'li', 'br']
ALLOWED_ATTRIBUTES = {'a' : ['href', 'title']}
ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']

def sanitize_input(user_input):
    sanitized_input = bleach.clean(
        user_input,
        tags = ALLOWED_TAGS,
        attributes = ALLOWED_ATTRIBUTES,
        protocols = ALLOWED_PROTOCOLS,
        strip = True
    )
    return sanitized_input

if __name__ == '__main__':
    raw_input = '<script>alert("XSS Attack!");</script><b>Valid Input</b>'
    print("Raw Input:", raw_input)
    safe_input = sanitize_input(raw_input)
    print("Sanitized Input:", safe_input)