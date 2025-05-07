# ============================ IMPORTS ============================ #
from string import (
    ascii_lowercase,                # A-Z
    ascii_uppercase,                # a-z
    digits,                         # 0-9
    punctuation)
# Import module to select random choice
from secrets import choice
# ============================ IMPORTS ============================ #


# =========================== CONSTANTS =========================== #
CHARS = (ascii_lowercase + ascii_uppercase + digits + punctuation)
# =========================== CONSTANTS =========================== #


# ======================= Generate Function ======================= #
def generate_pwd() -> str:
    """
    Prompts the user for password length and returns a generated password string.
    """
    try:

        length = int(input("How long would you like your password to be (Minimum 8): "))

        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")
        
        password = ''.join(choice(CHARS) for _ in range(length))
        return password
    
    except ValueError as e:
        print("Error:", e)
        return ""
# ======================= Generate Function ======================= #