import random
import string

# Set password length
password_length = 10

# Characters to choose from: letters, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(characters) for _ in range(password_length))

# Print the password
print("Generated Password:", password)
